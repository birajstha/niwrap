# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SIGLOSS_METADATA = Metadata(
    id="f70105ba28657c6115700f6a513062c37631da87",
    name="sigloss",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class SiglossOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sigloss(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def sigloss(
    input_b0map: InputPathType,
    output_sigloss: str,
    input_mask: InputPathType | None = None,
    echo_time: float | int | None = None,
    slice_direction: typing.Literal["x", "y", "z"] | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> SiglossOutputs:
    """
    sigloss by University of Oxford (Mark Jenkinson).
    
    Estimates signal loss from a field map (in rad/s).
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/sigloss
    
    Args:
        input_b0map: Input b0 map image filename (in rad/s).
        output_sigloss: Output signal loss image filename.
        input_mask: Input mask filename.
        echo_time: Echo time (in seconds).
        slice_direction: Slice direction (either x, y or z).
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SiglossOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIGLOSS_METADATA)
    cargs = []
    cargs.append("sigloss")
    cargs.extend(["-i", execution.input_file(input_b0map)])
    cargs.extend(["-s", output_sigloss])
    if input_mask is not None:
        cargs.extend(["-m", execution.input_file(input_mask)])
    if echo_time is not None:
        cargs.extend(["--te", str(echo_time)])
    if slice_direction is not None:
        cargs.extend(["-d", slice_direction])
    if verbose_flag:
        cargs.append("-v")
    ret = SiglossOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIGLOSS_METADATA",
    "SiglossOutputs",
    "sigloss",
]
