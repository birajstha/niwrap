# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EDDY_METADATA = Metadata(
    id="8f466b46846f19a611c06f1d0834a8091de316fd.boutiques",
    name="eddy",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class EddyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """Output file containing the corrected images"""
    eddy_parameters: OutputPathType
    """Text file containing subject movement and EC-induced field parameters for
    each volume"""
    rotated_bvecs: OutputPathType
    """File containing the reoriented b-vectors for diffusion analysis"""
    rotated_bvecs_slr: OutputPathType
    """File with rotated b-vectors for least-squares reconstruction"""
    command_txt: OutputPathType
    """Text file documenting the command line used to run eddy"""
    input_parameters: OutputPathType
    """List of all parameters used by eddy"""
    movement_rms: OutputPathType
    """Summary of total movement for each volume"""
    restricted_movement_rms: OutputPathType
    """Estimates movement RMS while disregarding translation in the PE
    direction"""
    shell_alignment_parameters: OutputPathType
    """Text file with rigid body movement parameters between different shells"""
    shell_pe_translation_parameters: OutputPathType
    """Translation parameters along the PE direction between different shells"""
    outlier_report: OutputPathType
    """Report of detected outlier slices"""
    outlier_map: OutputPathType
    """Numeric matrix indicating outlier slices"""
    outlier_n_stdev_map: OutputPathType
    """Map of the number of standard deviations for outliers"""
    outlier_n_sqr_stdev_map: OutputPathType
    """Map of the number of squared standard deviations for outliers"""
    outlier_free_data: OutputPathType
    """Original data with outlier slices replaced, only if --repol was set"""
    movement_over_time: OutputPathType
    """Text file with movement parameters over time, only if --mporder > 0"""
    mbs_first_order_fields: OutputPathType
    """4D image file of partial derivative fields, only if
    --estimate_move_by_susceptibility is set"""
    cnr_maps: OutputPathType
    """4D image file with SNR and CNR maps, only if --cnr_maps is set"""
    residuals: OutputPathType
    """4D image file of residuals, only if --residuals is set"""


def eddy(
    imain: InputPathType,
    mask: InputPathType,
    index: InputPathType,
    acqp: InputPathType,
    bvecs: InputPathType,
    bvals: InputPathType,
    implementation: typing.Literal["", "_openmp", "_cuda", "_cuda10.2", "_cuda9.1", "_cuda8.0"] = "",
    out: str = "eddy_corrected",
    mb: float | None = None,
    mb_offs: float | None = None,
    slspec: InputPathType | None = None,
    json_: InputPathType | None = None,
    mporder: float | None = None,
    s2v_lambda: float | None = None,
    topup: InputPathType | None = None,
    field: InputPathType | None = None,
    field_mat: InputPathType | None = None,
    flm: typing.Literal["movement", "linear", "quadratic", "cubic"] | None = None,
    slm: typing.Literal["none", "linear", "quadratic"] | None = None,
    fwhm: float | None = None,
    niter: float | None = None,
    s2v_niter: float | None = None,
    cnr_maps: bool = False,
    residuals: bool = False,
    fep: bool = False,
    interp: typing.Literal["spline", "trilinear"] | None = None,
    s2v_interp: typing.Literal["spline", "trilinear"] | None = None,
    resamp: typing.Literal["jac", "lsr"] | None = None,
    nvoxhp: float | None = None,
    initrand: float | None = None,
    ff: float | None = None,
    repol: bool = False,
    ol_nstd: float | None = None,
    ol_nvox: float | None = None,
    ol_type: typing.Literal["sw", "gw", "both"] | None = None,
    ol_pos: bool = False,
    ol_sqr: bool = False,
    estimate_move_by_susceptibility: bool = False,
    mbs_niter: float | None = None,
    mbs_lambda: float | None = None,
    mbs_ksp: float | None = None,
    dont_sep_offs_move: bool = False,
    dont_peas: bool = False,
    data_is_shelled: bool = False,
    verbose: bool = False,
    runner: Runner | None = None,
) -> EddyOutputs:
    """
    A tool for correcting eddy currents and movements in diffusion data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        imain: File containing all the images to estimate distortions for.
        mask: Mask to indicate brain.
        index: File containing indices for all volumes in --imain into --acqp\
            and --topup.
        acqp: File containing acquisition parameters.
        bvecs: File containing the b-vectors for all volumes in --imain.
        bvals: File containing the b-values for all volumes in --imain.
        implementation: Choose the implementation to use.
        out: Basename for output.
        mb: Multi-band factor.
        mb_offs: Multi-band offset (-1 if bottom slice removed, 1 if top slice\
            removed).
        slspec: Name of text file completely specifying slice/group acuistion.\
            N.B. --slspec and --json are mutually exclusive.
        json_: Name of .json text file with information about slice timing.\
            N.B. --json and --slspec are mutually exclusive.
        mporder: Order of slice-to-vol movement model (default 0, i.e.\
            vol-to-vol.
        s2v_lambda: Regularisation weight for slice-to-vol movement. (default\
            1, reasonable range 1--10).
        topup: Base name for output files from topup.
        field: Name of file with susceptibility field (in Hz).
        field_mat: Name of rigid body transform for susceptibility field.
        flm: First level EC model (movement/linear/quadratic/cubic, default\
            quadratic).
        slm: Second level EC model (none/linear/quadratic, default none).
        fwhm: FWHM for conditioning filter when estimating the parameters\
            (default 0).
        niter: Number of iterations (default 5).
        s2v_niter: Number of iterations for slice-to-vol (default 5).
        cnr_maps: Write shell-wise cnr-maps (default false).
        residuals: Write residuals (between GP and observations), (default\
            false).
        fep: Fill empty planes in x- or y-directions (default false).
        interp: Interpolation model for estimation step (spline/trilinear,\
            default spline).
        s2v_interp: Slice-to-vol interpolation model for estimation step\
            (spline/trilinear, default trilinear).
        resamp: Final resampling method (jac/lsr, default jac).
        nvoxhp: # of voxels used to estimate the hyperparameters (default 1000).
        initrand: Seeds rand for when selecting voxels (default 0=no seeding).
        ff: Fudge factor for hyperparameter error variance (default 10.0).
        repol: Detect and replace outlier slices (default false)).
        ol_nstd: Number of std off to qualify as outlier (default 4).
        ol_nvox: Min # of voxels in a slice for inclusion in outlier detection\
            (default 250).
        ol_type: Type of outliers, slicewise (sw), groupwise (gw) or both\
            (both). (default sw).
        ol_pos: Consider both positive and negative outliers if set (default\
            false).
        ol_sqr: Consider outliers among sums-of-squared differences if set\
            (default false).
        estimate_move_by_susceptibility: Estimate how susceptibility field\
            changes with subject movement (default false).
        mbs_niter: Number of iterations for MBS estimation (default 10).
        mbs_lambda: Weighting of regularisation for MBS estimation (default 10).
        mbs_ksp: Knot-spacing for MBS field estimation (default 10mm).
        dont_sep_offs_move: Do NOT attempt to separate field offset from\
            subject movement (default false).
        dont_peas: Do NOT perform a post-eddy alignment of shells (default\
            false).
        data_is_shelled: Assume, don't check, that data is shelled (default\
            false).
        verbose: switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_METADATA)
    cargs = []
    cargs.append("eddy" + implementation)
    cargs.append("--imain=" + execution.input_file(imain))
    cargs.append("--mask=" + execution.input_file(mask))
    cargs.append("--index=" + execution.input_file(index))
    cargs.append("--acqp=" + execution.input_file(acqp))
    cargs.append("--bvecs=" + execution.input_file(bvecs))
    cargs.append("--bvals=" + execution.input_file(bvals))
    cargs.append("--out=" + out)
    if mb is not None:
        cargs.append("--mb=" + str(mb))
    if mb_offs is not None:
        cargs.append("--mb_offs=" + str(mb_offs))
    if slspec is not None:
        cargs.append("--slspec=" + execution.input_file(slspec))
    if json_ is not None:
        cargs.append("--json=" + execution.input_file(json_))
    if mporder is not None:
        cargs.append("--mporder=" + str(mporder))
    if s2v_lambda is not None:
        cargs.append("--s2v_lambda=" + str(s2v_lambda))
    if topup is not None:
        cargs.append("--topup=" + execution.input_file(topup, resolve_parent=True))
    if field is not None:
        cargs.append("--field=" + execution.input_file(field))
    if field_mat is not None:
        cargs.append("--field_mat=" + execution.input_file(field_mat))
    if flm is not None:
        cargs.append("--flm=" + flm)
    if slm is not None:
        cargs.append("--slm=" + slm)
    if fwhm is not None:
        cargs.append("--fwhm=" + str(fwhm))
    if niter is not None:
        cargs.append("--niter=" + str(niter))
    if s2v_niter is not None:
        cargs.append("--s2v_niter=" + str(s2v_niter))
    if cnr_maps:
        cargs.append("--cnr_maps")
    if residuals:
        cargs.append("--residuals")
    if fep:
        cargs.append("--fep")
    if interp is not None:
        cargs.append("--interp=" + interp)
    if s2v_interp is not None:
        cargs.append("--s2v_interp=" + s2v_interp)
    if resamp is not None:
        cargs.append("--resamp=" + resamp)
    if nvoxhp is not None:
        cargs.append("--nvoxhp=" + str(nvoxhp))
    if initrand is not None:
        cargs.append("--initrand=" + str(initrand))
    if ff is not None:
        cargs.append("--ff=" + str(ff))
    if repol:
        cargs.append("--repol")
    if ol_nstd is not None:
        cargs.append("--ol_nstd=" + str(ol_nstd))
    if ol_nvox is not None:
        cargs.append("--ol_nvox=" + str(ol_nvox))
    if ol_type is not None:
        cargs.append("--ol_type=" + ol_type)
    if ol_pos:
        cargs.append("--ol_pos")
    if ol_sqr:
        cargs.append("--ol_sqr")
    if estimate_move_by_susceptibility:
        cargs.append("--estimate_move_by_susceptibility")
    if mbs_niter is not None:
        cargs.append("--mbs_niter=" + str(mbs_niter))
    if mbs_lambda is not None:
        cargs.append("--mbs_lambda=" + str(mbs_lambda))
    if mbs_ksp is not None:
        cargs.append("--mbs_ksp=" + str(mbs_ksp))
    if dont_sep_offs_move:
        cargs.append("--dont_sep_offs_move")
    if dont_peas:
        cargs.append("--dont_peas")
    if data_is_shelled:
        cargs.append("--data_is_shelled")
    if verbose:
        cargs.append("--verbose")
    ret = EddyOutputs(
        root=execution.output_file("."),
        out=execution.output_file(out + ".nii.gz"),
        eddy_parameters=execution.output_file(out + ".eddy_parameters"),
        rotated_bvecs=execution.output_file(out + ".eddy_rotated_bvecs"),
        rotated_bvecs_slr=execution.output_file(out + ".eddy_rotated_bvecs_for_SLR"),
        command_txt=execution.output_file(out + ".eddy_command_txt"),
        input_parameters=execution.output_file(out + ".eddy_values_of_all_input_parameters"),
        movement_rms=execution.output_file(out + ".eddy_movement_rms"),
        restricted_movement_rms=execution.output_file(out + ".eddy_restricted_movement_rms"),
        shell_alignment_parameters=execution.output_file(out + ".eddy_post_eddy_shell_alignment_parameters"),
        shell_pe_translation_parameters=execution.output_file(out + ".eddy_post_eddy_shell_PE_translation_parameters"),
        outlier_report=execution.output_file(out + ".eddy_outlier_report"),
        outlier_map=execution.output_file(out + ".eddy_outlier_map"),
        outlier_n_stdev_map=execution.output_file(out + ".eddy_outlier_n_stdev_map"),
        outlier_n_sqr_stdev_map=execution.output_file(out + ".eddy_outlier_n_sqr_stdev_map"),
        outlier_free_data=execution.output_file(out + ".eddy_outlier_free_data.nii.gz"),
        movement_over_time=execution.output_file(out + ".eddy_movement_over_time"),
        mbs_first_order_fields=execution.output_file(out + ".eddy_mbs_first_order_fields.nii.gz"),
        cnr_maps=execution.output_file(out + ".eddy_cnr_maps"),
        residuals=execution.output_file(out + ".eddy_residuals"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EDDY_METADATA",
    "EddyOutputs",
    "eddy",
]
