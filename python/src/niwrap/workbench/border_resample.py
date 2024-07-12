# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BORDER_RESAMPLE_METADATA = Metadata(
    id="9d8a31ac752f478532ef0b6b981876fe20590c36",
    name="border-resample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class BorderResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_out: OutputPathType
    """the output border file"""


def border_resample(
    border_in: InputPathType,
    current_sphere: InputPathType,
    new_sphere: InputPathType,
    border_out: str,
    runner: Runner | None = None,
) -> BorderResampleOutputs:
    """
    border-resample by Washington University School of Medicin.
    
    Resample a border file to a different mesh.
    
    Resamples a border file, given two spherical surfaces that are in register.
    Only borders that have the same structure as current-sphere will be
    resampled.
    
    Args:
        border_in: the border file to resample.
        current_sphere: a sphere surface with the mesh that the metric is\
            currently on.
        new_sphere: a sphere surface that is in register with <current-sphere>\
            and has the desired output mesh.
        border_out: the output border file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BorderResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-resample")
    cargs.append(execution.input_file(border_in))
    cargs.append(execution.input_file(current_sphere))
    cargs.append(execution.input_file(new_sphere))
    cargs.append(border_out)
    ret = BorderResampleOutputs(
        root=execution.output_file("."),
        border_out=execution.output_file(f"{border_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BORDER_RESAMPLE_METADATA",
    "BorderResampleOutputs",
    "border_resample",
]
