"""Measure new CPU reference implementations; no precomputed result claims."""
from __future__ import annotations
import argparse
import json
import platform
from time import perf_counter
import numpy as np
from neocpu import conv2d_reference, conv2d_im2col


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch",type=int,default=1)
    parser.add_argument("--height",type=int,default=16)
    parser.add_argument("--width",type=int,default=16)
    parser.add_argument("--channels",type=int,default=3)
    parser.add_argument("--filters",type=int,default=8)
    parser.add_argument("--repeats",type=int,default=5)
    args=parser.parse_args()
    if min(args.batch,args.height,args.width,args.channels,args.filters,args.repeats)<1:
        parser.error("all dimensions and repeats must be positive")
    if min(args.height,args.width)<3:
        parser.error("minimum spatial dimension is 3")
    rng=np.random.default_rng(42)
    x=rng.normal(size=(args.batch,args.height,args.width,args.channels)).astype(np.float32)
    w=rng.normal(size=(3,3,args.channels,args.filters)).astype(np.float32)
    expected=conv2d_reference(x,w)
    np.testing.assert_allclose(conv2d_im2col(x,w),expected,rtol=2e-5,atol=2e-5)
    timings={}
    for label,fn in [("reference",conv2d_reference),("im2col",conv2d_im2col)]:
        fn(x,w)
        samples=[]
        for _ in range(args.repeats):
            start=perf_counter()
            fn(x,w)
            samples.append((perf_counter()-start)*1000)
        timings[label]={"median_ms":float(np.median(samples)),"samples_ms":samples}
    report={"status":"locally_measured_new_reference","python":platform.python_version(),
            "numpy":np.__version__,"backend":"CPU / NumPy","input_shape":list(x.shape),
            "filter_shape":list(w.shape),"checks_passed":True,"timing":timings,
            "im2col_vs_reference":timings["reference"]["median_ms"]/timings["im2col"]["median_ms"],
            "disclaimer":"Not historic NeoCPU measurements; this is a new CPU reference."}
    print(json.dumps(report,indent=2))


if __name__=="__main__":main()

