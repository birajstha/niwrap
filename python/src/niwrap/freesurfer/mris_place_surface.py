# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_PLACE_SURFACE_METADATA = Metadata(
    id="e4e973bfe64ca5b7e38915757ccc306ea96b6327.boutiques",
    name="mris_place_surface",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisPlaceSurfaceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_place_surface(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_place_surface(
    output_surface: str,
    input_surface: str,
    autodetect_gray_white_stats: str,
    input_volume: str,
    surface_type_group: typing.Literal["--white", "--pial"],
    hemi_group: typing.Literal["--lh", "--rh"],
    wm_segment: str | None = None,
    out_volume: str | None = None,
    out_volume_only: str | None = None,
    restore_255: bool = False,
    segmentation: str | None = None,
    cortical_parcellation: str | None = None,
    nsmooth: float | None = None,
    smooth_after_rip: bool = False,
    max_cbv_dist: float | None = None,
    rip_label: str | None = None,
    rip_midline: bool = False,
    rip_bg: bool = False,
    rip_bg_no_annot: bool = False,
    no_rip_freeze: bool = False,
    rip_wmsa: bool = False,
    rip_lesion: bool = False,
    no_rip: bool = False,
    rip_overlay: str | None = None,
    rip_surface: str | None = None,
    rip_projection: list[float] | None = None,
    repulse_surface: str | None = None,
    white_surface: str | None = None,
    blend_surface: str | None = None,
    multimodal_input: str | None = None,
    mm_refine: bool = False,
    pin_medial_wall: str | None = None,
    no_intensity_proc: bool = False,
    debug_vertex: float | None = None,
    ripflag_out: str | None = None,
    local_max: str | None = None,
    target_surf: str | None = None,
    stop_mask: bool = False,
    mm_intensity_limits: str | None = None,
    cover_seg: str | None = None,
    first_peak_d1: bool = False,
    first_peak_d2: bool = False,
    white_border_low_factor: float | None = None,
    fill_lateral_ventricles: list[float] | None = None,
    runner: Runner | None = None,
) -> MrisPlaceSurfaceOutputs:
    """
    This program positions the triangular mesh representing a cortical surface,
    either the 'white' surface (ie, white/gray boundary) or the 'pial' surface (ie,
    the gray/csf boundary).
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_surface: Output surface.
        input_surface: Input surface.
        autodetect_gray_white_stats: Intensity stats created by\
            mris_autodet_gwstats.
        input_volume: T1-weighed intensity volume used to find white/gray/csf\
            gradients (usually brain.finalsurf.mgz).
        surface_type_group: Place the white surface or the pial surface. Must\
            choose one.
        hemi_group: Left or right hemisphere. Must choose one.
        wm_segment: White matter segmentation.
        out_volume: Save input volume after preprocessing.
        out_volume_only: Save input volume after preprocessing and then exit.
        restore_255: Set voxels in the input volume that start off as 255 to\
            110 (white surf only).
        segmentation: Whole-brain segmentation (usually aseg.presurf.mgz).
        cortical_parcellation: Set cortical parcellation used to rip vertices\
            (usually ?h.aparc.annot).
        nsmooth: Smooth input surface by number of iterations.
        smooth_after_rip: Smooth after ripping.
        max_cbv_dist: Limit distance MRIScomputeBorderValues() can search from\
            the input.
        rip_label: Do not move vertices that are NOT in the cortex label.
        rip_midline: Do not move vertices that are in the midline as indicated\
            by the seg.
        rip_bg: Do not move vertices near basal ganglia (as defined by seg).
        rip_bg_no_annot: Do not require surface have an annotation when ripping\
            BG.
        no_rip_freeze: Do NOT move vertices in/near freeze voxels (247 as\
            defined in seg).
        rip_wmsa: Do not move vertices in/near white-matter signal\
            abnormalities (77,78,79 as defined in seg).
        rip_lesion: Do not move vertices in/near lesions (25 and 57 as defined\
            in seg).
        no_rip: Turn off all ripping.
        rip_overlay: Rip vertices > 0.5 in the surface overlay file.
        rip_surface: Use this surface with ripping midline, BG, Freezes,\
            Lesions, and WMSA.
        rip_projection: Control projection depth along normal to ripsurface\
            when sampling seg.
        repulse_surface: Force input surface away from this surface (usually\
            the white surface when placing the pial).
        white_surface: Set the white{xyz} coordinates of the input surface\
            using this surface.
        blend_surface: Recompute the xyz coordinates of the input surface by\
            computing a weighted average with the blend surface.
        multimodal_input: Specify a T2 or FLAIR input volume used for placing\
            the pial surface. Must be in registration with the input volume.
        mm_refine: Use Siless' MultimodalRefinement. Sets tspring=nspring=0.3.
        pin_medial_wall: Set coordinates in vertices NOT in cortexlabel to be\
            that of the white{xyz} coordinates.
        no_intensity_proc: Do not process the input intensity volume (eg, to\
            remove parts of eye socket).
        debug_vertex: Debug vertex number.
        ripflag_out: Save ripflag as overlay.
        local_max: Save LocalMaxFoundFlag as overlay.
        target_surf: Save CBV target surface.
        stop_mask: Stop mask to stop search along normal for max gradient.
        mm_intensity_limits: Intensity limits for placing pial on multimodal\
            input.
        cover_seg: Force surface to cover the segmentation.
        first_peak_d1: Use find-first-peak option with 1st derivative in\
            ComputeBorderValues.
        first_peak_d2: Use find-first-peak option with 2nd derivative in\
            ComputeBorderValues.
        white_border_low_factor: white_border_low = f*adgws.gray_mean +\
            (1-f)*adgws.white_mean;.
        fill_lateral_ventricles: Fill lateral ventricles with 110.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisPlaceSurfaceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_PLACE_SURFACE_METADATA)
    cargs = []
    cargs.append("mris_place_surface")
    cargs.extend([
        "--o",
        output_surface
    ])
    cargs.extend([
        "--i",
        input_surface
    ])
    cargs.extend([
        "--adgw",
        autodetect_gray_white_stats
    ])
    cargs.extend([
        "--invol",
        input_volume
    ])
    cargs.append(surface_type_group)
    cargs.append(hemi_group)
    if wm_segment is not None:
        cargs.extend([
            "--wm",
            wm_segment
        ])
    if out_volume is not None:
        cargs.extend([
            "--outvol",
            out_volume
        ])
    if out_volume_only is not None:
        cargs.extend([
            "--outvol-only",
            out_volume_only
        ])
    if restore_255:
        cargs.append("--restore-255")
    if segmentation is not None:
        cargs.extend([
            "--seg",
            segmentation
        ])
    if cortical_parcellation is not None:
        cargs.extend([
            "--aparc",
            cortical_parcellation
        ])
    if nsmooth is not None:
        cargs.extend([
            "--nsmooth",
            str(nsmooth)
        ])
    if smooth_after_rip:
        cargs.append("--smooth-after-rip")
    if max_cbv_dist is not None:
        cargs.extend([
            "--max-cbv-dist",
            str(max_cbv_dist)
        ])
    if rip_label is not None:
        cargs.extend([
            "--rip-label",
            rip_label
        ])
    if rip_midline:
        cargs.append("--rip-midline")
    if rip_bg:
        cargs.append("--rip-bg")
    if rip_bg_no_annot:
        cargs.append("--rip-bg-no-annot")
    if no_rip_freeze:
        cargs.append("--no-rip-freeze")
    if rip_wmsa:
        cargs.append("--rip-wmsa")
    if rip_lesion:
        cargs.append("--rip-lesion")
    if no_rip:
        cargs.append("--no-rip")
    if rip_overlay is not None:
        cargs.extend([
            "--rip-overlay",
            rip_overlay
        ])
    if rip_surface is not None:
        cargs.extend([
            "--ripsurface",
            rip_surface
        ])
    if rip_projection is not None:
        cargs.extend([
            "--rip-projection",
            *map(str, rip_projection)
        ])
    if repulse_surface is not None:
        cargs.extend([
            "--repulse-surf",
            repulse_surface
        ])
    if white_surface is not None:
        cargs.extend([
            "--white-surf",
            white_surface
        ])
    if blend_surface is not None:
        cargs.extend([
            "--blend-surf",
            blend_surface
        ])
    if multimodal_input is not None:
        cargs.extend([
            "--mmvol",
            multimodal_input
        ])
    if mm_refine:
        cargs.append("--mm-refine")
    if pin_medial_wall is not None:
        cargs.extend([
            "--pin-medial-wall",
            pin_medial_wall
        ])
    if no_intensity_proc:
        cargs.append("--no-intensity-proc")
    if debug_vertex is not None:
        cargs.extend([
            "--debug-vertex",
            str(debug_vertex)
        ])
    if ripflag_out is not None:
        cargs.extend([
            "--ripflag-out",
            ripflag_out
        ])
    if local_max is not None:
        cargs.extend([
            "--local-max",
            local_max
        ])
    if target_surf is not None:
        cargs.extend([
            "--target",
            target_surf
        ])
    if stop_mask:
        cargs.append("--stop")
    if mm_intensity_limits is not None:
        cargs.extend([
            "--mm_{min,max}_{inside,outside}",
            mm_intensity_limits
        ])
    if cover_seg is not None:
        cargs.extend([
            "--cover-seg",
            cover_seg
        ])
    if first_peak_d1:
        cargs.append("--first-peak-d1")
    if first_peak_d2:
        cargs.append("--first-peak-d2")
    if white_border_low_factor is not None:
        cargs.extend([
            "--white_border_low_factor",
            str(white_border_low_factor)
        ])
    if fill_lateral_ventricles is not None:
        cargs.extend([
            "--fill-lat-vents",
            *map(str, fill_lateral_ventricles)
        ])
    cargs.append("[COST_FUNCTION_ARGS]")
    ret = MrisPlaceSurfaceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_PLACE_SURFACE_METADATA",
    "MrisPlaceSurfaceOutputs",
    "mris_place_surface",
]
