/* New portable matrix-multiplication reference, not recovered Gemmini code.
 * Deterministic, naive dense FP32 GEMM: C = A * B.
 * No accelerator or RISC-V instruction support is claimed.
 */
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static double seconds_now(void) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (double)ts.tv_sec + (double)ts.tv_nsec * 1.0e-9;
}
int main(int argc, char **argv) {
    int n = 64;
    if (argc > 1) {
        char *end = NULL;
        errno = 0;
        long val = strtol(argv[1], &end, 10);
        if (errno || end == argv[1] || *end || val < 1 || val > 512) {
            fputs("usage: matmul_reference [n=1..512]\n", stderr);
            return 2;
        }
        n = (int)val;
    }
    size_t count = (size_t)n * (size_t)n;
    float *a = calloc(count, sizeof(float));
    float *b = calloc(count, sizeof(float));
    float *c = calloc(count, sizeof(float));
    if (!a || !b || !c) {
        fputs("memory allocation failed\n", stderr);
        free(a); free(b); free(c);
        return 1;
    }
    for (size_t i = 0; i < count; ++i) {
        a[i] = (float)((i % 17) - 8) / 16.0f;
        b[i] = (float)((i % 13) - 6) / 16.0f;
    }
    double t0 = seconds_now();
    for (int i = 0; i < n; ++i) {
        for (int k = 0; k < n; ++k) {
            for (int j = 0; j < n; ++j) {
                c[(size_t)i*n+j] += a[(size_t)i*n+k] * b[(size_t)k*n+j];
            }
        }
    }
    double elapsed = seconds_now() - t0;
    double checksum = 0.0;
    for (size_t i = 0; i < count; ++i) checksum += c[i];
    printf("reference=cpu-naive n=%d seconds=%.9f checksum=%.8f\n",
           n, elapsed, checksum);
    free(a); free(b); free(c);
    return 0;
}

