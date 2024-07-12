# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VOLUME_PARCEL_RESAMPLING_GENERIC_METADATA = Metadata(
    id="2d59e55bf5f32ec1b28306be516bbaec72a0a07d",
    name="volume-parcel-resampling-generic",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeParcelResamplingGenericOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_parcel_resampling_generic(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """output volume"""


def volume_parcel_resampling_generic(
    volume_in: InputPathType,
    cur_parcels: InputPathType,
    new_parcels: InputPathType,
    kernel: float | int,
    volume_out: str,
    opt_fwhm: bool = False,
    opt_fix_zeros: bool = False,
    opt_subvolume_subvol: str | None = None,
    runner: Runner | None = None,
) -> VolumeParcelResamplingGenericOutputs:
    """
    volume-parcel-resampling-generic by Washington University School of Medicin.
    
    Smooth and resample volume parcels from different volume space.
    
    Smooths and resamples the region inside each label in cur-parcels to the
    region of the same label name in new-parcels. Any voxels in the output label
    region but outside the input label region will be extrapolated from nearby
    data. The -fix-zeros option causes the smoothing to not use an input value
    if it is zero, but still write a smoothed value to the voxel, and after
    smoothing is complete, it will check for any remaining values of zero, and
    fill them in with extrapolated values. The output volume will use the volume
    space of new-parcels, which does not need to be in the same volume space as
    the input.
    
    Args:
        volume_in: the input data volume.
        cur_parcels: label volume of where the parcels currently are.
        new_parcels: label volume of where the parcels should be.
        kernel: gaussian kernel size in mm to smooth by during resampling, as\
            sigma by default.
        volume_out: output volume.
        opt_fwhm: smoothing kernel size is FWHM, not sigma.
        opt_fix_zeros: treat zero values as not being data.
        opt_subvolume_subvol: select a single subvolume as input: the subvolume\
            number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VolumeParcelResamplingGenericOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_PARCEL_RESAMPLING_GENERIC_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-parcel-resampling-generic")
    cargs.append(execution.input_file(volume_in))
    cargs.append(execution.input_file(cur_parcels))
    cargs.append(execution.input_file(new_parcels))
    cargs.append(str(kernel))
    cargs.append(volume_out)
    if opt_fwhm:
        cargs.append("-fwhm")
    if opt_fix_zeros:
        cargs.append("-fix-zeros")
    if opt_subvolume_subvol is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvol])
    ret = VolumeParcelResamplingGenericOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{volume_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_PARCEL_RESAMPLING_GENERIC_METADATA",
    "VolumeParcelResamplingGenericOutputs",
    "volume_parcel_resampling_generic",
]
