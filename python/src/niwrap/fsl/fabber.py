# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_METADATA = Metadata(
    id="9b4801e7e3b720f0591a2b526cd78b167ed49de3.boutiques",
    name="fabber",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """File containing the names of the model parameters"""
    model_fit_file: OutputPathType
    """The model fit output file"""
    residuals_file: OutputPathType
    """The residuals output file"""
    model_extras_file: OutputPathType
    """The model extras output file"""
    mvn_file: OutputPathType
    """The MVN distributions output file"""
    mean_file: OutputPathType
    """The parameter means output file"""
    std_file: OutputPathType
    """The parameter standard deviations output file"""
    var_file: OutputPathType
    """The parameter variances output file"""
    zstat_file: OutputPathType
    """The parameter Zstats output file"""
    noise_mean_file: OutputPathType
    """The noise means output file"""
    noise_std_file: OutputPathType
    """The noise standard deviations output file"""
    free_energy_file: OutputPathType
    """The free energy output file"""


def fabber(
    output: str,
    method: str,
    model: str,
    data_file: InputPathType,
    data_files: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask_file: InputPathType | None = None,
    mt_n: float | None = None,
    supp_data: InputPathType | None = None,
    evaluate_output: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_to_latest: bool = False,
    load_models: InputPathType | None = None,
    debug: bool = False,
    optfile: InputPathType | None = None,
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
    help_: bool = False,
    list_methods: bool = False,
    list_models: bool = False,
    list_params: bool = False,
    desc_params: bool = False,
    list_outputs: bool = False,
    optfile_: InputPathType | None = None,
    old_optfile: InputPathType | None = None,
    runner: Runner | None = None,
) -> FabberOutputs:
    """
    Fabber is a tool for model-based Bayesian analysis of time-series data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        output: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data_file: Specify a single input data file.
        data_files: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled.
        mask_file: Mask file. Inference will only be performed where mask value\
            > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        supp_data: 'Supplemental' timeseries data, required for some models.
        evaluate_output: Evaluate model. Set to name of output required or\
            blank for default output. Requires model configuration options,\
            --evaluate-params and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_to_latest: Try to create a link to the most recent output\
            directory with the prefix _latest.
        load_models: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
        optfile: Read options in option=value form from the specified file.
        save_model_fit: Output the model prediction as a 4d volume.
        save_residuals: Output the residuals (difference between the data and\
            the model prediction).
        save_model_extras: Output any additional model-specific timeseries data.
        save_mvn: Output the final MVN distributions.
        save_mean: Output the parameter means.
        save_std: Output the parameter standard deviations.
        save_var: Output the parameter variances.
        save_zstat: Output the parameter Z-stats.
        save_noise_mean: Output the noise means. The noise distribution\
            inferred is the precision of a Gaussian noise source.
        save_noise_std: Output the noise standard deviations.
        save_free_energy: Output the free energy, if calculated.
        help_: Print this usage method. If given with --method or --model,\
            display relevant method/model usage information.
        list_methods: List all known inference methods.
        list_models: List all known forward models.
        list_params: List model parameters (requires model configuration\
            options to be given).
        desc_params: Describe model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        list_outputs: List additional model outputs (requires model\
            configuration options to be given).
        optfile_: Read options in option=value form from the specified file.
        old_optfile: Read options in command line form from the specified file\
            (DEPRECATED).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_METADATA)
    cargs = []
    cargs.append("fabber")
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
        execution.input_file(data_file)
    ])
    if data_files is not None:
        cargs.extend([
            "--data<n>",
            execution.input_file(data_files)
        ])
    if data_order is not None:
        cargs.extend([
            "--data-order",
            data_order
        ])
    if mask_file is not None:
        cargs.extend([
            "--mask",
            execution.input_file(mask_file)
        ])
    if mt_n is not None:
        cargs.extend([
            "--mt<n>",
            str(mt_n)
        ])
    if supp_data is not None:
        cargs.extend([
            "--suppdata",
            execution.input_file(supp_data)
        ])
    if evaluate_output is not None:
        cargs.extend([
            "--evaluate",
            evaluate_output
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
    if simple_output:
        cargs.append("--simple-output")
    if overwrite:
        cargs.append("--overwrite")
    if link_to_latest:
        cargs.append("--link-to-latest")
    if load_models is not None:
        cargs.extend([
            "--loadmodels",
            execution.input_file(load_models)
        ])
    if debug:
        cargs.append("--debug")
    if optfile is not None:
        cargs.extend([
            "-f",
            execution.input_file(optfile)
        ])
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
    if help_:
        cargs.append("--help")
    if list_methods:
        cargs.append("--listmethods")
    if list_models:
        cargs.append("--listmodels")
    if list_params:
        cargs.append("--listparams")
    if desc_params:
        cargs.append("--descparams")
    if list_outputs:
        cargs.append("--listoutputs")
    if optfile_ is not None:
        cargs.extend([
            "-f",
            execution.input_file(optfile_)
        ])
    if old_optfile is not None:
        cargs.extend([
            "-@",
            execution.input_file(old_optfile)
        ])
    ret = FabberOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file(output + "/paramnames.txt"),
        model_fit_file=execution.output_file(output + "/model_fit.nii.gz"),
        residuals_file=execution.output_file(output + "/residuals.nii.gz"),
        model_extras_file=execution.output_file(output + "/model_extras.nii.gz"),
        mvn_file=execution.output_file(output + "/mvn.nii.gz"),
        mean_file=execution.output_file(output + "/mean.nii.gz"),
        std_file=execution.output_file(output + "/std.nii.gz"),
        var_file=execution.output_file(output + "/var.nii.gz"),
        zstat_file=execution.output_file(output + "/zstat.nii.gz"),
        noise_mean_file=execution.output_file(output + "/noise_mean.nii.gz"),
        noise_std_file=execution.output_file(output + "/noise_std.nii.gz"),
        free_energy_file=execution.output_file(output + "/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_METADATA",
    "FabberOutputs",
    "fabber",
]
