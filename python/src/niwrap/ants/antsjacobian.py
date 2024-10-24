# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTSJACOBIAN_METADATA = Metadata(
    id="4c1495ce17166625b172b3fbe727bd30b17f079f.boutiques",
    name="ANTSJacobian",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsjacobianOutputs(typing.NamedTuple):
    """
    Output object returned when calling `antsjacobian(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    jacobian_output: OutputPathType
    """Output file containing the Jacobian determinant information."""


def antsjacobian(
    imagedim: int,
    gwarp: InputPathType,
    outfile: str,
    uselog: int,
    maskfn: InputPathType,
    normbytotalbool: int,
    projectionvector: str | None = None,
    runner: Runner | None = None,
) -> AntsjacobianOutputs:
    """
    Calculate the Jacobian determinant of a transformation using ANTs. WARNING:
    ANTSJacobian may not be working correctly; see CreateJacobianDeterminantImage
    for an alternative method.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        imagedim: The dimensionality of the input image.
        gwarp: The input warp image.
        outfile: The prefix for the output files.
        uselog: Whether to use logarithm in computation.
        maskfn: Mask file used in the computation.
        normbytotalbool: Normalize the Jacobian by the total in the mask. Use\
            this to adjust for head size.
        projectionvector: Projects the warp along the specified direction. Do\
            not add this option if no projection is desired.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsjacobianOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTSJACOBIAN_METADATA)
    cargs = []
    cargs.append("ANTSJacobian")
    cargs.append(str(imagedim))
    cargs.append(execution.input_file(gwarp))
    cargs.append(outfile)
    cargs.append(str(uselog))
    cargs.append(execution.input_file(maskfn))
    cargs.append(str(normbytotalbool))
    if projectionvector is not None:
        cargs.append(projectionvector)
    ret = AntsjacobianOutputs(
        root=execution.output_file("."),
        jacobian_output=execution.output_file(outfile + "Jacobian.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTSJACOBIAN_METADATA",
    "AntsjacobianOutputs",
    "antsjacobian",
]
