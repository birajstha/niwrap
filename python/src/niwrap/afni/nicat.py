# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

NICAT_METADATA = Metadata(
    id="150f64c79ef2ef5b2c3f9c0b00bdeb1447c981cd.boutiques",
    name="nicat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class NicatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nicat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def nicat(
    stream_spec: str,
    reopen: str | None = None,
    copy_stream: bool = False,
    read_only: bool = False,
    runner: Runner | None = None,
) -> NicatOutputs:
    """
    Copies stdin to the NIML stream, which will be opened for writing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        stream_spec: Stream specification (e.g., tcp:localhost:4444).
        reopen: Reopen the stream after connection to the stream specified by\
            the given value.
        copy_stream: Copy the stream to stdout instead; the 'streamspec' will\
            be opened for reading.
        read_only: Read the stream but don't copy to stdout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NicatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NICAT_METADATA)
    cargs = []
    cargs.append("nicat")
    cargs.append(stream_spec)
    if reopen is not None:
        cargs.extend([
            "-reopen",
            reopen
        ])
    if copy_stream:
        cargs.append("-r")
    if read_only:
        cargs.append("-R")
    ret = NicatOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NICAT_METADATA",
    "NicatOutputs",
    "nicat",
]
