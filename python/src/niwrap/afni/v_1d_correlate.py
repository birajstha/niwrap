# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_1D_CORRELATE_METADATA = Metadata(
    id="fff4e8147741f246df930fdd3dadbfead6a4b58c",
    name="1dCorrelate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V1dCorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_correlate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_correlate(
    input_files: list[InputPathType],
    pearson: bool = False,
    spearman: bool = False,
    quadrant: bool = False,
    ktaub: bool = False,
    nboot: float | int | None = None,
    alpha: float | int | None = None,
    block: bool = False,
    blk: bool = False,
    runner: Runner | None = None,
) -> V1dCorrelateOutputs:
    """
    1dCorrelate by AFNI Team.
    
    1dCorrelate calculates the correlation coefficients between columns of input
    1D files along with confidence intervals via a bootstrap procedure.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/1dCorrelate.html
    
    Args:
        input_files: Input 1D files.
        pearson: Pearson correlation (the default method).
        spearman: Spearman (rank) correlation (more robust versus outliers).
        quadrant: Quadrant (binarized) correlation (most robust, but weaker).
        ktaub: Kendall's tau_b correlation (popular somewhere, maybe).
        nboot: Set the number of bootstrap replicates.
        alpha: Set the 2-sided confidence interval width to '100-A' percent.
        block: Use variable-length block resampling to account for serial\
            correlation.
        blk: Alternate flag for variable-length block resampling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dCorrelateOutputs`).
    """
    runner = runner or get_global_runner()
    if alpha is not None and not (1 <= alpha <= 20): 
        raise ValueError(f"'alpha' must be between 1 <= x <= 20 but was {alpha}")
    execution = runner.start_execution(V_1D_CORRELATE_METADATA)
    cargs = []
    cargs.append("1dCorrelate")
    if ktaub:
        cargs.append("-Ktaub")
    if nboot is not None:
        cargs.extend(["-nboot", str(nboot)])
    if alpha is not None:
        cargs.extend(["-alpha", str(alpha)])
    if blk:
        cargs.append("-blk")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V1dCorrelateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V1dCorrelateOutputs",
    "V_1D_CORRELATE_METADATA",
    "v_1d_correlate",
]
