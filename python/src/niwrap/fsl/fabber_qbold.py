# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FABBER_QBOLD_METADATA = Metadata(
    id="b61189b4f75286ddaf90831238c383013e79e44b",
    name="fabber_qbold",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl/fabber:latest",
)


class FabberQboldOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_qbold(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    paramnames_file: OutputPathType
    """File containing the names of the model parameters"""
    model_fit_file: OutputPathType
    """4D volume of the model prediction"""
    residuals_file: OutputPathType
    """4D volume of the residuals"""
    model_extras_file: OutputPathType
    """Additional model-specific timeseries data"""
    mvn_file: OutputPathType
    """File containing the final MVN distributions"""
    mean_file: OutputPathType
    """File containing the parameter means"""
    std_file: OutputPathType
    """File containing the parameter standard deviations"""
    var_file: OutputPathType
    """File containing the parameter variances"""
    zstat_file: OutputPathType
    """File containing the parameter Zstats"""
    noise_mean_file: OutputPathType
    """File containing the noise means"""
    noise_std_file: OutputPathType
    """File containing the noise standard deviations"""
    free_energy_file: OutputPathType
    """File containing the free energy, if calculated"""
    logfile: OutputPathType
    """Logfile of the execution"""


def fabber_qbold(
    output_dir: str,
    method: str,
    model: str,
    data: InputPathType,
    data_n: InputPathType | None = None,
    data_order: str | None = "interleave",
    mask: InputPathType | None = None,
    mt_n: float | int | None = None,
    suppdata: InputPathType | None = None,
    listmethods: bool = False,
    listmodels: bool = False,
    listparams: bool = False,
    descparams: bool = False,
    listoutputs: bool = False,
    evaluate: str | None = None,
    evaluate_params: str | None = None,
    evaluate_nt: float | int | None = None,
    simple_output: bool = False,
    overwrite: bool = False,
    link_latest: bool = False,
    loadmodels: InputPathType | None = None,
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
    runner: Runner = None,
) -> FabberQboldOutputs:
    """
    fabber_qbold by FSL.
    
    Fabber - a flexible BaYesian modeling framework for FMRI and MRI analysis.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Fabber
    
    Args:
        output_dir: Directory for output files (including logfile).
        method: Use this inference method.
        model: Use this forward model.
        data: Specify a single input data file.
        data_n: Specify multiple data files for n=1, 2, 3...
        data_order: If multiple data files are specified, how they will be\
            handled: concatenate = one after the other, interleave = first record\
            from each file, then second, etc.
        mask: Mask file. Inference will only be performed where mask value > 0.
        mt_n: List of masked time points, indexed from 1. These will be ignored\
            in the parameter updates.
        suppdata: 'Supplemental' timeseries data, required for some models.
        listmethods: List all known inference methods.
        listmodels: List all known forward models.
        listparams: List model parameters (requires model configuration options\
            to be given).
        descparams: Descript model parameters (name, description, units) -\
            requires model configuration options to be given. Note that not all\
            models provide parameter descriptions.
        listoutputs: List additional model outputs (requires model\
            configuration options to be given).
        evaluate: Evaluate model. Set to name of output required or blank for\
            default output. Requires model configuration options, --evaluate-params\
            and --evaluate-nt.
        evaluate_params: List of parameter values for evaluation.
        evaluate_nt: Number of time points for evaluation - must be consistent\
            with model options where appropriate.
        simple_output: Instead of usual standard output, simply output series\
            of lines each giving progress as percentage.
        overwrite: If set will overwrite existing output. If not set, new\
            output directories will be created by appending '+' to the directory\
            name.
        link_latest: Try to create a link to the most recent output directory\
            with the prefix _latest.
        loadmodels: Load models dynamically from the specified filename, which\
            should be a DLL/shared library.
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
        debug: Output large amounts of debug information. ONLY USE WITH VERY\
            SMALL NUMBERS OF VOXELS.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberQboldOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_QBOLD_METADATA)
    cargs = []
    cargs.append("fabber")
    cargs.append("[--listmethods]")
    cargs.append("[--listmodels]")
    cargs.append("[--listparams]")
    cargs.append("[--descparams]")
    cargs.append("[--listoutputs]")
    cargs.append("[--evaluate]")
    cargs.append("[--evaluate-params]")
    cargs.append("[--evaluate-nt]")
    cargs.append("[--simple-output]")
    cargs.append("[--output]")
    cargs.append("[--overwrite]")
    cargs.append("[--link-to-latest]")
    cargs.append("[--method]")
    cargs.append("[--model]")
    cargs.append("[--loadmodels]")
    cargs.append("[--data]")
    cargs.append("[--data<n>]")
    cargs.append("[--data-order]")
    cargs.append("[--mask]")
    cargs.append("[--mt<n>]")
    cargs.append("[--suppdata]")
    cargs.append("[--dump-param-names]")
    cargs.append("[--save-model-fit]")
    cargs.append("[--save-residuals]")
    cargs.append("[--save-model-extras]")
    cargs.append("[--save-mvn]")
    cargs.append("[--save-mean]")
    cargs.append("[--save-std]")
    cargs.append("[--save-var]")
    cargs.append("[--save-zstat]")
    cargs.append("[--save-noise-mean]")
    cargs.append("[--save-noise-std]")
    cargs.append("[--save-free-energy]")
    cargs.append("[--optfile]")
    cargs.append("[--debug]")
    ret = FabberQboldOutputs(
        root=execution.output_file("."),
        paramnames_file=execution.output_file(f"{output_dir}/paramnames.txt", optional=True),
        model_fit_file=execution.output_file(f"{output_dir}/model_fit.nii.gz", optional=True),
        residuals_file=execution.output_file(f"{output_dir}/residuals.nii.gz", optional=True),
        model_extras_file=execution.output_file(f"{output_dir}/model_extras.nii.gz", optional=True),
        mvn_file=execution.output_file(f"{output_dir}/mvn.nii.gz", optional=True),
        mean_file=execution.output_file(f"{output_dir}/mean.nii.gz", optional=True),
        std_file=execution.output_file(f"{output_dir}/std.nii.gz", optional=True),
        var_file=execution.output_file(f"{output_dir}/var.nii.gz", optional=True),
        zstat_file=execution.output_file(f"{output_dir}/zstat.nii.gz", optional=True),
        noise_mean_file=execution.output_file(f"{output_dir}/noise_mean.nii.gz", optional=True),
        noise_std_file=execution.output_file(f"{output_dir}/noise_std.nii.gz", optional=True),
        free_energy_file=execution.output_file(f"{output_dir}/free_energy.nii.gz", optional=True),
        logfile=execution.output_file(f"{output_dir}/logfile.txt", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_QBOLD_METADATA",
    "FabberQboldOutputs",
    "fabber_qbold",
]
