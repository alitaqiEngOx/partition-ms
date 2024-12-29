from pathlib import Path

from casacore.tables import table, tableutil


def break_by_snapshots(
        msin_dir: Path, msout_dir: Path, filter: list[int]
) -> None:
    """
    """
    tableutil.tablecopy(f"{msin_dir}", f"{msout_dir}", copynorows=True)
    msin = table(f"{msin_dir}", ack=False)
    msout = table(f"{msout_dir}", ack=False, readonly=False)
    msout.addrows(filter[1]-filter[0])

    for colname in msin.colnames():
        try:
            coldata = msin.getcol(colname)

        except:
            print(f"skipping={colname}")
            continue

        msout.putcol(colname, coldata[filter[0]:filter[1]])
        print(f"copied={colname}")

    msin.close()
    msout.close()