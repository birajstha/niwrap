# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_MASK_METADATA = Metadata(
    id="c88d984dd58588f37c7a7cb282d5f5381d82b1e6.boutiques",
    name="mri_mask",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output volume file"""


def mri_mask(
    input_volume: InputPathType,
    mask_volume: InputPathType,
    output_volume: str,
    xform: str | None = None,
    lta_src: str | None = None,
    lta_dst: str | None = None,
    threshold: float | None = None,
    npad: float | None = None,
    npad_vector: list[float] | None = None,
    npad_multi_vector: list[float] | None = None,
    abs_: bool = False,
    invert: bool = False,
    no_invert: bool = False,
    rh_labels: bool = False,
    lh_labels: bool = False,
    dilate: float | None = None,
    no_cerebellum: bool = False,
    oval_value: float | None = None,
    transfer_value: float | None = None,
    keep_mask_deletion_edits: bool = False,
    samseg: bool = False,
    runner: Runner | None = None,
) -> MriMaskOutputs:
    """
    Applies a mask volume (typically skull stripped).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume file.
        mask_volume: Mask volume file.
        output_volume: Output volume file.
        xform: Apply M3Z/LTA to transform mask to the space of input volume\
            (identity.nofile possible, will invert if needed).
        lta_src: Source volume for -xform (if not available from the xform\
            file).
        lta_dst: Destination volume for -xform (if not available from the xform\
            file).
        threshold: Threshold mask volume at a given threshold (values <=\
            threshold considered zero).
        npad: Create a bounding box around the mask expanded by npad voxels in\
            each direction.
        npad_vector: Create a bounding box around the mask expanded by npad1\
            npad2 npad3 voxels in each direction.
        npad_multi_vector: Create a bounding box around the mask, expanded by\
            npad1a npad1b npad2a npad2b npad3a npad3b in each direction.
        abs_: Take absolute value before applying threshold.
        invert: Invert mask.
        no_invert: Turn off inversion of mask.
        rh_labels: Set mask in right hemisphere labels to 1 (assumes input mask\
            is an aseg).
        lh_labels: Set mask in left hemisphere labels to 1 (assumes input mask\
            is an aseg).
        dilate: Dilate mask N times before applying.
        no_cerebellum: Remove cerebellum from aseg mask (assumes input mask is\
            an aseg).
        oval_value: Use specified oval value as output instead of 0.
        transfer_value: Transfer only the specified voxel value from mask to\
            output.
        keep_mask_deletion_edits: Transfer voxel-deletion edits (voxels=1) from\
            mask to output volume.
        samseg: Assume mask is a SAMSEG segmentation and mask all non-brain\
            labels.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriMaskOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_MASK_METADATA)
    cargs = []
    cargs.append("mri_mask")
    cargs.append(execution.input_file(input_volume))
    cargs.append(execution.input_file(mask_volume))
    cargs.append(output_volume)
    if xform is not None:
        cargs.extend([
            "-xform",
            xform
        ])
    if lta_src is not None:
        cargs.extend([
            "-lta_src",
            lta_src
        ])
    if lta_dst is not None:
        cargs.extend([
            "-lta_dst",
            lta_dst
        ])
    if threshold is not None:
        cargs.extend([
            "-T",
            str(threshold)
        ])
    if npad is not None:
        cargs.extend([
            "-bb",
            str(npad)
        ])
    if npad_vector is not None:
        cargs.extend([
            "-bbm",
            *map(str, npad_vector)
        ])
    if npad_multi_vector is not None:
        cargs.extend([
            "-bbmm",
            *map(str, npad_multi_vector)
        ])
    if abs_:
        cargs.append("-abs")
    if invert:
        cargs.append("-invert")
    if no_invert:
        cargs.append("-no-invert")
    if rh_labels:
        cargs.append("-rh")
    if lh_labels:
        cargs.append("-lh")
    if dilate is not None:
        cargs.extend([
            "-dilate",
            str(dilate)
        ])
    if no_cerebellum:
        cargs.append("-no_cerebellum")
    if oval_value is not None:
        cargs.extend([
            "-oval",
            str(oval_value)
        ])
    if transfer_value is not None:
        cargs.extend([
            "-transfer",
            str(transfer_value)
        ])
    if keep_mask_deletion_edits:
        cargs.append("-keep_mask_deletion_edits")
    if samseg:
        cargs.append("-samseg")
    ret = MriMaskOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(output_volume),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_MASK_METADATA",
    "MriMaskOutputs",
    "mri_mask",
]