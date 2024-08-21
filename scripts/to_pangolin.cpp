#include<cstdio>
const int N = 1 << 23, M = 1 << 28;
long long row_ptr[N];
int col_idx[M];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%lld", row_ptr + i);
    }
    row_ptr[n] = m;
    int max_degree = 0;
    for (int i = 0; i < n; i++) {
        int buf_size = row_ptr[i + 1] - row_ptr[i];
        if (buf_size > max_degree) max_degree = buf_size;
    }

    FILE *fp = fopen("graph.meta.txt", "w");
    fprintf(fp, "%d\n%d\n", n, m);
    fprintf(fp, "4 8 1 2\n");
    fprintf(fp, "%d\n", max_degree);
    fprintf(fp, "0\n");
    fprintf(fp, "0\n");
    fprintf(fp, "0\n");
    fclose(fp);

    fp = fopen("graph.vertex.bin", "wb");
    fwrite(row_ptr, sizeof(long long), n + 1, fp);
    fclose(fp);

    for (int i = 0; i < m; i++) {
        int x;
        scanf("%d", &x);
        col_idx[i] = x;
    }
    fp = fopen("graph.edge.bin", "wb");
    fwrite(col_idx, sizeof(int), m, fp);
    fclose(fp);
    
    return 0;
}