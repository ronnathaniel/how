
"""
Ask More Questions.
Author: Ron Nathaniel
"""

from typing import Iterator


def gen_next_n(entities: Iterator, n: int) -> list:
    generated = []
    for _ in range(n):
        popped = entities.__next__()
        if not popped:
            return generated
        generated.append(popped)
    return generated
