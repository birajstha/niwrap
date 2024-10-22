# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_AFFINE_REGRESSION_METADATA = Metadata(
    id="e0129b9ce4df57c8c3c842837fa666878dbdcf53.boutiques",
    name="surface-affine-regression",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SurfaceAffineRegressionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_affine_regression(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def surface_affine_regression(
    source: InputPathType,
    target: InputPathType,
    affine_out: str,
    runner: Runner | None = None,
) -> SurfaceAffineRegressionOutputs:
    """
    Regress the affine transform between surfaces on the same mesh.
    
    Use linear regression to compute an affine that minimizes the sum of squares
    of the coordinate differences between the target surface and the warped
    source surface. Note that this has a bias to shrink the surface that is
    being warped. The output is written as a NIFTI 'world' matrix, see
    -convert-affine to convert it for use in other software.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        source: the surface to warp.
        target: the surface to match the coordinates of.
        affine_out: output - the output affine file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceAffineRegressionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_AFFINE_REGRESSION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-affine-regression")
    cargs.append(execution.input_file(source))
    cargs.append(execution.input_file(target))
    cargs.append(affine_out)
    ret = SurfaceAffineRegressionOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_AFFINE_REGRESSION_METADATA",
    "SurfaceAffineRegressionOutputs",
    "surface_affine_regression",
]
