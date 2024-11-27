# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ASEGSTATSDIFF_METADATA = Metadata(
    id="10487227e273c61c9beadcb9b38d15804d6724e3.boutiques",
    name="asegstatsdiff",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class AsegstatsdiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `asegstatsdiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    asegstats_output: OutputPathType | None
    """Output table with percent differences added."""


def asegstatsdiff(
    subject1: str,
    subject2: str,
    outdir: str | None = None,
    runner: Runner | None = None,
) -> AsegstatsdiffOutputs:
    """
    Compute and report percentage differences in aseg morphometry data between two
    subjects.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject1: The first subject to be compared.
        subject2: The second subject to be compared.
        outdir: Optionally specify a directory to write the output\
            asegstats.txt.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AsegstatsdiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ASEGSTATSDIFF_METADATA)
    cargs = []
    cargs.append("asegstatsdiff")
    cargs.append(subject1)
    if outdir is not None:
        cargs.append(subject2 + outdir)
    ret = AsegstatsdiffOutputs(
        root=execution.output_file("."),
        asegstats_output=execution.output_file(outdir + "/asegstats.txt") if (outdir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ASEGSTATSDIFF_METADATA",
    "AsegstatsdiffOutputs",
    "asegstatsdiff",
]
