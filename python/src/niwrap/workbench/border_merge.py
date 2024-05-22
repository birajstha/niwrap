# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


BORDER_MERGE_METADATA = Metadata(
    id="6d7ba65f1288a94a0839d6e889f94fd5f9b5fe03",
    name="border-merge",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class BorderMergeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `border_merge(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    border_file_out: OutputPathType
    """the output border file"""


def border_merge(
    border_file_out: InputPathType,
    opt_border_border_file_in: InputPathType | None = None,
    runner: Runner = None,
) -> BorderMergeOutputs:
    """
    border-merge by Washington University School of Medicin.
    
    MERGE BORDER FILES INTO A NEW FILE.
    
    Takes one or more border files and makes a new border file from the borders
    in them.
    
    Example: wb_command -border-merge out.border -border first.border -select 1
    -border second.border
    
    This example would take the first border from first.border, followed by all
    borders from second.border, and write these to out.border.
    
    Args:
        border_file_out: the output border file
        opt_border_border_file_in: specify an input border file: a border file
            to use borders from
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `BorderMergeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BORDER_MERGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-border-merge")
    cargs.append(execution.input_file(border_file_out))
    if opt_border_border_file_in is not None:
        cargs.extend(["-border", execution.input_file(opt_border_border_file_in)])
    ret = BorderMergeOutputs(
        root=execution.output_file("."),
        border_file_out=execution.output_file(f"{pathlib.Path(border_file_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BORDER_MERGE_METADATA",
    "BorderMergeOutputs",
    "border_merge",
]
