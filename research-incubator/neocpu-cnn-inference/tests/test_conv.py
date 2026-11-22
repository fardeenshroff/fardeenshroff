import numpy as np
import pytest
from neocpu import conv2d_reference, conv2d_im2col


@pytest.mark.parametrize("shape,filter_shape", [
    ((1,5,5,2),(3,3,2,4)),
    ((2,7,8,3),(2,3,3,2)),
    ((1,4,4,1),(1,1,1,1)),
])
def test_im2col_matches_reference(shape, filter_shape):
    gen = np.random.default_rng(42)
    x = gen.normal(size=shape).astype(np.float32)
    w = gen.normal(size=filter_shape).astype(np.float32)
    np.testing.assert_allclose(conv2d_im2col(x,w),
                               conv2d_reference(x,w),
                               rtol=2e-5, atol=2e-5)


def test_rejects_inconsistent_channels():
    with pytest.raises(ValueError):
        conv2d_im2col(np.zeros((1,4,4,3)), np.zeros((3,3,2,4)))

