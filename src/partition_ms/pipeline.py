from logging import Logger
from pathlib import Path

from casacore.tables import table


def break_by_snapshots(
        msin_dir: Path, msout_dir: Path, filter: list[int],
        *, logger: Logger
) -> None:
    """
    """
    # main table
    print("MAIN.....")
    msin = table(f"{msin_dir}", ack=False)
    msin.copy(f"{msout_dir}", deep=True, copynorows=True)

    msout = table(f"{msout_dir}", ack=False, readonly=False)
    msout.addrows(filter[1]-filter[0])

    for colname in msin.colnames():
        try:
            coldata = msin.getcol(colname)

        except Exception as e:
            print(f"skipping={colname}: {e}")
            continue

        msout.putcol(colname, coldata[filter[0]:filter[1]])
        print(f"copied={colname}")

    msin.close()
    msout.close()

    # all other tables
    tblnames = [
        tbl.name for tbl in msout_dir.iterdir() if tbl.is_dir()
    ]

    for tblname in tblnames:
        print(f"\n{tblname}.....")
        msin = table(f"{msin_dir.joinpath(tblname)}", ack=False)
        msout = table(f"{msout_dir.joinpath(tblname)}", ack=False, readonly=False)
        msout.addrows(msin.nrows())

        for colname in msin.colnames():
            try:
                coldata = msin.getcol(colname)

            except Exception as e:
                print(f"skipping={colname}: {e}")
                continue

            msout.putcol(colname, coldata)
            print(f"copied={colname}")

        msin.close()
        msout.close()