"""New CPU convolution comparison kernel. NHWC x HWIO, stride 1, valid padding.

Neither kernel is asserted to represent the user's lost historic NeoCPU code.
"""
from __future__ import annotations
import numpy as np


def _check(x: np.ndarray, w: np.ndarray):
    x = np.asarray(x, dtype=np.float32)
    w = np.asarray(w, dtype=np.float32)
    if x.ndim != 4 or w.ndim != 4:
        raise ValueError("Expected NHWC input and HWIO weights")
    n, h, width, channels = x.shape
    kh, kw, wc, filters = w.shape
    if channels != wc or h < kh or width < kw:
        raise ValueError("Incompatible channel counts or kernel larger than input")
    return x, w, (n, h-kh+1, width-kw+1, filters)


def conv2d_reference(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    x, w, shape = _check(x, w)
    n, oh, ow, filters = shape
    kh, kw, _, _ = w.shape
    out = np.empty(shape, dtype=np.float32)
    for batch in range(n):
        for iy in range(oh):
            for ix in range(ow):
                patch = x[batch, iy:iy+kh, ix:ix+kw, :]
                for f in range(filters):
                    out[batch, iy, ix, f] = np.sum(patch * w[:, :, :, f],
                                                       dtype=np.float32)
    return out


def conv2d_im2col(x: np.ndarray, w: np.ndarray) -> np.ndarray:
    x, w, shape = _check(x, w)
    n, oh, ow, filters = shape
    kh, kw, _, _ = w.shape
    # Materialize the patch matrix for a fair, explicit im2col baseline.
    rows = np.empty((n*oh*ow, kh*kw*x.shape[3]), dtype=np.float32)
    index = 0
    for batch in range(n):
        for iy in range(oh):
            for ix in range(ow):
                rows[index] = x[batch, iy:iy+kh, ix:ix+kw, :].ravel()
                index += 1
    out = rows @ w.reshape(-1, filters)
    return out.reshape(shape)

