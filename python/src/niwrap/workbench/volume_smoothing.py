# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


VOLUME_SMOOTHING_METADATA = Metadata(
    id="66f5f4e076e810dab6414414c93abe661c3d0884",
    name="volume-smoothing",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class VolumeSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_smoothing(
    volume_in: InputPathType,
    kernel: float | int,
    volume_out: InputPathType,
    opt_fwhm: bool = False,
    opt_roi_roivol: InputPathType | None = None,
    opt_fix_zeros: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner = None,
) -> VolumeSmoothingOutputs:
    """
    volume-smoothing by Washington University School of Medicin.
    
    SMOOTH A VOLUME FILE.
    
    Gaussian smoothing for volumes. By default, smooths all subvolumes with no
    ROI, if ROI is given, only positive voxels in the ROI volume have their
    values used, and all other voxels are set to zero. Smoothing a
    non-orthogonal volume will be significantly slower, because the operation
    cannot be separated into 1-dimensional smoothings without distorting the
    kernel shape.
    
    The -fix-zeros option causes the smoothing to not use an input value if it
    is zero, but still write a smoothed value to the voxel. This is useful for
    zeros that indicate lack of information, preventing them from pulling down
    the intensity of nearby voxels, while giving the zero an extrapolated value.
    
    Args:
        volume_in: the volume to smooth
        kernel: the size of the gaussian smoothing kernel in mm, as sigma by
            default
        volume_out: the output volume
        opt_fwhm: kernel size is FWHM, not sigma
        opt_roi_roivol: smooth only from data within an ROI: the volume to use
            as an ROI
        opt_fix_zeros: treat zero values as not being data
        opt_subvolume_subvol: select a single subvolume to smooth: the subvolume
            number or name
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-smoothing")
    cargs.append(execution.input_file(volume_in))
    cargs.append(str(kernel))
    cargs.append(execution.input_file(volume_out))
    if opt_fwhm:
        cargs.append("-fwhm")
    if opt_roi_roivol is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roivol)])
    if opt_fix_zeros:
        cargs.append("-fix-zeros")
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeSmoothingOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_SMOOTHING_METADATA",
    "VolumeSmoothingOutputs",
    "volume_smoothing",
]
