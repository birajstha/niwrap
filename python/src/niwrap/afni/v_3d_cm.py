# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_CM_METADATA = Metadata(
    id="298738935051c7b797c79b458694e4be34654252",
    name="3dCM",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dCmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_cm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    center_of_mass: OutputPathType
    """Center of mass of the dataset."""


def v_3d_cm(
    dset: InputPathType,
    mask: InputPathType | None = None,
    automask: bool = False,
    set_origin: list[float | int] | None = None,
    local_ijk: bool = False,
    roi_vals: list[float | int] | None = None,
    all_rois: bool = False,
    icent: bool = False,
    dcent: bool = False,
    runner: Runner | None = None,
) -> V3dCmOutputs:
    """
    3dCM by AFNI Team.
    
    Tool for computing the center of mass of a dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dCM.html
    
    Args:
        dset: Input dataset.
        mask: Use the specified dataset as a mask. Only voxels with nonzero\
            values in 'mset' will be averaged from 'dataset'. Both datasets must\
            have the same number of voxels.
        automask: Generate the mask automatically.
        set_origin: After computing the CM of the dataset, set the origin\
            fields in the header so that the CM will be at (x,y,z) in DICOM\
            coordinates.
        local_ijk: Output values as (i,j,k) in local orientation.
        roi_vals: Compute center of mass for each blob with specified voxel\
            values.
        all_rois: Automatically find all ROI values and compute their centers\
            of mass.
        icent: Compute Internal Center, which finds the center voxel closest to\
            the center of mass.
        dcent: Compute Distance Center, the center voxel with the shortest\
            average distance to all other voxels. This is computationally\
            expensive.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dCmOutputs`).
    """
    runner = runner or get_global_runner()
    if set_origin is not None and (len(set_origin) != 3): 
        raise ValueError(f"Length of 'set_origin' must be 3 but was {len(set_origin)}")
    execution = runner.start_execution(V_3D_CM_METADATA)
    cargs = []
    cargs.append("3dCM")
    cargs.append("[OPTIONS]")
    cargs.append(execution.input_file(dset))
    ret = V3dCmOutputs(
        root=execution.output_file("."),
        center_of_mass=execution.output_file(f"<stdout>"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dCmOutputs",
    "V_3D_CM_METADATA",
    "v_3d_cm",
]