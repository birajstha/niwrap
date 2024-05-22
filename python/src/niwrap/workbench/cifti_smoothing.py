# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_SMOOTHING_METADATA = Metadata(
    id="94bf1fc84e0408d4655aa0220af4da10ba26c8fc",
    name="cifti-smoothing",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_smoothing(
    cifti: InputPathType,
    surface_kernel: float | int,
    volume_kernel: float | int,
    direction: str,
    cifti_out: InputPathType,
    opt_fwhm: bool = False,
    opt_left_surface_surface: InputPathType | None = None,
    opt_right_surface_surface: InputPathType | None = None,
    opt_cerebellum_surface_surface: InputPathType | None = None,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_fix_zeros_volume: bool = False,
    opt_fix_zeros_surface: bool = False,
    opt_merged_volume: bool = False,
    runner: Runner = None,
) -> CiftiSmoothingOutputs:
    """
    cifti-smoothing by Washington University School of Medicin.
    
    SMOOTH A CIFTI FILE.
    
    The input cifti file must have a brain models mapping on the chosen
    dimension, columns for .dtseries, and either for .dconn. By default, data in
    different structures is smoothed independently (i.e., "parcel constrained"
    smoothing), so volume structures that touch do not smooth across this
    boundary. Specify -merged-volume to ignore these boundaries. Surface
    smoothing uses the GEO_GAUSS_AREA smoothing method.
    
    The -*-corrected-areas options are intended for when it is unavoidable to
    smooth on group average surfaces, it is only an approximate correction for
    the reduction of structure in a group average surface. It is better to
    smooth the data on individuals before averaging, when feasible.
    
    The -fix-zeros-* options will treat values of zero as lack of data, and not
    use that value when generating the smoothed values, but will fill zeros with
    extrapolated values. The ROI should have a brain models mapping along
    columns, exactly matching the mapping of the chosen direction in the input
    file. Data outside the ROI is ignored.
    
    Args:
        cifti: the input cifti
        surface_kernel: the size of the gaussian surface smoothing kernel in mm,
            as sigma by default
        volume_kernel: the size of the gaussian volume smoothing kernel in mm,
            as sigma by default
        direction: which dimension to smooth along, ROW or COLUMN
        cifti_out: the output cifti
        opt_fwhm: kernel sizes are FWHM, not sigma
        opt_left_surface_surface: specify the left surface to use: the left
            surface file
        opt_right_surface_surface: specify the right surface to use: the right
            surface file
        opt_cerebellum_surface_surface: specify the cerebellum surface to use:
            the cerebellum surface file
        opt_cifti_roi_roi_cifti: smooth only within regions of interest: the
            regions to smooth within, as a cifti file
        opt_fix_zeros_volume: treat values of zero in the volume as missing data
        opt_fix_zeros_surface: treat values of zero on the surface as missing
            data
        opt_merged_volume: smooth across subcortical structure boundaries
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-smoothing")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surface_kernel))
    cargs.append(str(volume_kernel))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_fwhm:
        cargs.append("-fwhm")
    if opt_left_surface_surface is not None:
        cargs.extend(["-left-surface", execution.input_file(opt_left_surface_surface)])
    if opt_right_surface_surface is not None:
        cargs.extend(["-right-surface", execution.input_file(opt_right_surface_surface)])
    if opt_cerebellum_surface_surface is not None:
        cargs.extend(["-cerebellum-surface", execution.input_file(opt_cerebellum_surface_surface)])
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_fix_zeros_volume:
        cargs.append("-fix-zeros-volume")
    if opt_fix_zeros_surface:
        cargs.append("-fix-zeros-surface")
    if opt_merged_volume:
        cargs.append("-merged-volume")
    ret = CiftiSmoothingOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_SMOOTHING_METADATA",
    "CiftiSmoothingOutputs",
    "cifti_smoothing",
]
