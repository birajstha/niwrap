# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

RMSDIFF_METADATA = Metadata(
    id="804d7c3a563c7927252788ae829e1c7d9390ceba",
    name="rmsdiff",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class RmsdiffOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rmsdiff(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def rmsdiff(
    matrixfile1: InputPathType,
    matrixfile2: InputPathType,
    refvol: InputPathType,
    mask: InputPathType | None = None,
    runner: Runner = None,
) -> RmsdiffOutputs:
    """
    rmsdiff.
    
    Outputs RMS deviation between matrices (in mm).
    
    Args:
        matrixfile1: First matrix file.
        matrixfile2: Second matrix file.
        refvol: Reference volume.
        mask: Optional mask.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RmsdiffOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RMSDIFF_METADATA)
    cargs = []
    cargs.append("rmsdiff")
    cargs.append(execution.input_file(matrixfile1))
    cargs.append(execution.input_file(matrixfile2))
    cargs.append(execution.input_file(refvol))
    if mask is not None:
        cargs.append(execution.input_file(mask))
    ret = RmsdiffOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RMSDIFF_METADATA",
    "RmsdiffOutputs",
    "rmsdiff",
]
