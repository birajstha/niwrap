# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_MERGE_METADATA = Metadata(
    id="2a43fcd0e4825044122b337043bd5c3a4ffa9030",
    name="cifti-merge",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_merge(
    cifti_out: InputPathType,
    opt_direction_direction: str | None = None,
    opt_mem_limit_limit_gb: float | int | None = None,
    opt_cifti_cifti_in: InputPathType | None = None,
    runner: Runner = None,
) -> CiftiMergeOutputs:
    """
    cifti-merge by Washington University School of Medicin.
    
    MERGE OR SPLIT ON SERIES, SCALAR, OR LABEL DIMENSIONS.
    
    Given input CIFTI files for which mappings along the selected direction are
    the same type, all either series, scalars, or labels, and the other
    dimensions are index-compatible, this command concatenates the data in the
    specified indices/ranges along the selected direction (by default, on
    typical 2D cifti, concatenate horizontally, so rows become longer). The
    direction can be either an integer starting from 1, or the strings 'ROW' or
    'COLUMN'.
    
    Example: wb_command -cifti-merge out.dtseries.nii -cifti first.dtseries.nii
    -index 1 -cifti second.dtseries.nii
    
    This example would take the first column from first.dtseries.nii, followed
    by all columns from second.dtseries.nii, and write these columns to
    out.dtseries.nii. .
    
    Args:
        cifti_out: output cifti file
        opt_direction_direction: merge in a direction other than along rows: the
            dimension to split/concatenate along, default ROW
        opt_mem_limit_limit_gb: restrict memory used for file reading
            efficiency: memory limit in gigabytes
        opt_cifti_cifti_in: specify an input cifti file: a cifti file to use
            data from
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge")
    cargs.append(execution.input_file(cifti_out))
    if opt_direction_direction is not None:
        cargs.extend(["-direction", opt_direction_direction])
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    if opt_cifti_cifti_in is not None:
        cargs.extend(["-cifti", execution.input_file(opt_cifti_cifti_in)])
    ret = CiftiMergeOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_MERGE_METADATA",
    "CiftiMergeOutputs",
    "cifti_merge",
]