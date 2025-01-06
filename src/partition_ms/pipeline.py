from logging import Logger
from pathlib import Path

from casacore.tables import table


def break_by_snapshots(
        msin_dir: Path, msout_dir: Path, filter: list[int],
        *, logger: Logger
) -> None:
    """
    """
    msin = table(f"{msin_dir}", ack=False)
    msin.copy(f"{msout_dir}", deep=True, copynorows=True)
    tblnames = ["MAIN"] + [
        tbl.name for tbl in msout_dir.iterdir() if tbl.is_dir()
    ]

    for tblname in tblnames:
        logger.info(f"   Copying {tblname} table...")

        if tblname == "MAIN":
            logger.info(f"   Only rows {filter[0]}-{filter[1]} out of {msin.nrows()}\n  |")

            msout = table(f"{msout_dir}", ack=False, readonly=False)
            msout.addrows(filter[1]-filter[0])

        else:
            msin = table(f"{msin_dir.joinpath(tblname)}", ack=False)
            msout = table(f"{msout_dir.joinpath(tblname)}", ack=False, readonly=False)
            msout.addrows(msin.nrows())

        for colname in msin.colnames():
            if tblname != "MAIN":
                logger.info(f"   All {msin.nrows()} row(s)\n  |")
            try:
                coldata = msin.getcol(colname)
            except Exception as e:
                logger.warning(f"Error in copying {colname} column, skipping")
                continue

            if tblname == "MAIN":
                msout.putcol(colname, coldata[filter[0]:filter[1]])
            else:
                msout.putcol(colname, coldata)

            if colname == msin.colnames()[-1]:
                logger.info(f"   Copied {colname} column\n  |")
            else:
                logger.info(f"   Copied {colname} column")

        msin.close()
        msout.close()