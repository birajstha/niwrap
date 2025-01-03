# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_GLM_METADATA = Metadata(
    id="13323bbac119e1e50fc454f4295b97cfbae335c5.boutiques",
    name="fsl_glm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class FslGlmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_glm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file_out: OutputPathType | None
    """Output file name for GLM parameter estimates (GLM betas)"""
    output_copes_out: OutputPathType | None
    """Output file name for COPEs (either as text file or image)"""
    output_zstats_out: OutputPathType | None
    """Output file name for Z-stats (either as text file or image)"""
    output_tstats_out: OutputPathType | None
    """Output file name for t-stats (either as text file or image)"""
    output_pvals_out: OutputPathType | None
    """Output file name for p-values of Z-stats (either as text file or
    image)"""
    output_fvals_out: OutputPathType | None
    """Output file name for F-value of full model fit"""
    output_pfvals_out: OutputPathType | None
    """Output file name for p-value for full model fit"""
    output_residuals_out: OutputPathType | None
    """Output file name for residuals"""
    output_varcb_out: OutputPathType | None
    """Output file name for variance of COPEs"""
    output_sigsq_out: OutputPathType | None
    """Output file name for residual noise variance sigma-square"""
    output_data_out: OutputPathType | None
    """Output file name for pre-processed data"""
    output_vnscales_out: OutputPathType | None
    """Output file name for scaling factors for variance normalisation"""


def fsl_glm(
    input_file: InputPathType,
    design_matrix: InputPathType,
    output_file: InputPathType | None = None,
    contrasts: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    dof: float | None = None,
    design_norm_flag: bool = False,
    data_norm_flag: bool = False,
    vn_flag: bool = False,
    demean_flag: bool = False,
    output_copes: InputPathType | None = None,
    output_zstats: InputPathType | None = None,
    output_tstats: InputPathType | None = None,
    output_pvals: InputPathType | None = None,
    output_fvals: InputPathType | None = None,
    output_pfvals: InputPathType | None = None,
    output_residuals: InputPathType | None = None,
    output_varcb: InputPathType | None = None,
    output_sigsq: InputPathType | None = None,
    output_data: InputPathType | None = None,
    output_vnscales: InputPathType | None = None,
    vx_text: list[str] | None = None,
    vx_images: list[InputPathType] | None = None,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslGlmOutputs:
    """
    Simple GLM allowing temporal or spatial regression on either text data or
    images.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        input_file: Input file name (text matrix or 3D/4D image file).
        design_matrix: File name of the GLM design matrix (text time courses\
            for temporal regression or an image file for spatial regression).
        output_file: Output file name for GLM parameter estimates (GLM betas).
        contrasts: Matrix of t-statistics contrasts.
        mask_file: Mask image file name if input is image.
        dof: Set degrees-of-freedom explicitly.
        design_norm_flag: Switch on normalisation of the design matrix columns\
            to unit std. deviation.
        data_norm_flag: Switch on normalisation of the data time series to unit\
            std. deviation.
        vn_flag: Perform MELODIC variance-normalisation on data.
        demean_flag: Switch on de-meaning of design and data.
        output_copes: Output file name for COPEs (either as text file or image).
        output_zstats: Output file name for Z-stats (either as text file or\
            image).
        output_tstats: Output file name for t-stats (either as text file or\
            image).
        output_pvals: Output file name for p-values of Z-stats (either as text\
            file or image).
        output_fvals: Output file name for F-value of full model fit.
        output_pfvals: Output file name for p-value for full model fit.
        output_residuals: Output file name for residuals.
        output_varcb: Output file name for variance of COPEs.
        output_sigsq: Output file name for residual noise variance sigma-square.
        output_data: Output file name for pre-processed data.
        output_vnscales: Output file name for scaling factors for variance\
            normalisation.
        vx_text: List of text files containing text matrix confounds. Caution,\
            BETA option.
        vx_images: List of 4D images containing voxelwise confounds. Caution,\
            BETA option.
        help_flag: Display this help text.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslGlmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_GLM_METADATA)
    cargs = []
    cargs.append("fsl_glm")
    cargs.extend([
        "-i",
        execution.input_file(input_file)
    ])
    cargs.extend([
        "-d",
        execution.input_file(design_matrix)
    ])
    if output_file is not None:
        cargs.extend([
            "-o",
            execution.input_file(output_file)
        ])
    if contrasts is not None:
        cargs.extend([
            "-c",
            execution.input_file(contrasts)
        ])
    if mask_file is not None:
        cargs.extend([
            "-m",
            execution.input_file(mask_file)
        ])
    if dof is not None:
        cargs.extend([
            "--dof",
            str(dof)
        ])
    if design_norm_flag:
        cargs.append("--des_norm")
    if data_norm_flag:
        cargs.append("--dat_norm")
    if vn_flag:
        cargs.append("--vn")
    if demean_flag:
        cargs.append("--demean")
    if output_copes is not None:
        cargs.extend([
            "--out_cope",
            execution.input_file(output_copes)
        ])
    if output_zstats is not None:
        cargs.extend([
            "--out_z",
            execution.input_file(output_zstats)
        ])
    if output_tstats is not None:
        cargs.extend([
            "--out_t",
            execution.input_file(output_tstats)
        ])
    if output_pvals is not None:
        cargs.extend([
            "--out_p",
            execution.input_file(output_pvals)
        ])
    if output_fvals is not None:
        cargs.extend([
            "--out_f",
            execution.input_file(output_fvals)
        ])
    if output_pfvals is not None:
        cargs.extend([
            "--out_pf",
            execution.input_file(output_pfvals)
        ])
    if output_residuals is not None:
        cargs.extend([
            "--out_res",
            execution.input_file(output_residuals)
        ])
    if output_varcb is not None:
        cargs.extend([
            "--out_varcb",
            execution.input_file(output_varcb)
        ])
    if output_sigsq is not None:
        cargs.extend([
            "--out_sigsq",
            execution.input_file(output_sigsq)
        ])
    if output_data is not None:
        cargs.extend([
            "--out_data",
            execution.input_file(output_data)
        ])
    if output_vnscales is not None:
        cargs.extend([
            "--out_vnscales",
            execution.input_file(output_vnscales)
        ])
    if vx_text is not None:
        cargs.extend([
            "--vxt",
            *vx_text
        ])
    if vx_images is not None:
        cargs.extend([
            "--vxf",
            *[execution.input_file(f) for f in vx_images]
        ])
    if help_flag:
        cargs.append("-h")
    ret = FslGlmOutputs(
        root=execution.output_file("."),
        output_file_out=execution.output_file(pathlib.Path(output_file).name + ".nii.gz") if (output_file is not None) else None,
        output_copes_out=execution.output_file(pathlib.Path(output_copes).name + ".nii.gz") if (output_copes is not None) else None,
        output_zstats_out=execution.output_file(pathlib.Path(output_zstats).name + ".nii.gz") if (output_zstats is not None) else None,
        output_tstats_out=execution.output_file(pathlib.Path(output_tstats).name + ".nii.gz") if (output_tstats is not None) else None,
        output_pvals_out=execution.output_file(pathlib.Path(output_pvals).name + ".nii.gz") if (output_pvals is not None) else None,
        output_fvals_out=execution.output_file(pathlib.Path(output_fvals).name + ".nii.gz") if (output_fvals is not None) else None,
        output_pfvals_out=execution.output_file(pathlib.Path(output_pfvals).name + ".nii.gz") if (output_pfvals is not None) else None,
        output_residuals_out=execution.output_file(pathlib.Path(output_residuals).name + ".nii.gz") if (output_residuals is not None) else None,
        output_varcb_out=execution.output_file(pathlib.Path(output_varcb).name + ".nii.gz") if (output_varcb is not None) else None,
        output_sigsq_out=execution.output_file(pathlib.Path(output_sigsq).name + ".nii.gz") if (output_sigsq is not None) else None,
        output_data_out=execution.output_file(pathlib.Path(output_data).name + ".nii.gz") if (output_data is not None) else None,
        output_vnscales_out=execution.output_file(pathlib.Path(output_vnscales).name + ".nii.gz") if (output_vnscales is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_GLM_METADATA",
    "FslGlmOutputs",
    "fsl_glm",
]
