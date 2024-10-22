# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RBA_METADATA = Metadata(
    id="e398b3a57e7258897bfc2032d62fb4854a2e607c.boutiques",
    name="RBA",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RbaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rba(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_txt: OutputPathType
    """Main output text file with inference information for effects of
    interest."""
    output_rdata: OutputPathType
    """Saved R data in binary format for post hoc processing."""


def rba(
    prefix: str,
    data_table: InputPathType,
    chains: float | None = None,
    iterations: float | None = None,
    model: str | None = None,
    eoi: str | None = None,
    wcp: float | None = None,
    tstat: str | None = None,
    stdz: str | None = None,
    c_vars: str | None = None,
    q_vars: str | None = None,
    dist_roi: str | None = None,
    dist_subj: str | None = None,
    dist_y: str | None = None,
    ridge_plot: str | None = None,
    roi: str | None = None,
    subj: str | None = None,
    scale: float | None = None,
    se: str | None = None,
    pdp: str | None = None,
    mean: str | None = None,
    sigma: str | None = None,
    debug: bool = False,
    verbose: float | None = None,
    md: bool = False,
    r2z: bool = False,
    runner: Runner | None = None,
) -> RbaOutputs:
    """
    Region-Based Analysis Program through Bayesian Multilevel Modeling.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix for output file names.
        data_table: Data table in pure text format.
        chains: Specify the number of Markov chains.
        iterations: Specify the number of iterations per Markov chain.
        model: Specify the model formula.
        eoi: Identify effects of interest in the output.
        wcp: Invoke within-chain parallelization.
        tstat: Specify the column name that lists the t-statistic values.
        stdz: Identify quantitative variables (or covariates) to be\
            standardized.
        c_vars: Identify categorical (qualitative) variables (or factors).
        q_vars: Identify quantitative variables (or covariates).
        dist_roi: Specify the distribution for the ROIs.
        dist_subj: Specify the distribution for the subjects.
        dist_y: Specify the distribution for the response variable.
        ridge_plot: Plot the posterior distributions stacked together.
        roi: Specify the column name that is designated as the region variable.
        subj: Specify the column name that is designated as the measuring unit\
            variable (usually subject).
        scale: Specify a multiplier for the Y values.
        se: This option indicates that standard error for the response variable\
            is available as input.
        pdp: Specify the layout of posterior distribution plot.
        mean: Specify the formulation for the mean of the likelihood (sampling\
            distribution).
        sigma: Specify the formulation for the standard deviation (sigma) of\
            the likelihood (sampling distribution).
        debug: This option will enable R to save the parameters in a file for\
            debugging.
        verbose: Specify verbose level.
        md: This option indicates that there are missing data in the input.
        r2z: Perform Fisher transformation on the response variable if it is a\
            correlation coefficient.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RbaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RBA_METADATA)
    cargs = []
    cargs.append("RBA")
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.extend([
        "-dataTable",
        execution.input_file(data_table)
    ])
    if chains is not None:
        cargs.extend([
            "-chains",
            str(chains)
        ])
    if iterations is not None:
        cargs.extend([
            "-iterations",
            str(iterations)
        ])
    if model is not None:
        cargs.extend([
            "-model",
            model
        ])
    if eoi is not None:
        cargs.extend([
            "-EOI",
            eoi
        ])
    if wcp is not None:
        cargs.extend([
            "-WCP",
            str(wcp)
        ])
    if tstat is not None:
        cargs.extend([
            "-tstat",
            tstat
        ])
    if stdz is not None:
        cargs.extend([
            "-stdz",
            stdz
        ])
    if c_vars is not None:
        cargs.extend([
            "-cVars",
            c_vars
        ])
    if q_vars is not None:
        cargs.extend([
            "-qVars",
            q_vars
        ])
    if dist_roi is not None:
        cargs.extend([
            "-distROI",
            dist_roi
        ])
    if dist_subj is not None:
        cargs.extend([
            "-distSubj",
            dist_subj
        ])
    if dist_y is not None:
        cargs.extend([
            "-distY",
            dist_y
        ])
    if ridge_plot is not None:
        cargs.extend([
            "-ridgePlot",
            ridge_plot
        ])
    if roi is not None:
        cargs.extend([
            "-ROI",
            roi
        ])
    if subj is not None:
        cargs.extend([
            "-Subj",
            subj
        ])
    if scale is not None:
        cargs.extend([
            "-scale",
            str(scale)
        ])
    if se is not None:
        cargs.extend([
            "-se",
            se
        ])
    if pdp is not None:
        cargs.extend([
            "-PDP",
            pdp
        ])
    if mean is not None:
        cargs.extend([
            "-mean",
            mean
        ])
    if sigma is not None:
        cargs.extend([
            "-sigma",
            sigma
        ])
    if debug:
        cargs.append("-dbgArgs")
    if verbose is not None:
        cargs.extend([
            "-verb",
            str(verbose)
        ])
    if md:
        cargs.append("-MD")
    if r2z:
        cargs.append("-r2z")
    ret = RbaOutputs(
        root=execution.output_file("."),
        output_txt=execution.output_file(prefix + ".txt"),
        output_rdata=execution.output_file(prefix + ".RData"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RBA_METADATA",
    "RbaOutputs",
    "rba",
]
