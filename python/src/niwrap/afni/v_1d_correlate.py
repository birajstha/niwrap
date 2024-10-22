# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_1D_CORRELATE_METADATA = Metadata(
    id="98a6695a8bc372660a7916494450722774fd95c4.boutiques",
    name="1dCorrelate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V1dCorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_1d_correlate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_1d_correlate(
    input_files: list[InputPathType],
    ktaub: bool = False,
    nboot: float | None = None,
    alpha: float | None = None,
    blk: bool = False,
    runner: Runner | None = None,
) -> V1dCorrelateOutputs:
    """
    1dCorrelate calculates the correlation coefficients between columns of input 1D
    files along with confidence intervals via a bootstrap procedure.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input 1D files.
        ktaub: Kendall's tau_b correlation (popular somewhere, maybe).
        nboot: Set the number of bootstrap replicates.
        alpha: Set the 2-sided confidence interval width to '100-A' percent.
        blk: Alternate flag for variable-length block resampling.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V1dCorrelateOutputs`).
    """
    if alpha is not None and not (1 <= alpha <= 20): 
        raise ValueError(f"'alpha' must be between 1 <= x <= 20 but was {alpha}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_1D_CORRELATE_METADATA)
    cargs = []
    cargs.append("1dCorrelate")
    if ktaub:
        cargs.append("-Ktaub")
    if nboot is not None:
        cargs.extend([
            "-nboot",
            str(nboot)
        ])
    if alpha is not None:
        cargs.extend([
            "-alpha",
            str(alpha)
        ])
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
