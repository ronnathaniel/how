
from search_engine_parser.core.engines.google import Search as GoogleSearch
from search_engine_parser.core.engines.stackoverflow import Search as SOFSearch
from googleapi import google
from googlesearch import search
from typing import Generator

from how.util import gen_next_n


# # Singleton
# google_srch = None
# sof_srch = None
#
# def get_google_srch():
#     """
#
#     :return:
#     """
#     global google_srch
#     if not google_srch:
#         google_srch = GoogleSearch()
#     return google_srch


# def get_sof_srch():
#     """
#
#     :return:
#     """
#     global sof_srch
#     if not sof_srch:
#         sof_srch = SOFSearch()
#     return sof_srch


def ask_google(query: str, limit=20,) -> Generator:
    """

    :return:
    """
    results = search(
        query, stop=limit,
    )

    return results


def ask_sof(query: str, limit=20, ) -> Generator:
    """

    :return:
    """
    results = ask_google(
        query + ' site:stackoverflow.com',
        limit
    )

    return results


if __name__ == '__main__':
    res = ask_sof(
        'exit vi'
    )

    print(gen_next_n(res, 5))
