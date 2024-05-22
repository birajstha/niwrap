# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_ALL_LABELS_TO_ROIS_METADATA = Metadata(
    id="971fab6c3f79f23c354f23fd982c5ba7a4a7238b",
    name="cifti-all-labels-to-rois",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiAllLabelsToRoisOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_all_labels_to_rois(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_all_labels_to_rois(
    label_in: InputPathType,
    map_: str,
    cifti_out: InputPathType,
    runner: Runner = None,
) -> CiftiAllLabelsToRoisOutputs:
    """
    cifti-all-labels-to-rois by Washington University School of Medicin.
    
    MAKE ROIS FROM ALL LABELS IN A CIFTI LABEL MAP.
    
    The output cifti file is a dscalar file with a column (map) for each label
    in the specified input map, other than the ??? label, each of which contains
    a binary ROI of all brainordinates that are set to the corresponding label.
    
    Most of the time, specifying '1' for the <map> argument will do what is
    desired.
    
    Args:
        label_in: the input cifti label file
        map_: the number or name of the label map to use
        cifti_out: the output cifti file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiAllLabelsToRoisOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ALL_LABELS_TO_ROIS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-all-labels-to-rois")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(execution.input_file(cifti_out))
    ret = CiftiAllLabelsToRoisOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ALL_LABELS_TO_ROIS_METADATA",
    "CiftiAllLabelsToRoisOutputs",
    "cifti_all_labels_to_rois",
]
