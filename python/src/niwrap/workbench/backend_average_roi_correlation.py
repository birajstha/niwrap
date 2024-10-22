# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BACKEND_AVERAGE_ROI_CORRELATION_METADATA = Metadata(
    id="9e4134b170426222af03ea3002f52fa4de97b447.boutiques",
    name="backend-average-roi-correlation",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class BackendAverageRoiCorrelationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `backend_average_roi_correlation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def backend_average_roi_correlation(
    index_list: str,
    out_file: str,
    runner: Runner | None = None,
) -> BackendAverageRoiCorrelationOutputs:
    """
    Connectome db backend command for cifti average roi correlation.
    
    This command is probably not the one you are looking for, try
    -cifti-average-roi-correlation. It takes the list of cifti files to average
    from standard input, and writes its output as little endian, 32-bit integer
    of row size followed by the row as 32-bit floats.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        index_list: comma separated list of cifti indexes to average and then\
            correlate.
        out_file: file to write the average row to.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BackendAverageRoiCorrelationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BACKEND_AVERAGE_ROI_CORRELATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-backend-average-roi-correlation")
    cargs.append(index_list)
    cargs.append(out_file)
    ret = BackendAverageRoiCorrelationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BACKEND_AVERAGE_ROI_CORRELATION_METADATA",
    "BackendAverageRoiCorrelationOutputs",
    "backend_average_roi_correlation",
]
