
"""
Ask More Questions.
Author: Ron Nathaniel, Itay Bachar
"""

import sys
from enum import Enum
import argparse
import colorama

colorama.init(wrap=False)
stream_err = colorama.AnsiToWin32(sys.stderr).stream

ARGS = {
    ('query',): {
        'type': str,
        'metavar': 'QUERY',
        'nargs': '+',
        'help': 'Query to Search',
    },
    ('-n', '--num'): {
        'type': int,
        'metavar': 'n',
        'nargs': '?',
        'help': 'Query to Search',
        'default': 5,
    },
    ('-g', '--google'): {
        'action': 'store_true',
        'help': 'Search on Google',
    },
    ('-s', '--sites'): {
        'type': str,
        'nargs': 1,
        'help': 'Sites to search from',
        'metavar': 'url[,url,...]',
    },
}


class ConsoleStyles(str, Enum):
    RIGHT_ARROW = u'\u279c'
    YELLOW = u'\033[1;33m'
    BLUE_LIGHT = u'\033[1;36m'
    TEST = u'\033[1;38m'
    PURPLE = u'\033[1;35m'
    BLUE_DARK = u'\033[1;34m'
    GREEN = u'\033[1;32m'
    RED = u'\033[1;31m'
    BOLD = u'\033[1m'
    UNDERLINE = u'\033[4m'
    END = u'\033[0m'


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description='how')
    for op, kwargs in ARGS.items():
        parser.add_argument(*op, **kwargs)
    
    args_parsed = vars(parser.parse_args())
    
    query = args_parsed.get('query', [])
    n = args_parsed.get('num', 5)
    g = args_parsed.get('google', False)

    sites = args_parsed.get('sites', [''])
    if sites:
        sites = sites[0]
        sites = sites.split(',')

    return {
        'query': query,
        'n': n,
        'g': g,
        'sites': sites,
    }


def display_results(res: list = None, header: str = None) -> None:
    if header:
        print('\n' + "Results from " + ConsoleStyles.YELLOW + header + ConsoleStyles.END + ':' + ConsoleStyles.END)
    for r in res:
        print(ConsoleStyles.RIGHT_ARROW + '\r\t', end='')
        print(r)
    if not res:
        print('None found.')
        print(ConsoleStyles.RED + 'If a discrepency is found ' + ConsoleStyles.RIGHT_ARROW + ' contact the team at rnathaniel7@gmail.com.' + ConsoleStyles.END)