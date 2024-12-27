import argparse
import sys


def main() -> int:
    """
    Pipeline entry point.
    """
    args = parse_args()

    return 0


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    cmd Arguments
    -------------
    msin: str
        input MeasurementSet v2 directory.

    msout: str
        output MeasurementSet v2 name & directory.

    range: float
        range of snapshot indices to be extracted
        as an output MeasurementSet v2.
    """
    parser = argparse.ArgumentParser(
        description="Break MeasurementSet v2 by snapshots",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "msin",
        type=str,
        help="input MeasurementSet v2 directory"
    )
    parser.add_argument(
        "msout",
        type=str,
        help="output MeasurementSet v2 name & directory"
    )
    parser.add_argument(
        "range",
        type=int,
        nargs=2,
        help="output MeasurementSet v2 name & directory"
    )

    return parser.parse_args()


if __name__ == "__main__":
    sys.exit(main())