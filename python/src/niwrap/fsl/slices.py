# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SLICES_METADATA = Metadata(
    id="73d5a02e6472d952aeae112091415b456c22f364",
    name="slices",
)


class SlicesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slices(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def slices(
    primary_input: InputPathType,
    secondary_input: InputPathType | None = None,
    scale_factor: float | int | None = None,
    intensity_range: list[float | int] = None,
    output_gif: str | None = None,
    runner: Runner = None,
) -> SlicesOutputs:
    """
    slices by Unknown.
    
    Generate a set of slices from an image, possibly with some scaling and
    intensity range options, and save as a GIF.
    
    Args:
        primary_input: Primary input image file (e.g. img1.nii.gz).
        secondary_input: Secondary input image file (e.g. img2.nii.gz).
        scale_factor: Scale factor to apply to images.
        intensity_range: Intensity range to consider (minimum and maximum\
            values).
        output_gif: Output GIF file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SlicesOutputs`).
    """
    runner = runner or get_global_runner()
    if intensity_range is not None and (len(intensity_range) != 2): 
        raise ValueError(f"Length of 'intensity_range' must be 2 but was {len(intensity_range)}")
    execution = runner.start_execution(SLICES_METADATA)
    cargs = []
    cargs.append("slices")
    cargs.append(execution.input_file(primary_input))
    if secondary_input is not None:
        cargs.append(execution.input_file(secondary_input))
    cargs.append("-s")
    if scale_factor is not None:
        cargs.extend(["-s", str(scale_factor)])
    cargs.append("-i")
    cargs.append("[INTMIN]")
    cargs.append("[INTMAX]")
    cargs.append("-o")
    if output_gif is not None:
        cargs.extend(["-o", output_gif])
    ret = SlicesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICES_METADATA",
    "SlicesOutputs",
    "slices",
]
