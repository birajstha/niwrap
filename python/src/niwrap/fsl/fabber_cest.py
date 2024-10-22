# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FABBER_CEST_METADATA = Metadata(
    id="d0c794144f9c1291cd815f24506dde4e858126c8.boutiques",
    name="fabber_cest",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FabberCestOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fabber_cest(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    logfile: OutputPathType
    """Log file"""
    modelfit_out: OutputPathType
    """Model fit output as a 4d volume"""
    residuals_out: OutputPathType
    """Residuals output as a 4d volume"""
    modelextras_out: OutputPathType
    """Model extras output"""
    mvn_out: OutputPathType
    """Final MVN distributions output"""
    mean_out: OutputPathType
    """Parameter means output"""
    std_out: OutputPathType
    """Parameter standard deviations output"""
    var_out: OutputPathType
    """Parameter variances output"""
    zstat_out: OutputPathType
    """Parameter Z statistics output"""
    noise_mean_out: OutputPathType
    """Noise means output"""
    noise_std_out: OutputPathType
    """Noise standard deviations output"""
    free_energy_out: OutputPathType
    """Free energy output"""


def fabber_cest(
    runner: Runner | None = None,
) -> FabberCestOutputs:
    """
    Fabber Model-based Analysis.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FabberCestOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FABBER_CEST_METADATA)
    cargs = []
    cargs.append("fabber")
    cargs.append("[--<option>")
    cargs.append("|")
    cargs.append("--<option>=<value>")
    cargs.append("...]")
    ret = FabberCestOutputs(
        root=execution.output_file("."),
        logfile=execution.output_file("[--output]/logfile.log"),
        modelfit_out=execution.output_file("[--output]/model_fit.nii.gz"),
        residuals_out=execution.output_file("[--output]/residuals.nii.gz"),
        modelextras_out=execution.output_file("[--output]/model_extras.nii.gz"),
        mvn_out=execution.output_file("[--output]/mvn.nii.gz"),
        mean_out=execution.output_file("[--output]/mean.nii.gz"),
        std_out=execution.output_file("[--output]/std.nii.gz"),
        var_out=execution.output_file("[--output]/var.nii.gz"),
        zstat_out=execution.output_file("[--output]/zstat.nii.gz"),
        noise_mean_out=execution.output_file("[--output]/noise_mean.nii.gz"),
        noise_std_out=execution.output_file("[--output]/noise_std.nii.gz"),
        free_energy_out=execution.output_file("[--output]/free_energy.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FABBER_CEST_METADATA",
    "FabberCestOutputs",
    "fabber_cest",
]
