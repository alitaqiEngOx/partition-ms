from pathlib import Path
from shutil import copytree

from casacore.tables import table


def break_by_snapshots(
        msin: Path, msout: Path, range: list[int]
) -> None:
    """
    """
    copytree(f"{msin}", f"{msout}")
    ms = table(f"{msout}", readonly=False)

    for name in ms.colnames():
        try:
            col = ms.getcol(name)
        except:
            continue 