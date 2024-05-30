# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


CIFTI_ROI_AVERAGE_METADATA = Metadata(
    id="bd3ef39d6435b0868a5924ccc4268c09a881c62f",
    name="cifti-roi-average",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiRoiAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_roi_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_roi_average(
    cifti_in: InputPathType,
    text_out: str,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
    runner: Runner = None,
) -> CiftiRoiAverageOutputs:
    """
    cifti-roi-average by Washington University School of Medicin.
    
    Average rows in a single cifti file.
    
    Average the rows that are within the specified ROIs, and write the resulting
    average row to a text file, separated by newlines. If -cifti-roi is
    specified, -left-roi, -right-roi, -cerebellum-roi, and -vol-roi must not be
    specified.
    
    Args:
        cifti_in: the cifti file to average rows from
        text_out: output text file of the average values
        opt_cifti_roi_roi_cifti: cifti file containing combined rois: the rois
            as a cifti file
        opt_left_roi_roi_metric: vertices to use from left hemisphere: the left
            roi as a metric file
        opt_right_roi_roi_metric: vertices to use from right hemisphere: the
            right roi as a metric file
        opt_cerebellum_roi_roi_metric: vertices to use from cerebellum: the
            cerebellum roi as a metric file
        opt_vol_roi_roi_vol: voxels to use: the roi volume file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiRoiAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_ROI_AVERAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-roi-average")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(text_out)
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_left_roi_roi_metric is not None:
        cargs.extend(["-left-roi", execution.input_file(opt_left_roi_roi_metric)])
    if opt_right_roi_roi_metric is not None:
        cargs.extend(["-right-roi", execution.input_file(opt_right_roi_roi_metric)])
    if opt_cerebellum_roi_roi_metric is not None:
        cargs.extend(["-cerebellum-roi", execution.input_file(opt_cerebellum_roi_roi_metric)])
    if opt_vol_roi_roi_vol is not None:
        cargs.extend(["-vol-roi", execution.input_file(opt_vol_roi_roi_vol)])
    ret = CiftiRoiAverageOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_ROI_AVERAGE_METADATA",
    "CiftiRoiAverageOutputs",
    "cifti_roi_average",
]
