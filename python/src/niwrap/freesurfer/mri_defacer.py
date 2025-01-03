# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_DEFACER_METADATA = Metadata(
    id="1b6a737bd3d80434774e54823d1c3ab67e9eccdf.boutiques",
    name="mri_defacer",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriDefacerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_defacer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_defacer(
    input_volume: InputPathType,
    headmask: InputPathType,
    tempsurf: InputPathType,
    defaced_volume: str,
    templabel: list[InputPathType] | None = None,
    watermark: float | None = None,
    facemask: str | None = None,
    fill_constants: list[float] | None = None,
    exclude_mask: InputPathType | None = None,
    tempreg: InputPathType | None = None,
    minsurfpath: str | None = None,
    maxsurfpath: str | None = None,
    distbounds: InputPathType | None = None,
    distoverlay: InputPathType | None = None,
    distdat: InputPathType | None = None,
    statspath: InputPathType | None = None,
    output_tempsurf: InputPathType | None = None,
    apply_to_volume: list[str] | None = None,
    ripple_center: list[float] | None = None,
    apply_ripple: list[str] | None = None,
    diagnostic_level: float | None = None,
    debug: bool = False,
    checkopts: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MriDefacerOutputs:
    """
    Tool for defacing MRI images to remove facial features.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Input volume.
        headmask: Head mask volume.
        tempsurf: Template surface file.
        defaced_volume: Output defaced volume.
        templabel: Template label, specify one or multiple labels.
        watermark: Watermark density.
        facemask: Face mask volume.
        fill_constants: Constants for filling within/outside the mask.
        exclude_mask: Mask to exclude from defacing.
        tempreg: Registration file to apply to surface.
        minsurfpath: Output minimum surface path.
        maxsurfpath: Output maximum surface path.
        distbounds: File with distance bounds for each label.
        distoverlay: Overlay file showing distance for each vertex.
        distdat: File with distances for each vertex.
        statspath: Statistics path for nxmask with means and modes.
        output_tempsurf: Output template surface after watermark/ripple.
        apply_to_volume: Apply face mask and registration to another volume.
        ripple_center: Center of ripple effect.
        apply_ripple: Apply ripple effect on surface.
        diagnostic_level: Set diagnostic level.
        debug: Turn on debugging.
        checkopts: Check options and exit without executing.
        version: Print version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriDefacerOutputs`).
    """
    if apply_to_volume is not None and (len(apply_to_volume) != 4): 
        raise ValueError(f"Length of 'apply_to_volume' must be 4 but was {len(apply_to_volume)}")
    if apply_ripple is not None and (len(apply_ripple) != 6): 
        raise ValueError(f"Length of 'apply_ripple' must be 6 but was {len(apply_ripple)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_DEFACER_METADATA)
    cargs = []
    cargs.append("mri_defacer")
    cargs.extend([
        "-i",
        execution.input_file(input_volume)
    ])
    cargs.extend([
        "-hm",
        execution.input_file(headmask)
    ])
    cargs.extend([
        "-ts",
        execution.input_file(tempsurf)
    ])
    if templabel is not None:
        cargs.extend([
            "--l",
            *[execution.input_file(f) for f in templabel]
        ])
    if watermark is not None:
        cargs.extend([
            "--w",
            str(watermark)
        ])
    cargs.extend([
        "-o",
        defaced_volume
    ])
    if facemask is not None:
        cargs.extend([
            "--m",
            facemask
        ])
    if fill_constants is not None:
        cargs.extend([
            "--fill-const",
            *map(str, fill_constants)
        ])
    if exclude_mask is not None:
        cargs.extend([
            "--xmask",
            execution.input_file(exclude_mask)
        ])
    if tempreg is not None:
        cargs.extend([
            "--reg",
            execution.input_file(tempreg)
        ])
    if minsurfpath is not None:
        cargs.extend([
            "--min",
            minsurfpath
        ])
    if maxsurfpath is not None:
        cargs.extend([
            "--max",
            maxsurfpath
        ])
    if distbounds is not None:
        cargs.extend([
            "--distbounds",
            execution.input_file(distbounds)
        ])
    if distoverlay is not None:
        cargs.extend([
            "--distoverlay",
            execution.input_file(distoverlay)
        ])
    if distdat is not None:
        cargs.extend([
            "--distdat",
            execution.input_file(distdat)
        ])
    if statspath is not None:
        cargs.extend([
            "--stats",
            execution.input_file(statspath)
        ])
    if output_tempsurf is not None:
        cargs.extend([
            "--ots",
            execution.input_file(output_tempsurf)
        ])
    if apply_to_volume is not None:
        cargs.extend([
            "--apply",
            *apply_to_volume
        ])
    if ripple_center is not None:
        cargs.extend([
            "--ripple-center",
            *map(str, ripple_center)
        ])
    if apply_ripple is not None:
        cargs.extend([
            "--apply-ripple",
            *apply_ripple
        ])
    if diagnostic_level is not None:
        cargs.extend([
            "--gdiag",
            str(diagnostic_level)
        ])
    if debug:
        cargs.append("--debug")
    if checkopts:
        cargs.append("--checkopts")
    if version:
        cargs.append("--version")
    ret = MriDefacerOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_DEFACER_METADATA",
    "MriDefacerOutputs",
    "mri_defacer",
]
