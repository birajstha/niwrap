# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SPEC_FILE_RELOCATE_METADATA = Metadata(
    id="afbe63530dfcccb2fb3fd8719bb8ab0f90b52c87",
    name="spec-file-relocate",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SpecFileRelocateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `spec_file_relocate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def spec_file_relocate(
    input_spec: str,
    output_spec: str,
    runner: Runner = None,
) -> SpecFileRelocateOutputs:
    """
    spec-file-relocate by Washington University School of Medicin.
    
    Recreate spec file in new location.
    
    Spec files contain internal relative paths, such that moving or copying a
    spec file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the spec file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Args:
        input_spec: the spec file to use.
        output_spec: output - the new spec file to create.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SpecFileRelocateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SPEC_FILE_RELOCATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-spec-file-relocate")
    cargs.append(input_spec)
    cargs.append(output_spec)
    ret = SpecFileRelocateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SPEC_FILE_RELOCATE_METADATA",
    "SpecFileRelocateOutputs",
    "spec_file_relocate",
]
