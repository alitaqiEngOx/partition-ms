from logging import Logger
from pathlib import Path

from casacore.tables import table, tableutil


def break_by_snapshots(
        msin_dir: Path, msout_dir: Path, filter: list[int],
        *, logger: Logger
) -> None:
    """
    """
    #tableutil.tablecopy(f"{msin_dir}", f"{msout_dir}", copynorows=True)

    # main table
    #print("MAIN.....")
    msin = table(f"{msin_dir}", ack=False)
    msin.copy(f"{msout_dir}", deep=True, copynorows=True)

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

    for tblname in [
        "ANTENNA", "DATA_DESCRIPTION", "DOPPLER", "FEED", 
        "FIELD", "FLAG_CMD", "FREQ_OFFSET", "HISTORY", 
        "OBSERVATION", "POINTING", "PLOARIZATION", 
        "PROCESSOR", "SOURCE", "SPECTRAL_WINDOW", 
        "STATE", "SYSCAL", "WEATHER"
    ]:
        if msout_dir.joinpath(tblname).exists():
            print(f"{tblname}.....")
            msin = table(f"{msin_dir.joinpath(tblname)}", ack=False)
            msout = table(f"{msout_dir.joinpath(tblname)}", ack=False, readonly=False)
            msout.addrows(msin.nrows())

            for colname in msin.colnames():
                try:
                    coldata = msin.getcol(colname)

                except:
                    print(f"skipping={colname}")
                    continue

                msout.putcol(colname, coldata)
                print(f"copied={colname}")

            msin.close()
            msout.close()

        else:
            print(f"Table {tblname} does not exist - skipping")
            continue
