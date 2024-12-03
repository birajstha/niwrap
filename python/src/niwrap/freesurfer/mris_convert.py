# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_CONVERT_METADATA = Metadata(
    id="2935cffb17b5edbbc239ffbc0efa59b1c070ffca.boutiques",
    name="mris_convert",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    converted_surface: OutputPathType
    """Output converted surface file"""


def mris_convert(
    input_file: InputPathType,
    output_file: str,
    second_input_file: InputPathType | None = None,
    patch: bool = False,
    curv_overlay_files: list[str] | None = None,
    functional_data_file: InputPathType | None = None,
    orig_positions: str | None = None,
    scale: float | None = None,
    rescale: bool = False,
    talairach_xfm: str | None = None,
    normals: bool = False,
    neighbors: bool = False,
    xyz: bool = False,
    annotation_file: InputPathType | None = None,
    parcstats_file: InputPathType | None = None,
    gifti_dataarray_num: float | None = None,
    label_file: InputPathType | None = None,
    label_stats_file: str | None = None,
    combine_surfs: bool = False,
    merge_gifti: bool = False,
    split_gifti: bool = False,
    gifti_outdir: str | None = None,
    delete_cmds: bool = False,
    center: bool = False,
    vol_geom: str | None = None,
    remove_vol_geom: bool = False,
    to_surf: str | None = None,
    to_scanner: bool = False,
    to_tkr: bool = False,
    userealras: bool = False,
    usesurfras: bool = False,
    upsample: str | None = None,
    volume: str | None = None,
    area: str | None = None,
    angle: str | None = None,
    label_to_mask: str | None = None,
    cras_add: bool = False,
    cras_subtract: bool = False,
    runner: Runner | None = None,
) -> MrisConvertOutputs:
    """
    This program will convert MRI-surface data formats.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input filename.
        output_file: Output filename.
        second_input_file: Second input filename to be combined, required for\
            --combinesurfs.
        patch: Input file is a patch file, not a full surface.
        curv_overlay_files: Input scalar curv overlay files.
        functional_data_file: Input functional time-series or other multi-frame\
            data.
        orig_positions: Read orig positions.
        scale: Scale vertex xyz by scale.
        rescale: Rescale vertex xyz so total area is same as group average.
        talairach_xfm: Apply talairach xfm of subject to vertex xyz.
        normals: Output ascii file where vertex data is the surface normal\
            vector.
        neighbors: Write out neighbors of a vertex in each row.
        xyz: Print only surface xyz to ascii file.
        annotation_file: Input annotation or gifti label data.
        parcstats_file: Input text file containing label/val pairs for\
            parcellation.
        gifti_dataarray_num: Input gifti dataarray number to use.
        label_file: Input .label file and name for this label.
        label_stats_file: Output gifti file to which label stats will be\
            written.
        combine_surfs: Combine surface files, two input surface files required.
        merge_gifti: Generate combined gifti file with surface and multiple\
            curvature data.
        split_gifti: Separate surface and data array from combined gifti file.
        gifti_outdir: Output directory for generated gifti files.
        delete_cmds: Delete command lines in surface.
        center: Put center of surface at (0,0,0).
        vol_geom: Use MRIVol to set the volume geometry.
        remove_vol_geom: Set the valid flag in vg to 0.
        to_surf: Copy coordinates from surfcoords to output (good for patches).
        to_scanner: Convert coordinates from native FS (tkr) coords to scanner\
            coords.
        to_tkr: Convert coordinates from scanner coords to native FS (tkr)\
            coords.
        userealras: Same as --to-scanner.
        usesurfras: Same as --to-tkr.
        upsample: Upsample N times by splitting edges/faces.
        volume: Compute vertex-wise volume.
        area: Compute vertex-wise area.
        angle: Compute cortical orientation angles.
        label_to_mask: Convert a surface-based label to a binary mask.
        cras_add: Shift center to scanner coordinate center.
        cras_subtract: Shift center from scanner coordinate center.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_CONVERT_METADATA)
    cargs = []
    cargs.append("mris_convert")
    cargs.append(execution.input_file(input_file))
    if second_input_file is not None:
        cargs.append(execution.input_file(second_input_file))
    cargs.append(output_file)
    if patch:
        cargs.append("-p")
    if curv_overlay_files is not None:
        cargs.extend([
            "-c",
            *curv_overlay_files
        ])
    if functional_data_file is not None:
        cargs.extend([
            "-f",
            execution.input_file(functional_data_file)
        ])
    if orig_positions is not None:
        cargs.extend([
            "-o",
            orig_positions
        ])
    if scale is not None:
        cargs.extend([
            "-s",
            str(scale)
        ])
    if rescale:
        cargs.append("-r")
    if talairach_xfm is not None:
        cargs.extend([
            "-t",
            talairach_xfm
        ])
    if normals:
        cargs.append("-n")
    if neighbors:
        cargs.append("-v")
    if xyz:
        cargs.append("-a")
    if annotation_file is not None:
        cargs.extend([
            "--annot",
            execution.input_file(annotation_file)
        ])
    if parcstats_file is not None:
        cargs.extend([
            "--parcstats",
            execution.input_file(parcstats_file)
        ])
    if gifti_dataarray_num is not None:
        cargs.extend([
            "--da_num",
            str(gifti_dataarray_num)
        ])
    if label_file is not None:
        cargs.extend([
            "--label",
            execution.input_file(label_file)
        ])
    if label_stats_file is not None:
        cargs.extend([
            "--labelstats",
            label_stats_file
        ])
    if combine_surfs:
        cargs.append("--combinesurfs")
    if merge_gifti:
        cargs.append("--mergegifti")
    if split_gifti:
        cargs.append("--splitgifti")
    if gifti_outdir is not None:
        cargs.extend([
            "--giftioutdir",
            gifti_outdir
        ])
    if delete_cmds:
        cargs.append("--delete-cmds")
    if center:
        cargs.append("--center")
    if vol_geom is not None:
        cargs.extend([
            "--vol-geom",
            vol_geom
        ])
    if remove_vol_geom:
        cargs.append("--remove-vol-geom")
    if to_surf is not None:
        cargs.extend([
            "--to-surf",
            to_surf
        ])
    if to_scanner:
        cargs.append("--to-scanner")
    if to_tkr:
        cargs.append("--to-tkr")
    if userealras:
        cargs.append("--userealras")
    if usesurfras:
        cargs.append("--usesurfras")
    if upsample is not None:
        cargs.extend([
            "--upsample",
            upsample
        ])
    if volume is not None:
        cargs.extend([
            "--volume",
            volume
        ])
    if area is not None:
        cargs.extend([
            "--area",
            area
        ])
    if angle is not None:
        cargs.extend([
            "--angle",
            angle
        ])
    if label_to_mask is not None:
        cargs.extend([
            "--label2mask",
            label_to_mask
        ])
    if cras_add:
        cargs.append("--cras_add")
    if cras_subtract:
        cargs.append("--cras_subtract")
    ret = MrisConvertOutputs(
        root=execution.output_file("."),
        converted_surface=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_CONVERT_METADATA",
    "MrisConvertOutputs",
    "mris_convert",
]