
"""
Ask More Questions.
Author: Ron Nathaniel
"""

from how.cli import parse_args, display_results
from how.util import gen_next_n
from how.crawler import ask_sof


def run():
    args = parse_args()
    query = args.get('query', '')
    query = ' '.join(query)
    n = args.get('n')

    results = ask_sof(query, limit=n)

    display_results(gen_next_n(results, n))


if __name__ == '__main__':
    run()