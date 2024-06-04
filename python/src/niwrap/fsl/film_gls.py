# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FILM_GLS_METADATA = Metadata(
    id="32d2d29f2358012f2366f7a7e89860c2840706b7",
    name="film_gls",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FilmGlsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `film_gls(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    prewhitened_data: OutputPathType
    """Prewhitened data output"""
    average_design_matrix: OutputPathType
    """Average design matrix output"""
    results_data: OutputPathType
    """Results output"""


def film_gls(
    infile: InputPathType,
    ac_flag: bool = False,
    threshold: float | int | None = None,
    ar_flag: bool = False,
    noest_flag: bool = False,
    output_pw_flag: bool = False,
    pava_flag: bool = False,
    sa_flag: bool = False,
    verbose_flag: bool = False,
    results_dir: str | None = None,
    mode: str | None = None,
    input_surface: InputPathType | None = None,
    mean_func_file: InputPathType | None = None,
    min_timepoint_file: InputPathType | None = None,
    paradigm_file: InputPathType | None = None,
    t_contrasts_file: InputPathType | None = None,
    f_contrasts_file: InputPathType | None = None,
    epith: float | int | None = None,
    ms: float | int | None = None,
    tukey: float | int | None = None,
    mt: float | int | None = None,
    ven: list[str] = None,
    vef: list[InputPathType] = None,
    runner: Runner = None,
) -> FilmGlsOutputs:
    """
    film_gls by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    General Linear Model fitting with autocorrelation in FMRI.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FILM
    
    Args:
        infile: Input data file (NIFTI for volumetric, GIFTI for surface)
        ac_flag: Perform autocorrelation estimation only
        threshold: Initial threshold to apply to input data
        ar_flag: Fits autoregressive model - default is to use tukey with
            M=sqrt(numvols)
        noest_flag: Do not estimate autocorrelations
        output_pw_flag: Output prewhitened data and average design matrix
        pava_flag: Estimates autocorrelation using PAVA - default is to use
            tukey with M=sqrt(numvols)
        sa_flag: Smooths autocorrelation estimates
        verbose_flag: Outputs full data
        results_dir: Directory name to store results in, default is results
        mode: Analysis mode, options are volumetric (default) or surface.
            Caution: surface-based functionality is still BETA
        input_surface: Input surface for autocorrelation smoothing in
            surface-based analyses
        mean_func_file: Re-estimate mean_func baseline - for use with perfusion
            subtraction
        min_timepoint_file: Minimum timepoint file
        paradigm_file: Paradigm file
        t_contrasts_file: T-contrasts file
        f_contrasts_file: F-contrasts file
        epith: SUSAN brightness threshold for volumetric analysis/smoothing
            sigma for surface analysis
        ms: SUSAN mask size for volumetric analysis/smoothing extent for surface
            analysis
        tukey: Uses tukey window to estimate autocorrelation with window size
            num - default is to use tukey with M=sqrt(numvols)
        mt: Uses multitapering with slepian tapers and num is the time-bandwidth
            product - default is to use tukey with M=sqrt(numvols)
        ven: List of numbers indicating voxelwise EVs position in the design
            matrix (list order corresponds to files in vxf option). Caution BETA
            option, only use with volumetric analysis.
        vef: List of 4D images containing voxelwise EVs (list order corresponds
            to numbers in vxl option). Caution BETA option, only use with volumetric
            analysis.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FilmGlsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILM_GLS_METADATA)
    cargs = []
    cargs.append("film_gls")
    cargs.append(execution.input_file(infile))
    if ac_flag:
        cargs.append("--ac")
    if threshold is not None:
        cargs.extend(["--thr", str(threshold)])
    if ar_flag:
        cargs.append("--ar")
    if noest_flag:
        cargs.append("--noest")
    if output_pw_flag:
        cargs.append("--outputPWdata")
    if pava_flag:
        cargs.append("--pava")
    if sa_flag:
        cargs.append("--sa")
    if verbose_flag:
        cargs.append("-v")
    if results_dir is not None:
        cargs.extend(["--rn", results_dir])
    if mode is not None:
        cargs.extend(["--mode", mode])
    if input_surface is not None:
        cargs.extend(["--in2", execution.input_file(input_surface)])
    if mean_func_file is not None:
        cargs.extend(["--mf", execution.input_file(mean_func_file)])
    if min_timepoint_file is not None:
        cargs.extend(["--mft", execution.input_file(min_timepoint_file)])
    if paradigm_file is not None:
        cargs.extend(["--pd", execution.input_file(paradigm_file)])
    if t_contrasts_file is not None:
        cargs.extend(["--con", execution.input_file(t_contrasts_file)])
    if f_contrasts_file is not None:
        cargs.extend(["--fcon", execution.input_file(f_contrasts_file)])
    if epith is not None:
        cargs.extend(["--epith", str(epith)])
    if ms is not None:
        cargs.extend(["--ms", str(ms)])
    if tukey is not None:
        cargs.extend(["--tukey", str(tukey)])
    if mt is not None:
        cargs.extend(["--mt", str(mt)])
    if ven is not None:
        cargs.extend(["--ven", *ven])
    if vef is not None:
        cargs.extend(["--vef", *[execution.input_file(f) for f in vef]])
    ret = FilmGlsOutputs(
        root=execution.output_file("."),
        prewhitened_data=execution.output_file(f"[rn]/prewhitened_data.nii.gz", optional=True),
        average_design_matrix=execution.output_file(f"[rn]/average_design_matrix.txt", optional=True),
        results_data=execution.output_file(f"[rn]/results.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILM_GLS_METADATA",
    "FilmGlsOutputs",
    "film_gls",
]
