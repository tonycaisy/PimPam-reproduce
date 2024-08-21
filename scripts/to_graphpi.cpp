#include<cstdio>
const int N = 1 << 23, M = 1 << 28;
int row_ptr[N];
int main() {
    int n, m;
    scanf("%d%d", &n, &m);
    printf("%d %d\n", n, m >> 1);
    for (int i = 0; i < n; i++) {
        scanf("%d", row_ptr + i);
    }
    row_ptr[n] = m;
    for (int i = 0; i < n; i++) {
        int buf_size = row_ptr[i + 1] - row_ptr[i];
        for (int j = 0; j < buf_size; j++) {
            int x;
            scanf("%d", &x);
            if (x > i) printf("%d %d\n", i, x);
        }
    }
    return 0;
}