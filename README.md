# Partition MS
Truncate a radio astronomy MeasurementSet v2 down to the required number of snapshots.<br />
This project is under active development.

## Installation
1- Clone this repository;<br />
2- activate a clean virtual python environment, with `python 3.11` (e.g., using `conda`);<br />
3- install `poetry`:
```
$ pip3 install poetry
```
4- navigate to the parent directory of your copy of this repository;<br />
5- install the package using `poetry`:
```
$ poetry install
```

## Usage
Once installed, the general usage is as follows:
```
$ break-by-snapshots [--cmd_logs] {msin} {msout} {start_row} {finish_row}
```
`msin` = your input MeasurementSet v2 directory;<br />
`msout` = directory and name for your truncated MeasurementSet v2 output;<br />
`start_row` = index of the first snapshot row to be copied over;<br />
`finish_row` = index of the snapshot row after the final one to be copied over.

`--cmd_logs`: raise this optional flag to stream logs on the command line in addition to the default `logfile.log` to be generated.
