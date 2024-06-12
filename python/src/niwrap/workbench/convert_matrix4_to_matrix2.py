# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CONVERT_MATRIX4_TO_MATRIX2_METADATA = Metadata(
    id="daa956f5e14a27f9a3d2c41fefb567999a9fff22",
    name="convert-matrix4-to-matrix2",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ConvertMatrix4ToMatrix2IndividualFibersOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ConvertMatrix4ToMatrix2IndividualFibers.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fiber_1: OutputPathType
    """output file for first fiber"""
    fiber_2: OutputPathType
    """output file for second fiber"""
    fiber_3: OutputPathType
    """output file for third fiber"""


@dataclasses.dataclass
class ConvertMatrix4ToMatrix2IndividualFibers:
    """
    output files for each fiber direction
    """
    fiber_1: InputPathType
    """output file for first fiber"""
    fiber_2: InputPathType
    """output file for second fiber"""
    fiber_3: InputPathType
    """output file for third fiber"""
    
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
        cargs.append(execution.input_file(self.fiber_1))
        cargs.append(execution.input_file(self.fiber_2))
        cargs.append(execution.input_file(self.fiber_3))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConvertMatrix4ToMatrix2IndividualFibersOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConvertMatrix4ToMatrix2IndividualFibersOutputs`).
        """
        ret = ConvertMatrix4ToMatrix2IndividualFibersOutputs(
            root=execution.output_file("."),
            fiber_1=execution.output_file(f"{pathlib.Path(self.fiber_1).name}"),
            fiber_2=execution.output_file(f"{pathlib.Path(self.fiber_2).name}"),
            fiber_3=execution.output_file(f"{pathlib.Path(self.fiber_3).name}"),
        )
        return ret


class ConvertMatrix4ToMatrix2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_matrix4_to_matrix2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    counts_out: OutputPathType
    """the total fiber counts, as a cifti file"""
    distance_out: OutputPathType
    """the distances, as a cifti file"""
    individual_fibers: ConvertMatrix4ToMatrix2IndividualFibersOutputs
    """Subcommand outputs"""


def convert_matrix4_to_matrix2(
    matrix4_wbsparse: str,
    counts_out: InputPathType,
    distance_out: InputPathType,
    opt_distances: bool = False,
    individual_fibers: ConvertMatrix4ToMatrix2IndividualFibers | None = None,
    runner: Runner = None,
) -> ConvertMatrix4ToMatrix2Outputs:
    """
    convert-matrix4-to-matrix2 by Washington University School of Medicin.
    
    Generates a matrix2 cifti from matrix4 wbsparse.
    
    This command makes a cifti file from the fiber counts in a matrix4 wbsparse
    file, and optionally a second cifti file from the distances. Note that while
    the total count is stored exactly, the per-fiber counts are stored as
    approximate fractions, so the output of -individual-fibers will contain
    nonintegers.
    
    Args:
        matrix4_wbsparse: a wbsparse matrix4 file.
        counts_out: the total fiber counts, as a cifti file.
        distance_out: the distances, as a cifti file.
        opt_distances: output average trajectory distance.
        individual_fibers: output files for each fiber direction.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertMatrix4ToMatrix2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_MATRIX4_TO_MATRIX2_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-matrix4-to-matrix2")
    cargs.append(matrix4_wbsparse)
    cargs.append(execution.input_file(counts_out))
    if opt_distances:
        cargs.append("-distances")
    cargs.append(execution.input_file(distance_out))
    if individual_fibers is not None:
        cargs.extend(["-individual-fibers", *individual_fibers.run(execution)])
    ret = ConvertMatrix4ToMatrix2Outputs(
        root=execution.output_file("."),
        counts_out=execution.output_file(f"{pathlib.Path(counts_out).name}"),
        distance_out=execution.output_file(f"{pathlib.Path(distance_out).name}"),
        individual_fibers=individual_fibers.outputs(execution),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_MATRIX4_TO_MATRIX2_METADATA",
    "ConvertMatrix4ToMatrix2IndividualFibers",
    "ConvertMatrix4ToMatrix2IndividualFibersOutputs",
    "ConvertMatrix4ToMatrix2Outputs",
    "convert_matrix4_to_matrix2",
]
