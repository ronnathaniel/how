
"""
Ask More Questions.
Author: Ron Nathaniel
"""

from googlesearch import search


def ask_google(query: str, limit: int = 20) -> list:
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


def ask_any(query: str, limit: int = 20, site: str = None) -> list:
    """
    Ask Any Site, Anything.
    :param query: Query to search
    :param limit: Total results to return
    :param site: Site to search
    :return: List of result URIs
    """
    if site:
        query += ' site:' + site
    results = ask_google(
        query=query,
        limit=limit,
    )

    return results


def ask_sof(query: str, limit: int = 20) -> list:
    """
    Ask StackOverflow Anything.
    :param query: Query to StackOverflow search
    :param limit: Total results to return
    :return: List of result URIs
    """
    results = ask_any(
        query=query,
        limit=limit,
        site='stackoverflow.com',
    )

    return results


if __name__ == '__main__':
    # example usage
    res = ask_sof(
        'exit vi'
    )
