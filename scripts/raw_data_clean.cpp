// remove self loops and empty nodes
// renumber nodes and transfer into undirected graph
// output in CSR format

#include<cstdio>
#include<algorithm>

using std::sort;
using std::unique;

const int N = 1 << 23, M = 1 << 28;

int first[N];
int *next, *v;
inline void add_edge(int u, int v) {
    static int ct = 0;
    next[++ct] = first[u];
    first[u] = ct;
    ::v[ct] = v;
}

char buffer[1 << 10];
void read_input() {
    // omit the first 4 lines
    for (int i = 0; i < 4; i++) {
        fgets(buffer, sizeof(buffer), stdin);
    }
    int u, v;
    while (scanf("%d%d", &u, &v) != EOF) {
        // omit self loops
        if (v == u) continue;
        add_edge(u, v);
        add_edge(v, u);
    }
}

int renumbered[N];
int renumber() {
    int ct = 0;
    for (int i = 0; i < N; i++) {
        if (first[i] != 0) {
            renumbered[i] = ct++;
        }
        else {
            renumbered[i] = -1;
        }
    }
    return ct;
}

int row_ptr[N];
int *col_ind;
int col_buf[N];
int main() {
    next = new int[M];
    v = new int[M];
    col_ind = new int[M];
    read_input();
    int n = renumber();
    int m = 0;
    for (int i = 0; i < N; i++) if (first[i] != 0) {
        row_ptr[renumbered[i]] = m;
        int buf_size = 0;
        for (int j = first[i]; j != 0; j = next[j]) {
            col_buf[buf_size++] = renumbered[v[j]];
        }
        sort(col_buf, col_buf + buf_size);
        int *end = unique(col_buf, col_buf + buf_size);
        for (int *p = col_buf; p != end; p++) {
            col_ind[m++] = *p;
        }
        if (renumbered[i] % 100000 == 0) fprintf(stderr, "%d\n", renumbered[i]);
    }
    printf("%d\n%d\n", n, m);
    for (int i = 0; i < n; i++) {
        printf("%d\n", row_ptr[i]);
    }
    for (int i = 0; i < m; i++) {
        printf("%d\n", col_ind[i]);
    }
    return 0;
}