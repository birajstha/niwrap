# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

UNPACKMINCDIR_METADATA = Metadata(
    id="665926cbe3f5b98854ac7511f567b75246bc682e.boutiques",
    name="unpackmincdir",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class UnpackmincdirOutputs(typing.NamedTuple):
    """
    Output object returned when calling `unpackmincdir(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def unpackmincdir(
    source_directory: str,
    target_directory: str,
    scan_sequence_info: str | None = None,
    functional_sequence: str | None = None,
    functional_subdirectory: str | None = None,
    minc_only: bool = False,
    no_copy: bool = False,
    umask: str | None = None,
    runner: Runner | None = None,
) -> UnpackmincdirOutputs:
    """
    Tool for unpacking directories with MINC files.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        source_directory: Source directory containing the MINC files.
        target_directory: Target directory to unpack the contents to.
        scan_sequence_info: Scan sequence directives file, e.g.,\
            freesurfer_alpha/scanseq.info.
        functional_sequence: Use seqname for functionals (example:\
            ep2d_fid_ts_20b2604).
        functional_subdirectory: Functional subdirectory, e.g., bold.
        minc_only: Do not unpack into bshorts.
        no_copy: Create directories but do not copy/convert data.
        umask: Unix file permission mask (default: 22).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnpackmincdirOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UNPACKMINCDIR_METADATA)
    cargs = []
    cargs.append("unpackmincdir")
    cargs.extend([
        "-src",
        source_directory
    ])
    cargs.extend([
        "-targ",
        target_directory
    ])
    if scan_sequence_info is not None:
        cargs.extend([
            "-scanseqinfo",
            scan_sequence_info
        ])
    if functional_sequence is not None:
        cargs.extend([
            "-funcseq",
            functional_sequence
        ])
    if functional_subdirectory is not None:
        cargs.extend([
            "-fsd",
            functional_subdirectory
        ])
    if minc_only:
        cargs.append("-minconly")
    if no_copy:
        cargs.append("-nocopy")
    if umask is not None:
        cargs.extend([
            "-umask",
            umask
        ])
    ret = UnpackmincdirOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UNPACKMINCDIR_METADATA",
    "UnpackmincdirOutputs",
    "unpackmincdir",
]
