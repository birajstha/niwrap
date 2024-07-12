# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VOLUME_ESTIMATE_FWHM_METADATA = Metadata(
    id="a5a800df95fdc292e5a236c6ad888630a0b434a0",
    name="volume-estimate-fwhm",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeEstimateFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_estimate_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_estimate_fwhm(
    volume: InputPathType,
    opt_roi_roivol: InputPathType | None = None,
    opt_subvolume_subvol: str | None = None,
    opt_whole_file: bool = False,
    opt_demean: bool = False,
    runner: Runner | None = None,
) -> VolumeEstimateFwhmOutputs:
    """
    volume-estimate-fwhm by Washington University School of Medicin.
    
    Estimate fwhm smoothness of a volume.
    
    Estimates the smoothness of the input volume in X, Y, and Z directions
    separately, printing the estimates to standard output, in mm as FWHM. If
    -subvolume or -whole-file are not specified, each subvolume is estimated and
    displayed separately.
    
    Args:
        volume: the input volume.
        opt_roi_roivol: use only data within an ROI: the volume to use as an\
            ROI.
        opt_subvolume_subvol: select a single subvolume to estimate smoothness\
            of: the subvolume number or name.
        opt_whole_file: estimate for the whole file at once, not each subvolume\
            separately.
        opt_demean: subtract the mean image before estimating smoothness.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeEstimateFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_ESTIMATE_FWHM_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-estimate-fwhm")
    cargs.append(execution.input_file(volume))
    if opt_roi_roivol is not None:
        cargs.extend(["-roi", execution.input_file(opt_roi_roivol)])
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    if opt_whole_file:
        cargs.append("-whole-file")
    if opt_demean:
        cargs.append("-demean")
    ret = VolumeEstimateFwhmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_ESTIMATE_FWHM_METADATA",
    "VolumeEstimateFwhmOutputs",
    "volume_estimate_fwhm",
]
