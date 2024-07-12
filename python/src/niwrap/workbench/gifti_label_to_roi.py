# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

GIFTI_LABEL_TO_ROI_METADATA = Metadata(
    id="f8957a62616930c7c9602d4f31ffab1bee8ebbec",
    name="gifti-label-to-roi",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class GiftiLabelToRoiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `gifti_label_to_roi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    metric_out: OutputPathType
    """the output metric file"""


def gifti_label_to_roi(
    label_in: InputPathType,
    metric_out: str,
    opt_name_label_name: str | None = None,
    opt_key_label_key: int | None = None,
    opt_map_map: str | None = None,
    runner: Runner | None = None,
) -> GiftiLabelToRoiOutputs:
    """
    gifti-label-to-roi by Washington University School of Medicin.
    
    Make a gifti label into an roi metric.
    
    For each map in <label-in>, a map is created in <metric-out> where all
    locations labeled with <label-name> or with a key of <label-key> are given a
    value of 1, and all other locations are given 0. Exactly one of -name and
    -key must be specified. Specify -map to use only one map from <label-in>.
    
    Args:
        label_in: the input gifti label file.
        metric_out: the output metric file.
        opt_name_label_name: select label by name: the label name that you want\
            an roi of.
        opt_key_label_key: select label by key: the label key that you want an\
            roi of.
        opt_map_map: select a single label map to use: the map number or name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GiftiLabelToRoiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GIFTI_LABEL_TO_ROI_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-gifti-label-to-roi")
    cargs.append(execution.input_file(label_in))
    cargs.append(metric_out)
    if opt_name_label_name is not None:
        cargs.extend(["-name", opt_name_label_name])
    if opt_key_label_key is not None:
        cargs.extend(["-key", str(opt_key_label_key)])
    if opt_map_map is not None:
        cargs.extend(["-map", opt_map_map])
    ret = GiftiLabelToRoiOutputs(
        root=execution.output_file("."),
        metric_out=execution.output_file(f"{metric_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GIFTI_LABEL_TO_ROI_METADATA",
    "GiftiLabelToRoiOutputs",
    "gifti_label_to_roi",
]
