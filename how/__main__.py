
"""
Ask More Questions.
Author: Ron Nathaniel, Itay Bachar
"""

from how.cli import parse_args, display_results
from how.crawler import ask_any, ask_sof, ask_google


def run():
    args = parse_args()

    query = args.get('query', '')
    query = ' '.join(query)

    n = args.get('n')
    g = args.get('g')
    sites = args.get('sites')

    if sites:
        for site in sites:
            results = ask_any(query, limit=n, site=site)
            display_results(results, site)
    elif g:
        results = ask_google(query, limit=n)
        display_results(results, 'google.com')
    else:
        results = ask_sof(query, limit=n)
        display_results(results, 'stackoverflow.com')


if __name__ == '__main__':
    run()
