# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_SKELETON_METADATA = Metadata(
    id="964224a75752deee356a86c05d66f7f00a1b912b.boutiques",
    name="afni_skeleton",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniSkeletonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_skeleton(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def afni_skeleton(
    infiles: list[InputPathType] | None = None,
    help_: bool = False,
    hist: bool = False,
    ver: bool = False,
    runner: Runner | None = None,
) -> AfniSkeletonOutputs:
    """
    Skeleton of a basic python program example.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/afni_skeleton.py.html
    
    Args:
        infiles: Specify input files.
        help_: Show help message.
        hist: Show the revision history.
        ver: Show the version number.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniSkeletonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_SKELETON_METADATA)
    cargs = []
    cargs.append("afni_skeleton.py")
    if infiles is not None:
        cargs.extend([execution.input_file(f) for f in infiles])
    if help_:
        cargs.append("-help")
    if hist:
        cargs.append("-hist")
    if ver:
        cargs.append("-ver")
    ret = AfniSkeletonOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_SKELETON_METADATA",
    "AfniSkeletonOutputs",
    "afni_skeleton",
]