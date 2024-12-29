import argparse
import sys
from pathlib import Path

from partition_ms.pipeline import break_by_snapshots
from partition_ms.utils import log_handler


def main() -> int:
    """
    Pipeline entry point.
    """
    args = parse_args()
    logger = log_handler.generate(
        "Partition MS", cmd_logs=args.cmd_logs
    )

    break_by_snapshots(
        Path(args.msin), Path(args.msout), args.range
    )

    return 0


def parse_args() -> argparse.Namespace:
    """
    Parses command line arguments.

    cmd Arguments
    -------------
    --cmd_logs (optional): None
      raising this flag will prompt the pipeline to output
      logs on the command line in addition to logging into a
      logfile.

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
        "--cmd_logs",
        action="store_true",
        help="Generates detailed logs on the command line"
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