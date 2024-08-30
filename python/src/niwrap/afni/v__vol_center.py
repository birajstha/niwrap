# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V__VOL_CENTER_METADATA = Metadata(
    id="f002ad42baa635e8ffc0f31d96d3b3410181eb68",
    name="@VolCenter",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VVolCenterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__vol_center(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__vol_center(
    dset: InputPathType,
    orient: str | None = None,
    runner: Runner | None = None,
) -> VVolCenterOutputs:
    """
    @VolCenter by AFNI Team.
    
    Tool to return the center of volume for a given dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@VolCenter.html
    
    Args:
        dset: Input volume dataset.
        orient: Output coordinate system orientation (e.g., RAI).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VVolCenterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__VOL_CENTER_METADATA)
    cargs = []
    cargs.append("@VolCenter")
    cargs.append("<-dset")
    cargs.append("DSET>")
    cargs.append("[-or")
    cargs.append("ORIENT]")
    ret = VVolCenterOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VVolCenterOutputs",
    "V__VOL_CENTER_METADATA",
    "v__vol_center",
]