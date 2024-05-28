# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


CIFTI_CONVERT_METADATA = Metadata(
    id="54dd9c58ecf9499b7fc53b46eb368125bedb9e65",
    name="cifti-convert",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiConvertToGiftiExt:
    """
    convert to GIFTI external binary
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
class CiftiConvertResetTimepoints:
    """
    reset the mapping along rows to timepoints, taking length from the gifti file
    """
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
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
        if self.opt_unit_unit is not None:
            cargs.extend(["-unit", self.opt_unit_unit])
        return cargs


@dataclasses.dataclass
class CiftiConvertReplaceBinary:
    """
    replace data with a binary file
    """
    opt_flip_endian: bool = False
    """byteswap the binary file"""
    opt_transpose: bool = False
    """transpose the binary file"""
    
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
        if self.opt_flip_endian:
            cargs.append("-flip-endian")
        if self.opt_transpose:
            cargs.append("-transpose")
        return cargs


@dataclasses.dataclass
class CiftiConvertFromGiftiExt:
    """
    convert a GIFTI made with this command back into a CIFTI
    """
    cifti_out: InputPathType
    """the output cifti file"""
    reset_timepoints: CiftiConvertResetTimepoints | None = None
    """reset the mapping along rows to timepoints, taking length from the gifti
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the gifti file"""
    opt_column_reset_scalars: bool = False
    """reset mapping along columns to scalar (useful for changing number of
    series in a sdseries file)"""
    replace_binary: CiftiConvertReplaceBinary | None = None
    """replace data with a binary file"""
    
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
        cargs.append(execution.input_file(self.cifti_out))
        if self.reset_timepoints is not None:
            cargs.extend(["-reset-timepoints", *self.reset_timepoints.run(execution)])
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        if self.opt_column_reset_scalars:
            cargs.append("-column-reset-scalars")
        if self.replace_binary is not None:
            cargs.extend(["-replace-binary", *self.replace_binary.run(execution)])
        return cargs


@dataclasses.dataclass
class CiftiConvertToNifti:
    """
    convert to NIFTI1
    """
    nifti_out: InputPathType
    """the output nifti file"""
    opt_smaller_file: bool = False
    """use better-fitting dimension lengths"""
    opt_smaller_dims: bool = False
    """minimize the largest dimension, for tools that don't like large
    indices"""
    
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
        cargs.append(execution.input_file(self.nifti_out))
        if self.opt_smaller_file:
            cargs.append("-smaller-file")
        if self.opt_smaller_dims:
            cargs.append("-smaller-dims")
        return cargs


@dataclasses.dataclass
class CiftiConvertResetTimepoints:
    """
    reset the mapping along rows to timepoints, taking length from the nifti file
    """
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
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
        if self.opt_unit_unit is not None:
            cargs.extend(["-unit", self.opt_unit_unit])
        return cargs


@dataclasses.dataclass
class CiftiConvertFromNifti:
    """
    convert a NIFTI (1 or 2) file made with this command back into CIFTI
    """
    cifti_out: InputPathType
    """the output cifti file"""
    reset_timepoints: CiftiConvertResetTimepoints | None = None
    """reset the mapping along rows to timepoints, taking length from the nifti
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the nifti file"""
    
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
        cargs.append(execution.input_file(self.cifti_out))
        if self.reset_timepoints is not None:
            cargs.extend(["-reset-timepoints", *self.reset_timepoints.run(execution)])
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        return cargs


@dataclasses.dataclass
class CiftiConvertToText:
    """
    convert to a plain text file
    """
    opt_col_delim_delim_string: str | None = None
    """choose string to put between elements in a row: the string to use
    (default is a tab character)"""
    
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
        if self.opt_col_delim_delim_string is not None:
            cargs.extend(["-col-delim", self.opt_col_delim_delim_string])
        return cargs


@dataclasses.dataclass
class CiftiConvertResetTimepoints:
    """
    reset the mapping along rows to timepoints, taking length from the text file
    """
    opt_unit_unit: str | None = None
    """use a unit other than time: unit identifier (default SECOND)"""
    
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
        if self.opt_unit_unit is not None:
            cargs.extend(["-unit", self.opt_unit_unit])
        return cargs


@dataclasses.dataclass
class CiftiConvertFromText:
    """
    convert from plain text to cifti
    """
    cifti_out: InputPathType
    """the output cifti file"""
    opt_col_delim_delim_string: str | None = None
    """specify string that is between elements in a row: the string to use
    (default is any whitespace)"""
    reset_timepoints: CiftiConvertResetTimepoints | None = None
    """reset the mapping along rows to timepoints, taking length from the text
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the text file"""
    
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
        cargs.append(execution.input_file(self.cifti_out))
        if self.opt_col_delim_delim_string is not None:
            cargs.extend(["-col-delim", self.opt_col_delim_delim_string])
        if self.reset_timepoints is not None:
            cargs.extend(["-reset-timepoints", *self.reset_timepoints.run(execution)])
        if self.opt_reset_scalars:
            cargs.append("-reset-scalars")
        return cargs


class CiftiConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_convert(
    to_gifti_ext: CiftiConvertToGiftiExt | None = None,
    from_gifti_ext: CiftiConvertFromGiftiExt | None = None,
    to_nifti: CiftiConvertToNifti | None = None,
    from_nifti: CiftiConvertFromNifti | None = None,
    to_text: CiftiConvertToText | None = None,
    from_text: CiftiConvertFromText | None = None,
    runner: Runner = None,
) -> CiftiConvertOutputs:
    """
    cifti-convert by Washington University School of Medicin.
    
    Dump cifti matrix into other formats.
    
    This command is used to convert a full CIFTI matrix to/from formats that can
    be used by programs that don't understand CIFTI. You must specify exactly
    one of -to-gifti-ext, -from-gifti-ext, -to-nifti, -from-nifti, -to-text, or
    -from-text.
    
    If you want to write an existing CIFTI file with a different CIFTI version,
    see -file-convert, and its -cifti-version-convert option.
    
    If you want part of the CIFTI file as a metric, label, or volume file, see
    -cifti-separate. If you want to create a CIFTI file from metric and/or
    volume files, see the -cifti-create-* commands.
    
    If you want to import a matrix that is restricted to an ROI, first create a
    template CIFTI file matching that ROI using a -cifti-create-* command. After
    importing to CIFTI, you can then expand the file into a standard
    brainordinates space with -cifti-create-dense-from-template. If you want to
    export only part of a CIFTI file, first create an roi-restricted CIFTI file
    with -cifti-restrict-dense-mapping.
    
    The -transpose option to -from-gifti-ext is needed if the replacement binary
    file is in column-major order.
    
    The -unit options accept these values:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Args:
        to_gifti_ext: convert to GIFTI external binary
        from_gifti_ext: convert a GIFTI made with this command back into a CIFTI
        to_nifti: convert to NIFTI1
        from_nifti: convert a NIFTI (1 or 2) file made with this command back
            into CIFTI
        to_text: convert to a plain text file
        from_text: convert from plain text to cifti
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-convert")
    if to_gifti_ext is not None:
        cargs.extend(["-to-gifti-ext", *to_gifti_ext.run(execution)])
    if from_gifti_ext is not None:
        cargs.extend(["-from-gifti-ext", *from_gifti_ext.run(execution)])
    if to_nifti is not None:
        cargs.extend(["-to-nifti", *to_nifti.run(execution)])
    if from_nifti is not None:
        cargs.extend(["-from-nifti", *from_nifti.run(execution)])
    if to_text is not None:
        cargs.extend(["-to-text", *to_text.run(execution)])
    if from_text is not None:
        cargs.extend(["-from-text", *from_text.run(execution)])
    ret = CiftiConvertOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CONVERT_METADATA",
    "CiftiConvertFromGiftiExt",
    "CiftiConvertFromNifti",
    "CiftiConvertFromText",
    "CiftiConvertOutputs",
    "CiftiConvertReplaceBinary",
    "CiftiConvertResetTimepoints",
    "CiftiConvertResetTimepoints",
    "CiftiConvertResetTimepoints",
    "CiftiConvertToGiftiExt",
    "CiftiConvertToNifti",
    "CiftiConvertToText",
    "cifti_convert",
]
