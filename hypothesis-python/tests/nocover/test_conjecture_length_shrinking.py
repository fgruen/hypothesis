# coding=utf-8
#
# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis-python
#
# Most of this work is copyright (C) 2013-2018 David R. MacIver
# (david@drmaciver.com), but it contains contributions by others. See
# CONTRIBUTING.rst for a full list of people who may hold copyright, and
# consult the git log if you need to determine who owns an individual
# contribution.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at http://mozilla.org/MPL/2.0/.
#
# END HEADER

from __future__ import division, print_function, absolute_import

from random import Random

import hypothesis.strategies as st
from hypothesis import given, example
from hypothesis.internal.conjecture.shrinking import Length

sizes = st.integers(0, 100)


@example(m=0, n=1)
@given(sizes, sizes)
def test_shrinks_down_to_size(m, n):
    m, n = sorted((m, n))
    assert Length.shrink(
        [0] * n + [1], lambda ls: len(ls) >= m + 1 and ls[-1] == 1,
        random=Random(0)
    ) == (0,) * m + (1,)


def test_will_shrink_to_zero():
    assert Length.shrink([1], lambda x: True, random=Random(0)) == ()
