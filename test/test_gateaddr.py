"""
Tests for `quickdial.gateaddr` module.
"""
import pytest
from quickdial import gateaddr


class TestGateAddr(object):

    def test_generate_length(self):
        for addr in gateaddr.generate(5, count=10):
            assert len(addr) == 7

    def test_generate_origin(self):
        for addr in gateaddr.generate(5, count=10):
            assert addr[-1] == 5
