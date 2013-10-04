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

    def test_address_string(self):
        assert gateaddr.pretty([0, 2, 34, 10, 27, 24, 20]) == "AC8 Q1Y U"
