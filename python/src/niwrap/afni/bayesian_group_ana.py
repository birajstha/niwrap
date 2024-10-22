# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BAYESIAN_GROUP_ANA_METADATA = Metadata(
    id="a1ce8090cf80ecc5ea4041a617ea91e6c7b82df4.boutiques",
    name="BayesianGroupAna",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class BayesianGroupAnaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bayesian_group_ana(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    summary: OutputPathType | None
    """Summary of the brmsfit object from R."""
    rhats: OutputPathType | None
    """Rhats for each effect and x variable combination."""
    intercept_table: OutputPathType | None
    """Table with the MedianEst, StdDev, 2.50%, 5%, 50%, 95%, and 97.50% of each
    ROI for the Intercept term."""
    x_var_table: OutputPathType | None
    """The same table as the Intercept but for the specified x variable."""


def bayesian_group_ana(
    data_table: InputPathType,
    y_variable: str,
    prefix: str | None = None,
    x_variables: list[str] | None = None,
    no_center: bool = False,
    iterations: float | None = None,
    chains: float | None = None,
    control_list: str | None = None,
    plot: bool = False,
    more_plots: list[str] | None = None,
    rdata: bool = False,
    seed: float | None = None,
    overwrite: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> BayesianGroupAnaOutputs:
    """
    This program conducts Bayesian Group Analysis (BGA) on a list of regions of
    interest (ROIs). Compared to the conventional univariate GLM, BGA pools and
    shares the information across the ROIs in a multilevel system.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/BayesianGroupAna.py.html
    
    Args:
        data_table: Input text file containing the data table.
        y_variable: Column name for the y variable.
        prefix: Name of the output file.
        x_variables: Column name(s) for the x variables. If not specified, only\
            the intercept will be added.
        no_center: Disable centering on the x variables. Maybe useful if you\
            centered manually.
        iterations: Number of total iterations per chain including warmup.\
            Default [1000].
        chains: Number of Markov chains. Default [4].
        control_list: Comma separated list of control parameters to pass to the\
            brm function. Default is the brm function defaults.
        plot: Output box, fit, and posterior prediction plots.
        more_plots: Output 'stanplots' given different types of plot names.
        rdata: Save the R session workspace and data.
        seed: Seed to generate random number. Default [1234].
        overwrite: Overwrites the output files.
        help_: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BayesianGroupAnaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BAYESIAN_GROUP_ANA_METADATA)
    cargs = []
    cargs.append("BayesianGroupAna")
    cargs.append(execution.input_file(data_table))
    cargs.append(y_variable)
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if x_variables is not None:
        cargs.extend([
            "-x",
            *x_variables
        ])
    if no_center:
        cargs.append("-no_center")
    if iterations is not None:
        cargs.extend([
            "-iterations",
            str(iterations)
        ])
    if chains is not None:
        cargs.extend([
            "-chains",
            str(chains)
        ])
    if control_list is not None:
        cargs.extend([
            "-control_list",
            control_list
        ])
    if plot:
        cargs.append("-plot")
    if more_plots is not None:
        cargs.extend([
            "-more_plots",
            *more_plots
        ])
    if rdata:
        cargs.append("-RData")
    if seed is not None:
        cargs.extend([
            "-seed",
            str(seed)
        ])
    if overwrite:
        cargs.append("-overwrite")
    if help_:
        cargs.append("-help")
    ret = BayesianGroupAnaOutputs(
        root=execution.output_file("."),
        summary=execution.output_file(prefix + "_summary.txt") if (prefix is not None) else None,
        rhats=execution.output_file(prefix + "_rhats.csv") if (prefix is not None) else None,
        intercept_table=execution.output_file(prefix + "_Intercept_table.csv") if (prefix is not None) else None,
        x_var_table=execution.output_file(prefix + "_table.csv") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BAYESIAN_GROUP_ANA_METADATA",
    "BayesianGroupAnaOutputs",
    "bayesian_group_ana",
]