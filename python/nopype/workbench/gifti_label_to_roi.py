# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:55.919809

import typing

from ..styxdefs import *


GIFTI_LABEL_TO_ROI_METADATA = Metadata(
    id="4ac6d01d43e14cd0825e0f573af2974e90b8be9f",
    name="gifti-label-to-roi",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class GiftiLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_label_to_roi(...)`.
    """
    metric_out: OutputPathType
    """the output metric file"""


def gifti_label_to_roi(
    runner: Runner,
    label_in: InputPathType,
    metric_out: InputPathType,
    opt_name_label_name: str | None = None,
    opt_key_label_key: float | int | None = None,
    opt_map_map: str | None = None,
) -> GiftiLabelToRoiOutputs:
    """
    MAKE A GIFTI LABEL INTO AN ROI METRIC.
    
    For each map in <label-in>, a map is created in <metric-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Args:
        runner: Command runner
        label_in: the input gifti label file
        metric_out: the output metric file
        opt_name_label_name: select label by name: the label name that you want
            an roi of
        opt_key_label_key: select label by key: the label key that you want an
            roi of
        opt_map_map: select a single label map to use: the map number or name
    Returns:
        NamedTuple of outputs (described in `GiftiLabelToRoiOutputs`).
    """
    execution = runner.start_execution(GIFTI_LABEL_TO_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-gifti-label-to-roi")
    cargs.append(execution.input_file(label_in))
    cargs.append(execution.input_file(metric_out))
    if opt_name_label_name is not None:
        cargs.extend(["-name", opt_name_label_name])
    if opt_key_label_key is not None:
        cargs.extend(["-key", str(opt_key_label_key)])
    if opt_map_map is not None:
        cargs.extend(["-map", opt_map_map])
    ret = GiftiLabelToRoiOutputs(
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret