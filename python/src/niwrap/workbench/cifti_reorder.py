# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CIFTI_REORDER_METADATA = Metadata(
    id="0524822039be62e4fa7e64df14c1370d49ab9288",
    name="cifti-reorder",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiReorderOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_reorder(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the reordered cifti file"""


def cifti_reorder(
    cifti_in: InputPathType,
    direction: str,
    reorder_list: str,
    cifti_out: InputPathType,
    runner: Runner = None,
) -> CiftiReorderOutputs:
    """
    cifti-reorder by Washington University School of Medicin.
    
    Reorder the parcels or scalar/label maps in a cifti file.
    
    The mapping along the specified direction must be parcels, scalars, or
    labels. For pscalar or ptseries, use COLUMN to reorder the parcels. For
    dlabel, use ROW. The <reorder-list> file must contain 1-based indices
    separated by whitespace (spaces, newlines, tabs, etc), with as many indices
    as <cifti-in> has along the specified dimension. These indices specify which
    current index should end up in that position, for instance, if the current
    order is 'A B C D', and the desired order is 'D A B C', the text file should
    contain '4 1 2 3'.
    
    Args:
        cifti_in: input cifti file.
        direction: which dimension to reorder along, ROW or COLUMN.
        reorder_list: a text file containing the desired order transformation.
        cifti_out: the reordered cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiReorderOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_REORDER_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-reorder")
    cargs.append(execution.input_file(cifti_in))
    cargs.append(direction)
    cargs.append(reorder_list)
    cargs.append(execution.input_file(cifti_out))
    ret = CiftiReorderOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_REORDER_METADATA",
    "CiftiReorderOutputs",
    "cifti_reorder",
]
