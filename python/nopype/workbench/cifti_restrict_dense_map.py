# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


CIFTI_RESTRICT_DENSE_MAP_METADATA = Metadata(
    id="6ddb386b0d5115f7c0e0f30bc0393135818f3b3b",
    name="cifti-restrict-dense-map",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiRestrictDenseMapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_restrict_dense_map(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_restrict_dense_map(
    runner: Runner,
    cifti_in: InputPathType,
    direction: str,
    cifti_out: InputPathType,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_left_roi_roi_metric: InputPathType | None = None,
    opt_right_roi_roi_metric: InputPathType | None = None,
    opt_cerebellum_roi_roi_metric: InputPathType | None = None,
    opt_vol_roi_roi_vol: InputPathType | None = None,
) -> CiftiRestrictDenseMapOutputs:
    """
    EXCLUDE BRAINORDINATES FROM A CIFTI FILE.
    
    Writes a modified version of <cifti-in>, where all brainordinates outside
    the specified roi(s) are removed from the file. The direction can be either
    an integer starting from 1, or the strings 'ROW' or 'COLUMN'. If -cifti-roi
    is specified, no other -*-roi option may be specified. If not using
    -cifti-roi, any -*-roi options not present will discard the relevant
    structure, if present in the input file.
    
    Args:
        runner: Command runner
        cifti_in: the input cifti
        direction: which dimension to change the mapping on (integer, 'ROW', or
            'COLUMN')
        cifti_out: the output cifti
        opt_cifti_roi_roi_cifti: cifti file containing combined rois: the rois
            as a cifti file
        opt_left_roi_roi_metric: vertices to use from left hemisphere: the left
            roi as a metric file
        opt_right_roi_roi_metric: vertices to use from right hemisphere: the
            right roi as a metric file
        opt_cerebellum_roi_roi_metric: vertices to use from cerebellum: the
            cerebellum roi as a metric file
        opt_vol_roi_roi_vol: voxels to use: the roi volume file
    Returns:
        NamedTuple of outputs (described in `CiftiRestrictDenseMapOutputs`).
    """
    execution = runner.start_execution(CIFTI_RESTRICT_DENSE_MAP_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-restrict-dense-map")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
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
    ret = CiftiRestrictDenseMapOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).stem}"),
    )
    execution.run(cargs)
    return ret
