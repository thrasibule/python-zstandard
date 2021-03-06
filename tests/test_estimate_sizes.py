import unittest

import zstandard as zstd

from . common import (
    make_cffi,
)


@make_cffi
class TestSizes(unittest.TestCase):
    def test_decompression_size(self):
        size = zstd.estimate_decompression_context_size()
        self.assertGreater(size, 100000)

