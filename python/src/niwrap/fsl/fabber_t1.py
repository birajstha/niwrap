# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_T1_METADATA = Metadata(
    id="226e046a747617a247e8a3d9c7a9094ffb89ebb4.boutiques",
    name="fabber_t1",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberT1Outputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_t1(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    param_names: OutputPathType
    """File containing the names of the model parameters"""
    model_fit: OutputPathType
    """Output the model prediction as a 4D volume"""
    residuals: OutputPathType
    """Output the residuals (difference between the data and the model
    prediction)"""
    model_extras: OutputPathType
    """Output any additional model-specific timeseries data"""
    mvn_distributions: OutputPathType
    """Output the final MVN distributions"""
    param_means: OutputPathType
    """Output the parameter means"""
    param_stds: OutputPathType
    """Output the parameter standard deviations"""
    param_vars: OutputPathType
    """Output the parameter variances"""
    param_zstats: OutputPathType
    """Output the parameter Z-stats"""
    noise_means: OutputPathType
    """Output the noise means"""
    noise_stds: OutputPathType
    """Output the noise standard deviations"""
    free_energy: OutputPathType
    """Output the free energy"""


def fabber_t1(
    output: str,
    method: str,
    model: str,
    data: InputPathType,
    data_mult: list[InputPathType] | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    masked_time_points: list[float] | None = None,
    supp_data: InputPathType | None = None,
    overwrite: bool = False,
    link_to_latest: bool = False,
    simple_output: bool = False,
    load_models: InputPathType | None = None,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    dump_param_names: bool = False,
    save_model_fit: bool = False,
    save_residuals: bool = False,
    save_model_extras: bool = False,
    save_mvn: bool = False,
    save_mean: bool = False,
    save_std: bool = False,
    save_var: bool = False,
    save_zstat: bool = False,
    save_noise_mean: bool = False,
    save_noise_std: bool = False,
    save_free_energy: bool = False,
    optfile: InputPathType | None = None,
    debug: bool = False,
    runner: Runner | None = None,
) -> FabberT1Outputs:
    """
    Fabber is a tool for performing model-based analysis of fMRI data, using
    advanced Bayesian inference techniques.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output: Directory for output files (including logfile).
        method: Inference method to use.
        model: Forward model to use.
        data: Specify a single input data file.
        data_mult: Specify multiple data files for n=1, 2, 3...
        data_order: How multiple data files are handled: concatenate or\
            interleave.
        mask: Mask file. Inference will only be performed where mask value > 0.
        masked_time_points: List of masked time points, indexed from 1. These\
            will be ignored in the parameter updates.
        supp_data: Supplemental timeseries data, required for some models.
        overwrite: Overwrite existing output. If not set, new output\
            directories will be created by appending '+' to the directory name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        simple_output: Simple output format: progress as percentage.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        dump_param_names: Write the file paramnames.txt containing the names of\
            the model parameters.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Zstats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        optfile: File containing additional options, one per line, in the same\
            form as specified on the command line.
        debug: Output large amounts of debug information.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberT1Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_T1_METADATA)
    cargs = []
    cargs.append("fabber_t1")
    cargs.extend([
        "--output",
        output
    ])
    cargs.extend([
        "--method",
        method
    ])
    cargs.extend([
        "--model",
        model
    ])
    cargs.extend([
        "--data",
        execution.input_file(data)
    ])
    if data_mult is not None:
        cargs.extend([
            "--data<n>",
            *[execution.input_file(f) for f in data_mult]
        ])
    if data_order is not None:
        cargs.extend([
            "--data-order",
            data_order
        ])
    if mask is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask)
        ])
    if masked_time_points is not None:
        cargs.extend([
            "--mt<n>",
            *map(str, masked_time_points)
        ])
    if supp_data is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(supp_data)
        ])
    if overwrite:
        cargs.append("--overwrite")
    if link_to_latest:
        cargs.append("--link-to-latest")
    if simple_output:
        cargs.append("--simple-output")
    if load_models is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(load_models)
        ])
    if evaluate is not None:
        cargs.extend([
            "--evaluate",
            evaluate
        ])
    if evaluate_params is not None:
        cargs.extend([
            "--evaluate-params",
            evaluate_params
        ])
    if evaluate_nt is not None:
        cargs.extend([
            "--evaluate-nt",
            str(evaluate_nt)
        ])
    if dump_param_names:
        cargs.append("--dump-param-names")
    if save_model_fit:
        cargs.append("--save-model-fit")
    if save_residuals:
        cargs.append("--save-residuals")
    if save_model_extras:
        cargs.append("--save-model-extras")
    if save_mvn:
        cargs.append("--save-mvn")
    if save_mean:
        cargs.append("--save-mean")
    if save_std:
        cargs.append("--save-std")
    if save_var:
        cargs.append("--save-var")
    if save_zstat:
        cargs.append("--save-zstat")
    if save_noise_mean:
        cargs.append("--save-noise-mean")
    if save_noise_std:
        cargs.append("--save-noise-std")
    if save_free_energy:
        cargs.append("--save-free-energy")
    if optfile is not None:
        cargs.extend([
            "--optfile",
            execution.input_file(optfile)
        ])
    if debug:
        cargs.append("--debug")
    ret = FabberT1Outputs(
        root=execution.output_file("."),
        param_names=execution.output_file(output + "/paramnames.txt"),
        model_fit=execution.output_file(output + "/model_prediction.nii.gz"),
        residuals=execution.output_file(output + "/residuals.nii.gz"),
        model_extras=execution.output_file(output + "/model_extras.nii.gz"),
        mvn_distributions=execution.output_file(output + "/mvn_distributions.nii.gz"),
        param_means=execution.output_file(output + "/param_means.nii.gz"),
        param_stds=execution.output_file(output + "/param_stds.nii.gz"),
        param_vars=execution.output_file(output + "/param_vars.nii.gz"),
        param_zstats=execution.output_file(output + "/param_zstats.nii.gz"),
        noise_means=execution.output_file(output + "/noise_means.nii.gz"),
        noise_stds=execution.output_file(output + "/noise_stds.nii.gz"),
        free_energy=execution.output_file(output + "/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_T1_METADATA",
    "FabberT1Outputs",
    "fabber_t1",
]
