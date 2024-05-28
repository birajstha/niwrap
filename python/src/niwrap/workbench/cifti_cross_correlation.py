# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_CROSS_CORRELATION_METADATA = Metadata(
    id="fc07303dcd6b9f08ee2adc8e28f051912664067d",
    name="cifti-cross-correlation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiCrossCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_cross_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_cross_correlation(
    cifti_a: InputPathType,
    cifti_b: InputPathType,
    cifti_out: InputPathType,
    opt_weights_weight_file: str | None = None,
    opt_fisher_z: bool = False,
    opt_mem_limit_limit_gb: float | int | None = None,
    runner: Runner = None,
) -> CiftiCrossCorrelationOutputs:
    """
    cifti-cross-correlation by Washington University School of Medicin.
    
    Correlate a cifti file with another cifti file.
    
    Correlates every row in <cifti-a> with every row in <cifti-b>. The mapping
    along columns in <cifti-b> becomes the mapping along rows in the output.
    
    When using the -fisher-z option, the output is NOT a Z-score, it is
    artanh(r), to do further math on this output, consider using -cifti-math.
    
    Restricting the memory usage will make it calculate the output in chunks, by
    reading through <cifti-b> multiple times.
    
    Args:
        cifti_a: first input cifti file
        cifti_b: second input cifti file
        cifti_out: output cifti file
        opt_weights_weight_file: specify column weights: text file containing
            one weight per column
        opt_fisher_z: apply fisher small z transform (ie, artanh) to correlation
        opt_mem_limit_limit_gb: restrict memory usage: memory limit in gigabytes
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiCrossCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CROSS_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-cross-correlation")
    cargs.append(execution.input_file(cifti_a))
    cargs.append(execution.input_file(cifti_b))
    cargs.append(execution.input_file(cifti_out))
    if opt_weights_weight_file is not None:
        cargs.extend(["-weights", opt_weights_weight_file])
    if opt_fisher_z:
        cargs.append("-fisher-z")
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    ret = CiftiCrossCorrelationOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CROSS_CORRELATION_METADATA",
    "CiftiCrossCorrelationOutputs",
    "cifti_cross_correlation",
]
