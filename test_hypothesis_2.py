#! /usr/bin/env python3

# from https://alexwlchan.net/2016/12/strings-are-terrible/

from hypothesis import given, strategies as st
from hypothesis import example


@given(st.text())
#@example('ß')
def test_changing_case_preserves_length(xs):
    assert len(xs) == len(xs.upper())

