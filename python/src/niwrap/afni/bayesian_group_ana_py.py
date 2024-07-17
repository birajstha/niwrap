# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BAYESIAN_GROUP_ANA_METADATA = Metadata(
    id="701201b8538d448e2c12a0e2c4a3b39d10b50095",
    name="BayesianGroupAna",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
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
    """Table with the MedianEst, StdDev, 2.50%, 5%, 50%, 95%, and 97.50% of each ROI for the Intercept term."""
    x_var_table: OutputPathType | None
    """The same table as the Intercept but for the specified x variable."""


def bayesian_group_ana(
    data_table: InputPathType,
    y_variable: str,
    prefix: str | None = None,
    x_variables: list[str] | None = None,
    no_center: bool = False,
    iterations: float | int | None = None,
    chains: float | int | None = None,
    control_list: str | None = None,
    plot: bool = False,
    more_plots: list[str] | None = None,
    rdata: bool = False,
    seed: float | int | None = None,
    overwrite: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> BayesianGroupAnaOutputs:
    """
    BayesianGroupAna by AFNI Team.
    
    This program conducts Bayesian Group Analysis (BGA) on a list of regions of
    interest (ROIs). Compared to the conventional univariate GLM, BGA pools and
    shares the information across the ROIs in a multilevel system.
    
    More information:
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
    cargs.append("/opt/afni/src/../install/BayesianGroupAna.py")
    cargs.append("-dataTable")
    cargs.append(execution.input_file(data_table))
    cargs.append("-y")
    cargs.append(y_variable)
    cargs.append("[OPTIONS]")
    ret = BayesianGroupAnaOutputs(
        root=execution.output_file("."),
        summary=execution.output_file(f"{prefix}_summary.txt", optional=True) if prefix is not None else None,
        rhats=execution.output_file(f"{prefix}_rhats.csv", optional=True) if prefix is not None else None,
        intercept_table=execution.output_file(f"{prefix}_Intercept_table.csv", optional=True) if prefix is not None else None,
        x_var_table=execution.output_file(f"{prefix}_table.csv", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BAYESIAN_GROUP_ANA_METADATA",
    "BayesianGroupAnaOutputs",
    "bayesian_group_ana",
]
