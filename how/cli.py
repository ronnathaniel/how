
import sys
import argparse
import colorama

colorama.init(wrap=False)
stream_err = colorama.AnsiToWin32(sys.stderr).stream

ARGS = {
    'query': {
        'type': str,
        'metavar': 'QUERY',
        'nargs': '+',
        'help': 'Query to Search',
    },
    '-n': {
        'type': int,
        'metavar': 'n',
        'nargs': '?',
        'help': 'Query to Search',
        'default': 5,
    },
}


def parse_args() -> dict:
    parser = argparse.ArgumentParser(description='how')
    for op, kwargs in ARGS.items():
        parser.add_argument(op, **kwargs)
    args_parsed = vars(parser.parse_args())
    query = args_parsed.get('query', [])
    n = args_parsed.get('n', 5)
    return {
        'query': query,
        'n': n,
    }


def display_results(res: list) -> None:
    for r in res:
        print(u'\u279c' + '\r\t', end='')
        print(r)
