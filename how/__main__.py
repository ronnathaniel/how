
"""
Ask More Questions.
Author: Ron Nathaniel
"""

from how.cli import parse_args, display_results
from how.util import gen_next_n
from how.crawler import ask_any, ask_sof, ask_google


def run():
    args = parse_args()
    query = args.get('query', '')
    query = ' '.join(query)
    n = args.get('n')
    g = args.get('g')
    sites = args.get('sites')
    results = []

    if not sites:
        results = ask_google(query,limit=n) if g else ask_sof(query, limit=n)
        display_results(results)
    else:
        for site in sites:
            results = ask_any(query,limit=n,site=site)
            print()
            display_results(results,site)


if __name__ == '__main__':
    run()