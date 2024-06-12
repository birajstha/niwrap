# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MERGE_MRS_REPORTS_METADATA = Metadata(
    id="8fbcb7a07a605e31c1bd215f45edc0302e2184f9",
    name="merge_mrs_reports",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl/merge-mrs-reports:latest",
)


class MergeMrsReportsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `merge_mrs_reports(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    merged_output_file: OutputPathType | None
    """Merged HTML report"""


def merge_mrs_reports(
    input_files: list[InputPathType],
    dataset_description: str,
    output_folder: str | None = None,
    output_filename: str | None = None,
    delete_flag: bool = False,
    runner: Runner = None,
) -> MergeMrsReportsOutputs:
    """
    merge_mrs_reports by FSL.
    
    FSL Magnetic Resonance Spectroscopy - Merge HTML reports based on filename
    in directory.
    
    Args:
        input_files: List of input files.
        dataset_description: Dataset description.
        output_folder: Output folder (default=current directory).
        output_filename: Output filename (default=mergedReports.html).
        delete_flag: Delete files after successful merge.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MergeMrsReportsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MERGE_MRS_REPORTS_METADATA)
    cargs = []
    cargs.append("merge_mrs_reports")
    cargs.extend([execution.input_file(f) for f in input_files])
    cargs.append("--description")
    cargs.extend(["-d", dataset_description])
    if output_folder is not None:
        cargs.extend(["-o", output_folder])
    if output_filename is not None:
        cargs.extend(["-f", output_filename])
    if delete_flag:
        cargs.append("--delete")
    ret = MergeMrsReportsOutputs(
        root=execution.output_file("."),
        merged_output_file=execution.output_file(f"{output_folder}/{output_filename}", optional=True) if output_folder is not None and output_filename is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MERGE_MRS_REPORTS_METADATA",
    "MergeMrsReportsOutputs",
    "merge_mrs_reports",
]
