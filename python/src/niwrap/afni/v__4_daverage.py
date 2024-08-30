# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__4_DAVERAGE_METADATA = Metadata(
    id="3a01b98e94b0362957a63ac3f5a3eee9eb2f39c4",
    name="@4Daverage",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V4DaverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__4_daverage(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__4_daverage(
    output_prefix: str,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> V4DaverageOutputs:
    """
    @4Daverage by AFNI Team.
    
    Script for computing average 3D+time bricks using 3Dcalc.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@4Daverage.html
    
    Args:
        output_prefix: Prefix for the output 3D+t brick.
        input_files: List of 3D+t brick filenames to be averaged (e.g.,\
            brick1+orig, brick2+orig). Can use wildcards.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V4DaverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__4_DAVERAGE_METADATA)
    cargs = []
    cargs.append("@4Daverage")
    cargs.append(output_prefix)
    cargs.append("[INPUT_FILES...]")
    ret = V4DaverageOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V4DaverageOutputs",
    "V__4_DAVERAGE_METADATA",
    "v__4_daverage",
]