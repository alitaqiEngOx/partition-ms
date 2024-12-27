from pathlib import Path

from casacore.tables import table


def break_by_snapshots(
        msin_dir: Path, msout_dir: Path, range: list[int]
) -> None:
    """
    """
    msin = table(f"{msin_dir.absolute()}")

    for name in msin.colnames():
        try:
            col = msin.getcol(name)
        except:
            continue

    