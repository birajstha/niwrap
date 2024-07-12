# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SIENA_CAL_METADATA = Metadata(
    id="412fb22df44167ed5a9995e2cbef1ed5fac928d4",
    name="siena_cal",
)


class SienaCalOutputs(typing.NamedTuple):
    """
    Output object returned when calling `siena_cal(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dir: OutputPathType
    """Output directory containing SIENA results"""


def siena_cal(
    input1_file: InputPathType,
    input2_file: InputPathType,
    scale: float | int,
    siena_diff_options: str | None = None,
    runner: Runner | None = None,
) -> SienaCalOutputs:
    """
    siena_cal.
    
    SIENA is part of FSL (FMRIB Software Library), which performs a
    two-timepoint brain volume change analysis.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/SIENA
    
    Args:
        input1_file: First input image file root (e.g., baseline image root).
        input2_file: Second input image file root (e.g., follow-up image root).
        scale: Voxel size scaling factor.
        siena_diff_options: Optional SIENA difference options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SienaCalOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIENA_CAL_METADATA)
    cargs = []
    cargs.append("siena_cal")
    cargs.append(execution.input_file(input1_file))
    cargs.append(execution.input_file(input2_file))
    cargs.append(str(scale))
    if siena_diff_options is not None:
        cargs.append(siena_diff_options)
    ret = SienaCalOutputs(
        root=execution.output_file("."),
        output_dir=execution.output_file(f"{pathlib.Path(input1_file).name}_to_{pathlib.Path(input2_file).name}_siena", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIENA_CAL_METADATA",
    "SienaCalOutputs",
    "siena_cal",
]
