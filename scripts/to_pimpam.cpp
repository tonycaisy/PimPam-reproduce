#include<cstdio>
const int N = 1 << 23, M = 1 << 28;
int row_ptr[N];
int col_idx[M];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    for (int i = 0; i < n; i++) {
        scanf("%d", row_ptr + i);
    }
    for (int i = 0; i < m; i++) {
        scanf("%d", col_idx + i);
    }
    fwrite(&n, sizeof(int), 1, stdout);
    fwrite(&m, sizeof(int), 1, stdout);
    fwrite(row_ptr, sizeof(int), n, stdout);
    fwrite(col_idx, sizeof(int), m, stdout);
    return 0;
}