# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

AFF2RIGID_METADATA = Metadata(
    id="ef756e973bf00d7b0acb122e2c4bffc01ce55350",
    name="aff2rigid",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Aff2rigidOutputs(typing.NamedTuple):
    """
    Output object returned when calling `aff2rigid(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def aff2rigid(
    input_transform: InputPathType,
    output_transform: str,
    runner: Runner = None,
) -> Aff2rigidOutputs:
    """
    aff2rigid by FMRIB, University of Oxford.
    
    Tool for converting affine transformations to rigid transformations.
    
    Args:
        input_transform: Input FLIRT transform (12 DOF) from the input image to
            standard space.
        output_transform: Output matrix which will convert the input image to
            standard space using a 6 DOF transformation.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Aff2rigidOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFF2RIGID_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/aff2rigid")
    cargs.append(execution.input_file(input_transform))
    cargs.append(output_transform)
    ret = Aff2rigidOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFF2RIGID_METADATA",
    "Aff2rigidOutputs",
    "aff2rigid",
]
