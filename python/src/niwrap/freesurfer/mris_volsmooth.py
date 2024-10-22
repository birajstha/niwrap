# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_VOLSMOOTH_METADATA = Metadata(
    id="6daa83c0151b5fa3e4b9db3a35a80f2ff180a3e1.boutiques",
    name="mris_volsmooth",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisVolsmoothOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_volsmooth(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outvol_file: OutputPathType
    """Output volume file after surface-based smoothing."""
    lh_surface_output: OutputPathType | None
    """Left hemisphere smoothed surface output."""
    rh_surface_output: OutputPathType | None
    """Right hemisphere smoothed surface output."""


def mris_volsmooth(
    input_volume: InputPathType,
    output_volume: str,
    registration: InputPathType,
    projfrac: float | None = None,
    projfrac_avg: str | None = None,
    fill_ribbon: bool = False,
    surf_out: str | None = None,
    fwhm: float | None = None,
    niters: float | None = None,
    vol_fwhm: float | None = None,
    log: str | None = None,
    nocleanup: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> MrisVolsmoothOutputs:
    """
    Performs surface-based smoothing inside a volume by sampling a volume to a
    surface, smoothing on the surface, then replacing the surface voxels in the
    volume with values that were smoothed.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_volume: Source volume with values that will be smoothed on the\
            surface.
        output_volume: Output volume.
        registration: TKRegister-style registration matrix that maps between\
            the input/output volumes and the FreeSurfer surface anatomical.
        projfrac: Fraction of thickness to project along surface normal.
        projfrac_avg: Average sampling along normal, specified by min, max, and\
            delta.
        fill_ribbon: Fill ribbon.
        surf_out: Save smoothed surfaces as basename.?h.mgh.
        fwhm: Surface smoothing by full-width/half-max in mm.
        niters: Specify surface smoothing by number of nearest neighbor\
            smoothing iterations.
        vol_fwhm: Volume smoothing outside of the surface. Surface voxels and\
            non-surface voxels are smoothed separately.
        log: Explicitly set log file.
        nocleanup: Do not delete temporary files.
        debug: Turn on debugging.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisVolsmoothOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_VOLSMOOTH_METADATA)
    cargs = []
    cargs.append("mris_volsmooth")
    cargs.append("--i")
    cargs.append(execution.input_file(input_volume))
    cargs.append("--o")
    cargs.append(output_volume)
    cargs.append("--reg")
    cargs.append(execution.input_file(registration))
    if projfrac is not None:
        cargs.extend([
            "--projfrac",
            str(projfrac)
        ])
    if projfrac_avg is not None:
        cargs.extend([
            "--projfrac-avg",
            projfrac_avg
        ])
    if fill_ribbon:
        cargs.append("--fill-ribbon")
    if surf_out is not None:
        cargs.extend([
            "--surf-out",
            surf_out
        ])
    if fwhm is not None:
        cargs.extend([
            "--fwhm",
            str(fwhm)
        ])
    if niters is not None:
        cargs.extend([
            "--niters",
            str(niters)
        ])
    if vol_fwhm is not None:
        cargs.extend([
            "--vol-fwhm",
            str(vol_fwhm)
        ])
    if log is not None:
        cargs.extend([
            "--log",
            log
        ])
    if nocleanup:
        cargs.append("--nocleanup")
    if debug:
        cargs.append("--debug")
    ret = MrisVolsmoothOutputs(
        root=execution.output_file("."),
        outvol_file=execution.output_file(output_volume + ".mgh"),
        lh_surface_output=execution.output_file(surf_out + ".lh.mgh") if (surf_out is not None) else None,
        rh_surface_output=execution.output_file(surf_out + ".rh.mgh") if (surf_out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_VOLSMOOTH_METADATA",
    "MrisVolsmoothOutputs",
    "mris_volsmooth",
]