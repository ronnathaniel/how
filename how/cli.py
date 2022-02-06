
"""
Ask More Questions.
Author: Ron Nathaniel
"""

import sys
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
    ('-n',): {
        'type': int,
        'metavar': 'n',
        'nargs': '?',
        'help': 'Query to Search',
        'default': 5,
    },
    ('-g','--google'): {
        'action': 'store_true',
        'help': 'Search on Google',
    },
    ('-a','--add-sites'):
    {
        'type': str,
        'nargs': 1,
        'help': 'Search different websites, this will not include stack overflow unless specified.',
        'metavar': 'url[,url,...]',
    },
}


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description='how')
    for op, kwargs in ARGS.items():
        parser.add_argument(*op, **kwargs)
    
    args_parsed = vars(parser.parse_args())
    
    query = args_parsed.get('query', [])
    n = args_parsed.get('n', 5)
    g = args_parsed.get('google',False)
    sites = args_parsed.get('add_sites')

    #Process Sites
    if sites and len(sites)>0:
        sites = list(filter(lambda s: s != '',sites[0].split(',')))

    return {
        'query': query,
        'n': n,
        'g': g,
        'sites': sites,
    }


def display_results(res: list,header:str = None) -> None:
    if header:
        print(u'\033[4m' + "Results from {0}".format(header) + u'\033[0m')
    for r in res:
        print(u'\u279c' + '\r\t', end='')
        print(r)
