# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


VOLUME_SET_SPACE_METADATA = Metadata(
    id="25dcf2dbd44a1b701ee34698bbce94028b54e59f",
    name="volume-set-space",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeSetSpaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_set_space(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_set_space(
    runner: Runner,
    volume_in: InputPathType,
    volume_out: str,
    opt_file_volume_ref: str | None = None,
) -> VolumeSetSpaceOutputs:
    """
    CHANGE VOLUME SPACE INFORMATION.
    
    Writes a copy of the volume file, with the spacing information changed as
    specified. No reordering of the voxel data occurs, see -volume-reorient to
    change the volume indexing order and reorder the voxels to match. Exactly
    one of -plumb, -sform, or -file must be specified.
    
    Args:
        runner: Command runner
        volume_in: the input volume
        volume_out: output - the output volume
        opt_file_volume_ref: copy spacing info from volume file with matching
            dimensions: volume file to use for reference space
    Returns:
        NamedTuple of outputs (described in `VolumeSetSpaceOutputs`).
    """
    execution = runner.start_execution(VOLUME_SET_SPACE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-set-space")
    cargs.append(execution.input_file(volume_in))
    cargs.append(volume_out)
    if opt_file_volume_ref is not None:
        cargs.extend(["-file", opt_file_volume_ref])
    ret = VolumeSetSpaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret
