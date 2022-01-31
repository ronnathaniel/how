
"""
Ask More Questions.
Author: Ron Nathaniel
"""

from typing import Generator
from googlesearch import search

from how.util import gen_next_n


def ask_google(query: str, limit=20,) -> list:
    """
    Ask Google Anything.
    :param query: Query to google search
    :param limit: Total results to return
    :return: List of result URIs
    """
    results = search(
        query,
        num_results=limit,
    )

    return results


def ask_sof(query: str, limit=20, ) -> list:
    """
    Ask StackOverflow Anything.
    :param query: Query to StackOverflow search
    :param limit: Total results to return
    :return: List of result URIs
    """
    results = ask_google(
        query=query + ' site:stackoverflow.com',
        limit=limit
    )

    return results


if __name__ == '__main__':
    # Example Usage
    res = ask_sof(
        'exit vi'
    )

    print(gen_next_n(res, 5))
