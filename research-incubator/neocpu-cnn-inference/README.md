# NeoCPU — CNN Inference Optimization Reconstruction Workspace

**Status: newly written CPU convolution reference and correctness tests. No original NeoCPU source or claimed historical measurements have been restored.**

## Research question

How does a straightforward NHWC convolution kernel compare with an `im2col` + matrix-multiplication implementation on identical FP32 inputs, filters, and host CPU hardware? This reproduces **a general kernel-optimization comparison**, not a confirmed reconstruction of the historical NeoCPU project.

The original project was previously described as exploring CPU CNN inference optimization, tiling/layout, ARM/x86 execution and lower latency/memory use. Until source and measurements are recovered, those are **project descriptions**, not verified claims attached to this reference.

## Reproducible new implementation

- `neocpu/conv.py`: exact reference 2D valid convolution (NHWC inputs, HWIO kernels) and an `im2col` alternative.
- `tests/test_conv.py`: randomized numerical equivalence tests.
- `benchmark.py`: a timing harness that refuses to claim a fixed speedup; results depend on the host.

```bash
python -m pip install numpy pytest
python -m pytest -q
python benchmark.py --batch 1 --height 16 --width 16 --channels 3 --filters 8
```

## Publication roadmap

Restore any original `NCHW[x]c` packing, layout transformations, vectorization, cache-blocking, quantization, threading, allocator, and PBQP scheduling contributions, including appropriate build flags and machine specifications. Compare equivalent computation and verify accuracy before reporting latency or power.

**This is new reference code, not a recovered original implementation.**

