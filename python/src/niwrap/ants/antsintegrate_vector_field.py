# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTSINTEGRATE_VECTOR_FIELD_METADATA = Metadata(
    id="25eaf01e25105beba3ae7eb2187714401340f8d4.boutiques",
    name="ANTSIntegrateVectorField",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsintegrateVectorFieldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `antsintegrate_vector_field(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fibers_out_vtk: OutputPathType
    """The output is the fibers as a VTK text file."""
    length_image_out_nii: OutputPathType
    """The output is the length image."""


def antsintegrate_vector_field(
    vector_field_input: InputPathType,
    roi_mask_input: InputPathType,
    fibers_output: str,
    length_image_output: str,
    runner: Runner | None = None,
) -> AntsintegrateVectorFieldOutputs:
    """
    This tool integrates a vector field, where vectors are voxels, using a region of
    interest (ROI) mask. The ROI mask controls where the integration is performed
    and specifies the starting point region.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        vector_field_input: Input vector field image (e.g., VecImageIN.nii.gz),\
            where vectors are voxels.
        roi_mask_input: Input ROI mask image (e.g., ROIMaskIN.nii.gz), an\
            integer image controlling where the integration is performed.
        fibers_output: Output VTK text file for fibers (e.g., FibersOUT.vtk).
        length_image_output: Output length image (e.g., LengthImageOUT.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsintegrateVectorFieldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTSINTEGRATE_VECTOR_FIELD_METADATA)
    cargs = []
    cargs.append("ANTSIntegrateVectorField")
    cargs.append(execution.input_file(vector_field_input))
    cargs.append(execution.input_file(roi_mask_input))
    cargs.append(fibers_output)
    cargs.append(length_image_output)
    ret = AntsintegrateVectorFieldOutputs(
        root=execution.output_file("."),
        fibers_out_vtk=execution.output_file(fibers_output),
        length_image_out_nii=execution.output_file(length_image_output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTSINTEGRATE_VECTOR_FIELD_METADATA",
    "AntsintegrateVectorFieldOutputs",
    "antsintegrate_vector_field",
]
