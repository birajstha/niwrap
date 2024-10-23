# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FUGUE_METADATA = Metadata(
    id="6f420f4e48114e62d493a0e92de4e88d1fa52520.boutiques",
    name="fugue",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FugueOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fugue(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fmap_out_file_outfile: OutputPathType | None
    """Fieldmap file."""
    shift_out_file_outfile: OutputPathType | None
    """Voxel shift map file."""
    unwarped_file_outfile: OutputPathType | None
    """Unwarped file."""
    warped_file_outfile: OutputPathType | None
    """Forward warped file."""


def fugue(
    asym_se_time: float | None = None,
    despike_2dfilter: bool = False,
    despike_threshold: float | None = None,
    dwell_time: float | None = None,
    dwell_to_asym_ratio: float | None = None,
    fmap_in_file: InputPathType | None = None,
    fmap_out_file: InputPathType | None = None,
    forward_warping: bool = False,
    fourier_order: int | None = None,
    icorr: bool = False,
    icorr_only: bool = False,
    in_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    median_2dfilter: bool = False,
    no_extend: bool = False,
    no_gap_fill: bool = False,
    nokspace: bool = False,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    pava: bool = False,
    phase_conjugate: bool = False,
    phasemap_in_file: InputPathType | None = None,
    poly_order: int | None = None,
    save_fmap: bool = False,
    save_shift: bool = False,
    save_unmasked_fmap: bool = False,
    save_unmasked_shift: bool = False,
    shift_in_file: InputPathType | None = None,
    shift_out_file: InputPathType | None = None,
    smooth2d: float | None = None,
    smooth3d: float | None = None,
    unwarp_direction: typing.Literal["x", "y", "z", "x-", "y-", "z-"] | None = None,
    unwarped_file: InputPathType | None = None,
    warped_file: InputPathType | None = None,
    runner: Runner | None = None,
) -> FugueOutputs:
    """
    FMRIB's Utility for Geometric Unwarping of EPIs.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        asym_se_time: Set the fieldmap asymmetric spin echo time (sec).
        despike_2dfilter: Apply a 2d de-spiking filter.
        despike_threshold: Specify the threshold for de-spiking (default=3.0).
        dwell_time: Set the epi dwell time per phase-encode line - same as echo\
            spacing - (sec).
        dwell_to_asym_ratio: Set the dwell to asym time ratio.
        fmap_in_file: Filename for loading fieldmap (rad/s).
        fmap_out_file: Filename for saving fieldmap (rad/s).
        forward_warping: Apply forward warping instead of unwarping.
        fourier_order: Apply fourier (sinusoidal) fitting of order n.
        icorr: Apply intensity correction to unwarping (pixel shift method\
            only).
        icorr_only: Apply intensity correction only.
        in_file: Filename of input volume.
        mask_file: Filename for loading valid mask.
        median_2dfilter: Apply 2d median filtering.
        no_extend: Do not apply rigid-body extrapolation to the fieldmap.
        no_gap_fill: Do not apply gap-filling measure to the fieldmap.
        nokspace: Do not use k-space forward warping.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        pava: Apply monotonic enforcement via pava.
        phase_conjugate: Apply phase conjugate method of unwarping.
        phasemap_in_file: Filename for input phase image.
        poly_order: Apply polynomial fitting of order n.
        save_fmap: Write field map volume.
        save_shift: Write pixel shift volume.
        save_unmasked_fmap: Saves the unmasked fieldmap when using --savefmap.
        save_unmasked_shift: Saves the unmasked shiftmap when using\
            --saveshift.
        shift_in_file: Filename for reading pixel shift volume.
        shift_out_file: Filename for saving pixel shift volume.
        smooth2d: Apply 2d gaussian smoothing of sigma n (in mm).
        smooth3d: Apply 3d gaussian smoothing of sigma n (in mm).
        unwarp_direction: 'x' or 'y' or 'z' or 'x-' or 'y-' or 'z-'. Specifies\
            direction of warping (default y).
        unwarped_file: Apply unwarping and save as filename.
        warped_file: Apply forward warping and save as filename.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FugueOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FUGUE_METADATA)
    cargs = []
    cargs.append("fugue")
    if asym_se_time is not None:
        cargs.append("--asym=" + str(asym_se_time))
    if despike_2dfilter:
        cargs.append("--despike")
    if despike_threshold is not None:
        cargs.append("--despikethreshold=" + str(despike_threshold))
    if dwell_time is not None:
        cargs.append("--dwell=" + str(dwell_time))
    if dwell_to_asym_ratio is not None:
        cargs.append("--dwelltoasym=" + str(dwell_to_asym_ratio))
    if fmap_in_file is not None:
        cargs.append("--loadfmap=" + execution.input_file(fmap_in_file))
    if fmap_out_file is not None:
        cargs.append("--savefmap=" + execution.input_file(fmap_out_file))
    if forward_warping:
        cargs.append("--forward_warping")
    if fourier_order is not None:
        cargs.append("--fourier=" + str(fourier_order))
    if icorr:
        cargs.append("--icorr")
    if icorr_only:
        cargs.append("--icorronly")
    if in_file is not None:
        cargs.append("--in=" + execution.input_file(in_file))
    if mask_file is not None:
        cargs.append("--mask=" + execution.input_file(mask_file))
    if median_2dfilter:
        cargs.append("--median")
    if no_extend:
        cargs.append("--noextend")
    if no_gap_fill:
        cargs.append("--nofill")
    if nokspace:
        cargs.append("--nokspace")
    if output_type is not None:
        cargs.append(output_type)
    if pava:
        cargs.append("--pava")
    if phase_conjugate:
        cargs.append("--phaseconj")
    if phasemap_in_file is not None:
        cargs.append("--phasemap=" + execution.input_file(phasemap_in_file))
    if poly_order is not None:
        cargs.append("--poly=" + str(poly_order))
    if save_fmap:
        cargs.append("--save_fmap")
    if save_shift:
        cargs.append("--save_shift")
    if save_unmasked_fmap:
        cargs.append("--unmaskfmap")
    if save_unmasked_shift:
        cargs.append("--unmaskshift")
    if shift_in_file is not None:
        cargs.append("--loadshift=" + execution.input_file(shift_in_file))
    if shift_out_file is not None:
        cargs.append("--saveshift=" + execution.input_file(shift_out_file))
    if smooth2d is not None:
        cargs.append("--smooth2=" + str(smooth2d))
    if smooth3d is not None:
        cargs.append("--smooth3=" + str(smooth3d))
    if unwarp_direction is not None:
        cargs.append("--unwarpdir=" + unwarp_direction)
    if unwarped_file is not None:
        cargs.append("--unwarp=" + execution.input_file(unwarped_file))
    if warped_file is not None:
        cargs.append("--warp=" + execution.input_file(warped_file))
    ret = FugueOutputs(
        root=execution.output_file("."),
        fmap_out_file_outfile=execution.output_file(pathlib.Path(fmap_out_file).name) if (fmap_out_file is not None) else None,
        shift_out_file_outfile=execution.output_file(pathlib.Path(shift_out_file).name) if (shift_out_file is not None) else None,
        unwarped_file_outfile=execution.output_file(pathlib.Path(unwarped_file).name) if (unwarped_file is not None) else None,
        warped_file_outfile=execution.output_file(pathlib.Path(warped_file).name) if (warped_file is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FUGUE_METADATA",
    "FugueOutputs",
    "fugue",
]
