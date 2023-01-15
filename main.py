#!/usr/bin/env python3

from docopt import docopt
from tracert import Tracer


def main():
    usage = """
    Usage: main.py [-m <hops>] <destination>
           main.py --help

    Arguments:
      destination                   Destination host to probe

    Options:
      -m <hops>, --max-hops <hops>  Max number of hops to probe
                                    [default: 30]
      -h, --help                    Display this usage info
    """

    args = docopt(usage)
    tracer = Tracer(
        dst=args['<destination>'],
        hops=int(args['--max-hops'])
    )

    tracer.run()

if __name__ == '__main__':
    main()
