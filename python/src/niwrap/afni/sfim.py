# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SFIM_METADATA = Metadata(
    id="7d907353bfcbd4bba5e790eccb3031aedcc7f45b",
    name="sfim",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SfimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sfim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Output image file for interval 'i' with task state name."""


def sfim(
    input_images: list[InputPathType],
    sfint_file: str | None = None,
    baseline_state: str | None = None,
    local_base_option: bool = False,
    output_prefix: str | None = None,
    runner: Runner | None = None,
) -> SfimOutputs:
    """
    sfim by AFNI Team.
    
    Stepwise Functional IMages.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/sfim.html
    
    Args:
        input_images: Input image files in formats accepted by AFNI.
        sfint_file: Filename which contains the interval definitions. Default\
            is 'sfint'. Example: '3*# 5*rest 4*A 5*rest 4*B 5*rest 4*A 5*rest'.
        baseline_state: Task state name to use as the baseline. Default is\
            'rest'.
        local_base_option: Flag to indicate if each non-base task state\
            interval should have the mean of the two nearest base intervals\
            subtracted instead of the grand mean of all the base task intervals.
        output_prefix: Prefix for output image filenames for all states. The\
            i'th interval with task state name 'fred' will be written to file\
            'pname.fred.i'. Default is 'sfim'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SfimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SFIM_METADATA)
    cargs = []
    cargs.append("sfim")
    if sfint_file is not None:
        cargs.extend(["-sfint", sfint_file])
    if baseline_state is not None:
        cargs.extend(["-base", baseline_state])
    if local_base_option:
        cargs.append("-localbase")
    if output_prefix is not None:
        cargs.extend(["-prefix", output_prefix])
    cargs.append("[INPUT_FILES...]")
    ret = SfimOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(f"{output_prefix}.*.i") if output_prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SFIM_METADATA",
    "SfimOutputs",
    "sfim",
]
