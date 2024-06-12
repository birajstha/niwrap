# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FILE_CONVERT_METADATA = Metadata(
    id="d1e1f2779836a93aec5a47c4c2886f34fca369b9",
    name="file-convert",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class FileConvertBorderVersionConvert:
    """
    write a border file with a different version
    """
    opt_surface_surface: InputPathType | None = None
    """must be specified if the input is version 1: use this surface file for
    structure and number of vertices, ignore borders on other structures"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_surface_surface is not None:
            cargs.extend(["-surface", execution.input_file(self.opt_surface_surface)])
        return cargs


@dataclasses.dataclass
class FileConvertNiftiVersionConvert:
    """
    write a nifti file with a different version
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


@dataclasses.dataclass
class FileConvertCiftiVersionConvert:
    """
    write a cifti file with a different version
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class FileConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `file_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def file_convert(
    border_version_convert: FileConvertBorderVersionConvert | None = None,
    nifti_version_convert: FileConvertNiftiVersionConvert | None = None,
    cifti_version_convert: FileConvertCiftiVersionConvert | None = None,
    runner: Runner = None,
) -> FileConvertOutputs:
    """
    file-convert by Washington University School of Medicin.
    
    Change version of file format.
    
    You may only specify one top-level option.
    
    Args:
        border_version_convert: write a border file with a different version.
        nifti_version_convert: write a nifti file with a different version.
        cifti_version_convert: write a cifti file with a different version.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FileConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FILE_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-file-convert")
    if border_version_convert is not None:
        cargs.extend(["-border-version-convert", *border_version_convert.run(execution)])
    if nifti_version_convert is not None:
        cargs.extend(["-nifti-version-convert", *nifti_version_convert.run(execution)])
    if cifti_version_convert is not None:
        cargs.extend(["-cifti-version-convert", *cifti_version_convert.run(execution)])
    ret = FileConvertOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FILE_CONVERT_METADATA",
    "FileConvertBorderVersionConvert",
    "FileConvertCiftiVersionConvert",
    "FileConvertNiftiVersionConvert",
    "FileConvertOutputs",
    "file_convert",
]
