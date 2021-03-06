from itertools import chain, repeat, islice
from pipe import take, chain_with

import pytest

lst1 = [1, 2, 3]


def pythonic_pad_to(seq, padded_length):
    return seq + [None] * (padded_length - len(seq))


def iter_pad_to(seq, padded_length):
    return islice(chain(seq, repeat(None)), padded_length)


def pipe_pad_to(seq, padded_length):
    return (seq | chain_with(repeat(None))
                | take(padded_length))


@pytest.mark.parametrize(
    "seq, pad_to_func, padded_length", [
        (lst1, pythonic_pad_to, 6),
        (lst1, iter_pad_to, 6),
        (lst1, pipe_pad_to, 6),
        #    (range(4), pythonic_always_6_elements, 11),
        (range(4), iter_pad_to, 11),
        (range(4), pipe_pad_to, 11),
    ],
    ids=lambda v: None if callable(v) else str(v))
def test_iter(seq, pad_to_func, padded_length):
    assert len(list(pad_to_func(seq, padded_length))) == padded_length
