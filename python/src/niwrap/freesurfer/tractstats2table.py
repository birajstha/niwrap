# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TRACTSTATS2TABLE_METADATA = Metadata(
    id="38161452219ff5617b56510006b0303c43a0164f.boutiques",
    name="tractstats2table",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class Tractstats2tableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tractstats2table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_tablefile: OutputPathType
    """The output table file."""


def tractstats2table(
    tablefile: InputPathType,
    inputs: list[str] | None = None,
    load_pathstats_from_file: InputPathType | None = None,
    overall: bool = False,
    byvoxel: bool = False,
    byvoxel_measure: typing.Literal["AD", "RD", "MD", "FA"] | None = None,
    delimiter: typing.Literal["tab", "comma", "space", "semicolon"] | None = "tab",
    transpose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> Tractstats2tableOutputs:
    """
    Converts a track overall stats file created by tracula into a table used for
    group statistics.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        tablefile: The output table file.
        inputs: Specify input stat files.
        load_pathstats_from_file: Name of the file which has the list of\
            subjects (one subject per line).
        overall: Operate on the overall path statistics.
        byvoxel: Operate on the byvoxel path statistics.
        byvoxel_measure: Specify byvoxel measure. One of [AD, RD, MD, FA].\
            Required with --byvoxel option.
        delimiter: Delimiter between measures in the table. Default is tab (alt\
            comma, space, semicolon).
        transpose: Transpose the table (default is subject in rows and\
            measures/count in cols).
        debug: Increase verbosity.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tractstats2tableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRACTSTATS2TABLE_METADATA)
    cargs = []
    cargs.append("tractstats2table")
    if inputs is not None:
        cargs.extend([
            "--inputs",
            *inputs
        ])
    if load_pathstats_from_file is not None:
        cargs.extend([
            "--load-pathstats-from-file",
            execution.input_file(load_pathstats_from_file)
        ])
    if overall:
        cargs.append("-o")
    if byvoxel:
        cargs.append("-b")
    if byvoxel_measure is not None:
        cargs.extend([
            "--byvoxel-measure",
            byvoxel_measure
        ])
    cargs.extend([
        "-t",
        execution.input_file(tablefile)
    ])
    if delimiter is not None:
        cargs.extend([
            "-d",
            delimiter
        ])
    if transpose:
        cargs.append("--transpose")
    if debug:
        cargs.append("-v")
    ret = Tractstats2tableOutputs(
        root=execution.output_file("."),
        output_tablefile=execution.output_file(pathlib.Path(tablefile).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRACTSTATS2TABLE_METADATA",
    "Tractstats2tableOutputs",
    "tractstats2table",
]
