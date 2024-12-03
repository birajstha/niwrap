# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRI_PATH2LABEL_METADATA = Metadata(
    id="ac055539c26e5fa7d5b552e4523192ffbd1a7979.boutiques",
    name="mri_path2label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MriPath2labelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mri_path2label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mri_path2label(
    input_file: str,
    output_file: str,
    single: bool = False,
    path_to_label: bool = False,
    label_to_path: bool = False,
    connect: list[str] | None = None,
    fill: list[str] | None = None,
    confillx: list[str] | None = None,
    confill: list[str] | None = None,
    source_file: str | None = None,
    dest_file: str | None = None,
    runner: Runner | None = None,
) -> MriPath2labelOutputs:
    """
    Converts a path file to a label or a label file to a path file.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_file: Input file, either a path or label file.
        output_file: Output file, either a path or label file.
        single: Only convert a single path, and do not use sentinel values.
        path_to_label: Treat input as a path and output a label.
        label_to_path: Treat input as a label and output a path.
        connect: Connect path; input and output must be paths; requires subject\
            and hemi.
        fill: Fill already closed, connected path; input must be a path, output\
            must be a label; requires subject, hemi, and seedvtx.
        confillx: Connect and fill path; input must be a path, output must be a\
            label; requires surface_fname and seedvtx.
        confill: Connect and fill path; input must be a path, output must be a\
            label; requires subject, hemi, and seedvtx.
        source_file: The path file, if path2label.
        dest_file: The label file, if path2label.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MriPath2labelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRI_PATH2LABEL_METADATA)
    cargs = []
    cargs.append("mri_path2label")
    cargs.append(input_file)
    cargs.append(output_file)
    if single:
        cargs.append("--single")
    if path_to_label:
        cargs.append("--path2label")
    if label_to_path:
        cargs.append("--label2path")
    if connect is not None:
        cargs.extend([
            "--connect",
            *connect
        ])
    if fill is not None:
        cargs.extend([
            "--fill",
            *fill
        ])
    if confillx is not None:
        cargs.extend([
            "--confillx",
            *confillx
        ])
    if confill is not None:
        cargs.extend([
            "--confill",
            *confill
        ])
    if source_file is not None:
        cargs.extend([
            "--i",
            source_file
        ])
    if dest_file is not None:
        cargs.extend([
            "--o",
            dest_file
        ])
    ret = MriPath2labelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRI_PATH2LABEL_METADATA",
    "MriPath2labelOutputs",
    "mri_path2label",
]