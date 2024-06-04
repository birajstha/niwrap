# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MELODIC_METADATA = Metadata(
    id="2e0b0310f74af57e75efe6beb42411cb502f1806",
    name="melodic",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class MelodicOutputs(typing.NamedTuple):
    """
    Output object returned when calling `melodic(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    report_file: OutputPathType | None
    """Output Melodic web report"""
    ics_output_file: OutputPathType | None
    """Output IC components file"""
    mix_output_file: OutputPathType | None
    """Output mixing matrix file"""
    temporal_mode_file: OutputPathType | None
    """Output matrix of temporal modes"""
    melodic_report_directory: OutputPathType | None
    """Output Melodic report directory"""


def melodic(
    input_file: InputPathType,
    output_directory: str | None = None,
    mask_file: InputPathType | None = None,
    dimensionality_reduction: float | int | None = None,
    generate_report: bool = False,
    cifti_io: bool = False,
    variance_normalization: bool = False,
    no_masking: bool = False,
    update_masking: bool = False,
    no_bet: bool = False,
    bg_threshold: float | int | None = None,
    dimest_technique: str | None = None,
    separate_variance_normalization: bool = False,
    disable_migp: bool = False,
    num_internal_eigenmaps: float | int | None = None,
    migp_shuffle: bool = False,
    migp_factor: float | int | None = None,
    num_ics: float | int | None = None,
    nonlinearity: str | None = None,
    covar_weights: InputPathType | None = None,
    eps_error: float | int | None = None,
    eps_rank1_error: float | int | None = None,
    max_iters: float | int | None = None,
    max_restarts: float | int | None = None,
    mm_threshold: float | int | None = None,
    no_mixture_modeling: bool = False,
    ic_components_file: InputPathType | None = None,
    mixing_matrix_file: InputPathType | None = None,
    session_modes_file: InputPathType | None = None,
    component_filter: str | None = None,
    background_image: InputPathType | None = None,
    tr_seconds: float | int | None = None,
    log_power_calc: bool = False,
    time_domain_design_matrix: InputPathType | None = None,
    time_domain_t_contrast_matrix: InputPathType | None = None,
    subject_domain_design_matrix: InputPathType | None = None,
    subject_domain_t_contrast_matrix: InputPathType | None = None,
    output_unmixing_matrix: bool = False,
    output_stats: bool = False,
    output_pca: bool = False,
    output_whitening: bool = False,
    output_original_ics: bool = False,
    output_mean_volume: bool = False,
    version: bool = False,
    copyright_: bool = False,
    help_: bool = False,
    debug: bool = False,
    report_maps: str | None = None,
    keep_meanvol: bool = False,
    runner: Runner = None,
) -> MelodicOutputs:
    """
    melodic by Christian F. Beckmann, University of Oxford.
    
    Multivariate Exploratory Linear Optimised Decomposition into Independent
    Components.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/MELODIC
    
    Args:
        input_file: Input file names (either single file name or comma-separated
            list or text file)
        output_directory: Output directory name
        mask_file: File name of mask for thresholding
        dimensionality_reduction: Dimensionality reduction into specified number
            of dimensions (default is automatic estimation)
        generate_report: Generate Melodic web report
        cifti_io: Input/output as CIFTI (warning: auto-dimensionality estimation
            for CIFTI data is currently inaccurate)
        variance_normalization: Switch off variance normalization
        no_masking: Switch off masking
        update_masking: Switch off mask updating
        no_bet: Switch off BET
        bg_threshold: Brain / non-brain threshold (only if --nobet selected)
        dimest_technique: Use specific dimensionality estimation technique: lap,
            bic, mdl, aic, mean (default: lap)
        separate_variance_normalization: Switch on separate variance
            normalization for each input dataset (off by default)
        disable_migp: Switch off MIGP data reduction when using -a concat (full
            temporal concatenation will be used)
        num_internal_eigenmaps: Number of internal Eigenmaps
        migp_shuffle: Randomize MIGP file order (default: TRUE)
        migp_factor: Internal Factor of mem-threshold relative to number of
            Eigenmaps (default: 2)
        num_ics: Number of ICs to extract (for deflation approach)
        nonlinearity: Nonlinearity: gauss, tanh, pow3 (default), pow4
        covar_weights: Voxel-wise weights for the covariance matrix (e.g.
            segmentation information)
        eps_error: Minimum error change
        eps_rank1_error: Minimum error change for rank-1 approximation in TICA
        max_iters: Maximum number of iterations before restart
        max_restarts: Maximum number of restarts
        mm_threshold: Threshold for Mixture Model based inference
        no_mixture_modeling: Switch off mixture modeling on IC maps
        ic_components_file: Input filename of the IC components file for mixture
            modeling
        mixing_matrix_file: Input filename of mixing matrix for mixture modeling
            / filtering
        session_modes_file: Input filename of matrix of session modes for report
            generation
        component_filter: List of component numbers to remove
        background_image: Specify background image for report (default: mean
            image)
        tr_seconds: TR in seconds
        log_power_calc: Calculate log of power for frequency spectrum
        time_domain_design_matrix: Design matrix across time-domain
        time_domain_t_contrast_matrix: T-contrast matrix across time-domain
        subject_domain_design_matrix: Design matrix across subject-domain
        subject_domain_t_contrast_matrix: T-contrast matrix across
            subject-domain
        output_unmixing_matrix: Output unmixing matrix
        output_stats: Output thresholded maps and probability maps
        output_pca: Output PCA results
        output_whitening: Output whitening/dewhitening matrices
        output_original_ics: Output the original ICs
        output_mean_volume: Output mean volume
        version: Prints version information
        copyright_: Prints copyright information
        help_: Prints this help message
        debug: Switch on debug messages
        report_maps: Control string for spatial map images (see slicer)
        keep_meanvol: Do not subtract mean volume
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `MelodicOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MELODIC_METADATA)
    cargs = []
    cargs.append("melodic")
    cargs.extend(["-i", execution.input_file(input_file)])
    if output_directory is not None:
        cargs.extend(["-o", output_directory])
    if mask_file is not None:
        cargs.extend(["-m", execution.input_file(mask_file)])
    if dimensionality_reduction is not None:
        cargs.extend(["-d", str(dimensionality_reduction)])
    cargs.append("[APPROACH]")
    if variance_normalization:
        cargs.append("--vn")
    if generate_report:
        cargs.append("--report")
    if cifti_io:
        cargs.append("--CIFTI")
    if no_masking:
        cargs.append("--nomask")
    if update_masking:
        cargs.append("--update_mask")
    if no_bet:
        cargs.append("--nobet")
    if bg_threshold is not None:
        cargs.extend(["--bgthreshold", str(bg_threshold)])
    if dimest_technique is not None:
        cargs.extend(["--dimest", dimest_technique])
    if separate_variance_normalization:
        cargs.append("--sep_vn")
    if disable_migp:
        cargs.append("--disableMigp")
    if num_internal_eigenmaps is not None:
        cargs.extend(["--migpN", str(num_internal_eigenmaps)])
    if migp_shuffle:
        cargs.append("--migp_shuffle")
    if migp_factor is not None:
        cargs.extend(["--migp_factor", str(migp_factor)])
    if num_ics is not None:
        cargs.extend(["-n", str(num_ics)])
    if nonlinearity is not None:
        cargs.extend(["--nl", nonlinearity])
    if covar_weights is not None:
        cargs.extend(["--covarweight", execution.input_file(covar_weights)])
    if eps_rank1_error is not None:
        cargs.extend(["--epsS", str(eps_rank1_error)])
    if eps_error is not None:
        cargs.extend(["--eps", str(eps_error)])
    if max_iters is not None:
        cargs.extend(["--maxit", str(max_iters)])
    if max_restarts is not None:
        cargs.extend(["--maxrestart", str(max_restarts)])
    if mm_threshold is not None:
        cargs.extend(["--mmthresh", str(mm_threshold)])
    if no_mixture_modeling:
        cargs.append("--no_mm")
    if ic_components_file is not None:
        cargs.extend(["--ICs", execution.input_file(ic_components_file)])
    if mixing_matrix_file is not None:
        cargs.extend(["--mix", execution.input_file(mixing_matrix_file)])
    if session_modes_file is not None:
        cargs.extend(["--smode", execution.input_file(session_modes_file)])
    if component_filter is not None:
        cargs.extend(["-f", component_filter])
    if background_image is not None:
        cargs.extend(["--bgimage", execution.input_file(background_image)])
    if tr_seconds is not None:
        cargs.extend(["--tr", str(tr_seconds)])
    if log_power_calc:
        cargs.append("--logPower")
    if time_domain_design_matrix is not None:
        cargs.extend(["--Tdes", execution.input_file(time_domain_design_matrix)])
    if time_domain_t_contrast_matrix is not None:
        cargs.extend(["--Tcon", execution.input_file(time_domain_t_contrast_matrix)])
    if subject_domain_design_matrix is not None:
        cargs.extend(["--Sdes", execution.input_file(subject_domain_design_matrix)])
    if subject_domain_t_contrast_matrix is not None:
        cargs.extend(["--Scon", execution.input_file(subject_domain_t_contrast_matrix)])
    if output_unmixing_matrix:
        cargs.append("--Ounmix")
    if output_stats:
        cargs.append("--Ostats")
    if output_pca:
        cargs.append("--Opca")
    if output_whitening:
        cargs.append("--Owhite")
    if output_original_ics:
        cargs.append("--Oorig")
    if output_mean_volume:
        cargs.append("--Omean")
    if version:
        cargs.append("-V")
    if copyright_:
        cargs.append("--copyright")
    if debug:
        cargs.append("--debug")
    if report_maps is not None:
        cargs.extend(["--report_maps", report_maps])
    if keep_meanvol:
        cargs.append("--keep_meanvol")
    ret = MelodicOutputs(
        root=execution.output_file("."),
        report_file=execution.output_file(f"{output_directory}/report.html", optional=True) if output_directory is not None else None,
        ics_output_file=execution.output_file(f"{output_directory}/melodic_IC.nii.gz", optional=True) if output_directory is not None else None,
        mix_output_file=execution.output_file(f"{output_directory}/melodic_mix", optional=True) if output_directory is not None else None,
        temporal_mode_file=execution.output_file(f"{output_directory}/melodic_Tmodes", optional=True) if output_directory is not None else None,
        melodic_report_directory=execution.output_file(f"{output_directory}/melodic_report", optional=True) if output_directory is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MELODIC_METADATA",
    "MelodicOutputs",
    "melodic",
]
