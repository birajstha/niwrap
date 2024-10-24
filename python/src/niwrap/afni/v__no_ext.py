# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__NO_EXT_METADATA = Metadata(
    id="c6cf8e39158c82ff94f016b9c38f20ee91c053de.boutiques",
    name="@NoExt",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VNoExtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__no_ext(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """File name with specified extensions removed"""


def v__no_ext(
    extensions: list[str] | None = None,
    runner: Runner | None = None,
) -> VNoExtOutputs:
    """
    Tool for removing specified extensions from filenames.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        extensions: Extensions to be removed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VNoExtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__NO_EXT_METADATA)
    cargs = []
    cargs.append("@NoExt")
    cargs.append("<inputfile>")
    if extensions is not None:
        cargs.extend(extensions)
    ret = VNoExtOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file("output"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VNoExtOutputs",
    "V__NO_EXT_METADATA",
    "v__no_ext",
]
