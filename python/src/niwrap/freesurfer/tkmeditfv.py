# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TKMEDITFV_METADATA = Metadata(
    id="c54cb02c761041c3c2bd1fa2a8964899175b9969.boutiques",
    name="tkmeditfv",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class TkmeditfvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tkmeditfv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tkmeditfv(
    mainvol: InputPathType,
    subject: str | None = None,
    aux_volume: InputPathType | None = None,
    seg_volume: InputPathType | None = None,
    overlay: InputPathType | None = None,
    timecourse: InputPathType | None = None,
    overlay_registration: InputPathType | None = None,
    surface: list[str] | None = None,
    extra_volumes: list[InputPathType] | None = None,
    crs_location: list[float] | None = None,
    zoom_level: float | None = None,
    additional_segments: list[InputPathType] | None = None,
    load_white: bool = False,
    load_pial: bool = False,
    load_orig: bool = False,
    load_orig_nofix: bool = False,
    load_smoothwm_nofix: bool = False,
    load_white_preaparc: bool = False,
    load_inflated: bool = False,
    annot: str | None = None,
    load_aparc: bool = False,
    surfext: str | None = None,
    seg_outline: bool = False,
    intensity_minmax: list[float] | None = None,
    load_defects: bool = False,
    load_defect_pointset: bool = False,
    trilin_interpolation: bool = False,
    neurological_orientation: bool = False,
    rotate_around_cursor: bool = False,
    vgl_display: bool = False,
    use_tkmedit: bool = False,
    load_aparc_aseg: bool = False,
    runner: Runner | None = None,
) -> TkmeditfvOutputs:
    """
    A wrapper script to run Freeview with arguments similar to tkmedit, providing
    both functionalities.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        mainvol: Main volume file path.
        subject: Subject's name.
        aux_volume: Auxiliary volume file path.
        seg_volume: Segmentation volume file path.
        overlay: Overlay volume file path.
        timecourse: Timecourse for overlay.
        overlay_registration: Overlay timecourse registration file.
        surface: Load surface with optional color.
        extra_volumes: Load extra volume(s).
        crs_location: Place cursor at given (col, row, slice) location.
        zoom_level: Set zoom level.
        additional_segments: Add additional segmentations.
        load_white: Load lh and rh.white surfaces.
        load_pial: Load lh and rh.pial surfaces.
        load_orig: Load lh and rh.orig surfaces.
        load_orig_nofix: Load lh and rh.orig.nofix surfaces.
        load_smoothwm_nofix: Load lh and rh.smoothwm.nofix surfaces.
        load_white_preaparc: Load lh and rh.white.preaparc surfaces.
        load_inflated: Load lh and rh.inflated surfaces.
        annot: Load annotation file.
        load_aparc: Load aparc annotation.
        surfext: Add extension to the name of the surface.
        seg_outline: Enable segmentation outline mode.
        intensity_minmax: Set intensity min and max on first volume.
        load_defects: Load info needed to evaluate defects.
        load_defect_pointset: Load defect pointset.
        trilin_interpolation: Use trilinear interpolation for volume overlays.
        neurological_orientation: Use neurological orientation instead of\
            radiological.
        rotate_around_cursor: Rotate around cursor in 3D view.
        vgl_display: Set VGL_DISPLAY and run with vglrun.
        use_tkmedit: Use tkmedit instead of freeview.
        load_aparc_aseg: Load aparc+aseg.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TkmeditfvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TKMEDITFV_METADATA)
    cargs = []
    cargs.append("tkmeditfv")
    if subject is not None:
        cargs.append(subject)
    cargs.append(execution.input_file(mainvol))
    if aux_volume is not None:
        cargs.extend([
            "-aux",
            execution.input_file(aux_volume)
        ])
    if seg_volume is not None:
        cargs.extend([
            "-seg",
            execution.input_file(seg_volume)
        ])
    if overlay is not None:
        cargs.extend([
            "-ov",
            execution.input_file(overlay)
        ])
    if timecourse is not None:
        cargs.extend([
            "-t",
            execution.input_file(timecourse)
        ])
    if overlay_registration is not None:
        cargs.extend([
            "-reg",
            execution.input_file(overlay_registration)
        ])
    if surface is not None:
        cargs.extend([
            "-surf",
            *surface
        ])
    if extra_volumes is not None:
        cargs.extend([
            "-vol",
            *[execution.input_file(f) for f in extra_volumes]
        ])
    if crs_location is not None:
        cargs.extend([
            "-crs",
            *map(str, crs_location)
        ])
    if zoom_level is not None:
        cargs.extend([
            "-zoom",
            str(zoom_level)
        ])
    if additional_segments is not None:
        cargs.extend([
            "-seg2",
            *[execution.input_file(f) for f in additional_segments]
        ])
    if load_white:
        cargs.append("-white")
    if load_pial:
        cargs.append("-pial")
    if load_orig:
        cargs.append("-orig")
    if load_orig_nofix:
        cargs.append("-orig.nofix")
    if load_smoothwm_nofix:
        cargs.append("-smoothwm.nofix")
    if load_white_preaparc:
        cargs.append("-white.preaparc")
    if load_inflated:
        cargs.append("-inflated")
    if annot is not None:
        cargs.extend([
            "-annot",
            annot
        ])
    if load_aparc:
        cargs.append("-aparc")
    if surfext is not None:
        cargs.extend([
            "-surfext",
            surfext
        ])
    if seg_outline:
        cargs.append("-seg-outline")
    if intensity_minmax is not None:
        cargs.extend([
            "-main-minmax",
            *map(str, intensity_minmax)
        ])
    if load_defects:
        cargs.append("-defects")
    if load_defect_pointset:
        cargs.append("-defectps")
    if trilin_interpolation:
        cargs.append("-trilin")
    if neurological_orientation:
        cargs.append("-neuro")
    if rotate_around_cursor:
        cargs.append("-rotate-around-cursor")
    if vgl_display:
        cargs.append("-vgl")
    if use_tkmedit:
        cargs.append("-tkmedit")
    if load_aparc_aseg:
        cargs.append("-aparc+aseg")
    ret = TkmeditfvOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TKMEDITFV_METADATA",
    "TkmeditfvOutputs",
    "tkmeditfv",
]
