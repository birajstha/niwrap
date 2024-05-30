# This file was auto generated by Styx.
# Do not edit this file directly.

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


class ToGiftiExtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ToGiftiExt.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ToGiftiExt:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ToGiftiExtOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ToGiftiExtOutputs`).
        """
        ret = ToGiftiExtOutputs(
            root=execution.output_file("."),
        )
        return ret


class ResetTimepointsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ResetTimepoints.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ResetTimepoints:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ResetTimepointsOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ResetTimepointsOutputs`).
        """
        ret = ResetTimepointsOutputs(
            root=execution.output_file("."),
        )
        return ret


class ReplaceBinaryOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ReplaceBinary.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ReplaceBinary:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ReplaceBinaryOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ReplaceBinaryOutputs`).
        """
        ret = ReplaceBinaryOutputs(
            root=execution.output_file("."),
        )
        return ret


class FromGiftiExtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `FromGiftiExt.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""
    self.reset_timepoints: ResetTimepointsOutputs
    """Subcommand outputs"""
    self.replace_binary: ReplaceBinaryOutputs
    """Subcommand outputs"""


@dataclasses.dataclass
class FromGiftiExt:
    """
    convert a GIFTI made with this command back into a CIFTI
    """
    cifti_out: InputPathType
    """the output cifti file"""
    reset_timepoints: ResetTimepoints | None = None
    """reset the mapping along rows to timepoints, taking length from the gifti
    file"""
    opt_reset_scalars: bool = False
    """reset mapping along rows to scalars, taking length from the gifti file"""
    opt_column_reset_scalars: bool = False
    """reset mapping along columns to scalar (useful for changing number of
    series in a sdseries file)"""
    replace_binary: ReplaceBinary | None = None
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> FromGiftiExtOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `FromGiftiExtOutputs`).
        """
        ret = FromGiftiExtOutputs(
            root=execution.output_file("."),
            cifti_out=execution.output_file(f"{pathlib.Path(self.cifti_out).name}"),
            self.reset_timepoints=self.reset_timepoints.outputs(execution),
            self.replace_binary=self.replace_binary.outputs(execution),
        )
        return ret


class ToNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ToNifti.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    nifti_out: OutputPathType
    """the output nifti file"""


@dataclasses.dataclass
class ToNifti:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ToNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ToNiftiOutputs`).
        """
        ret = ToNiftiOutputs(
            root=execution.output_file("."),
            nifti_out=execution.output_file(f"{pathlib.Path(self.nifti_out).name}"),
        )
        return ret


class ResetTimepointsOutputs_(typing.NamedTuple):
    """
    Output object returned when calling `ResetTimepoints_.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ResetTimepoints_:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ResetTimepointsOutputs_:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ResetTimepointsOutputs_`).
        """
        ret = ResetTimepointsOutputs_(
            root=execution.output_file("."),
        )
        return ret


class FromNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `FromNifti.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out_: OutputPathType
    """the output cifti file"""
    self.reset_timepoints: ResetTimepointsOutputs_
    """Subcommand outputs"""


@dataclasses.dataclass
class FromNifti:
    """
    convert a NIFTI (1 or 2) file made with this command back into CIFTI
    """
    cifti_out: InputPathType
    """the output cifti file"""
    reset_timepoints: ResetTimepoints_ | None = None
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> FromNiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `FromNiftiOutputs`).
        """
        ret = FromNiftiOutputs(
            root=execution.output_file("."),
            cifti_out_=execution.output_file(f"{pathlib.Path(self.cifti_out).name}"),
            self.reset_timepoints=self.reset_timepoints.outputs(execution),
        )
        return ret


class ToTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ToText.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ToText:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ToTextOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ToTextOutputs`).
        """
        ret = ToTextOutputs(
            root=execution.output_file("."),
        )
        return ret


class ResetTimepointsOutputs_2(typing.NamedTuple):
    """
    Output object returned when calling `ResetTimepoints_2.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class ResetTimepoints_2:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ResetTimepointsOutputs_2:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ResetTimepointsOutputs_2`).
        """
        ret = ResetTimepointsOutputs_2(
            root=execution.output_file("."),
        )
        return ret


class FromTextOutputs(typing.NamedTuple):
    """
    Output object returned when calling `FromText.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out_2: OutputPathType
    """the output cifti file"""
    self.reset_timepoints: ResetTimepointsOutputs_2
    """Subcommand outputs"""


@dataclasses.dataclass
class FromText:
    """
    convert from plain text to cifti
    """
    cifti_out: InputPathType
    """the output cifti file"""
    opt_col_delim_delim_string: str | None = None
    """specify string that is between elements in a row: the string to use
    (default is any whitespace)"""
    reset_timepoints: ResetTimepoints_2 | None = None
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> FromTextOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `FromTextOutputs`).
        """
        ret = FromTextOutputs(
            root=execution.output_file("."),
            cifti_out_2=execution.output_file(f"{pathlib.Path(self.cifti_out).name}"),
            self.reset_timepoints=self.reset_timepoints.outputs(execution),
        )
        return ret


class CiftiConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    to_gifti_ext: ToGiftiExtOutputs
    """Subcommand outputs"""
    from_gifti_ext: FromGiftiExtOutputs
    """Subcommand outputs"""
    to_nifti: ToNiftiOutputs
    """Subcommand outputs"""
    from_nifti: FromNiftiOutputs
    """Subcommand outputs"""
    to_text: ToTextOutputs
    """Subcommand outputs"""
    from_text: FromTextOutputs
    """Subcommand outputs"""


def cifti_convert(
    to_gifti_ext: ToGiftiExt | None = None,
    from_gifti_ext: FromGiftiExt | None = None,
    to_nifti: ToNifti | None = None,
    from_nifti: FromNifti | None = None,
    to_text: ToText | None = None,
    from_text: FromText | None = None,
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
        to_gifti_ext=to_gifti_ext.outputs(execution),
        from_gifti_ext=from_gifti_ext.outputs(execution),
        to_nifti=to_nifti.outputs(execution),
        from_nifti=from_nifti.outputs(execution),
        to_text=to_text.outputs(execution),
        from_text=from_text.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CONVERT_METADATA",
    "CiftiConvertOutputs",
    "FromGiftiExt",
    "FromGiftiExtOutputs",
    "FromNifti",
    "FromNiftiOutputs",
    "FromText",
    "FromTextOutputs",
    "ReplaceBinary",
    "ReplaceBinaryOutputs",
    "ResetTimepoints",
    "ResetTimepointsOutputs",
    "ResetTimepointsOutputs_",
    "ResetTimepointsOutputs_2",
    "ResetTimepoints_",
    "ResetTimepoints_2",
    "ToGiftiExt",
    "ToGiftiExtOutputs",
    "ToNifti",
    "ToNiftiOutputs",
    "ToText",
    "ToTextOutputs",
    "cifti_convert",
]
