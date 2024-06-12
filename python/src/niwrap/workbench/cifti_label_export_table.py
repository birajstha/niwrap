# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

CIFTI_LABEL_EXPORT_TABLE_METADATA = Metadata(
    id="612ca61b4ba12319d159b362f67119fef7cf0f1c",
    name="cifti-label-export-table",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiLabelExportTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_label_export_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_label_export_table(
    label_in: InputPathType,
    map_: str,
    table_out: str,
    runner: Runner = None,
) -> CiftiLabelExportTableOutputs:
    """
    cifti-label-export-table by Washington University School of Medicin.
    
    Export label table from cifti as text.
    
    Takes the label table from the cifti label map, and writes it to a text
    format matching what is expected by -cifti-label-import.
    
    Args:
        label_in: the input cifti label file.
        map_: the number or name of the label map to use.
        table_out: output - the output text file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiLabelExportTableOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_LABEL_EXPORT_TABLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-label-export-table")
    cargs.append(execution.input_file(label_in))
    cargs.append(map_)
    cargs.append(table_out)
    ret = CiftiLabelExportTableOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_LABEL_EXPORT_TABLE_METADATA",
    "CiftiLabelExportTableOutputs",
    "cifti_label_export_table",
]
