# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_AVERAGE_METADATA = Metadata(
    id="185ad89a6fdcd3976ce8d726d7453bce3c5bd92e",
    name="cifti-average",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiAverageExcludeOutliers:
    """
    exclude outliers by standard deviation of each element across files
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
class CiftiAverageCifti:
    """
    specify an input file
    """
    opt_weight_weight: float | int | None = None
    """give a weight for this file: the weight to use"""
    
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
        if self.opt_weight_weight is not None:
            cargs.extend(["-weight", str(self.opt_weight_weight)])
        return cargs


class CiftiAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """output cifti file"""


def cifti_average(
    cifti_out: InputPathType,
    exclude_outliers: CiftiAverageExcludeOutliers | None = None,
    opt_mem_limit_limit_gb: float | int | None = None,
    cifti: list[CiftiAverageCifti] = None,
    runner: Runner = None,
) -> CiftiAverageOutputs:
    """
    cifti-average by Washington University School of Medicin.
    
    Average cifti files.
    
    Averages cifti files together. Files without -weight specified are given a
    weight of 1. If -exclude-outliers is specified, at each element, the data
    across all files is taken as a set, its unweighted mean and sample standard
    deviation are found, and values outside the specified number of standard
    deviations are excluded from the (potentially weighted) average at that
    element.
    
    Args:
        cifti_out: output cifti file.
        exclude_outliers: exclude outliers by standard deviation of each\
            element across files.
        opt_mem_limit_limit_gb: restrict memory used for file reading\
            efficiency: memory limit in gigabytes.
        cifti: specify an input file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_AVERAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-average")
    cargs.append(execution.input_file(cifti_out))
    if exclude_outliers is not None:
        cargs.extend(["-exclude-outliers", *exclude_outliers.run(execution)])
    if opt_mem_limit_limit_gb is not None:
        cargs.extend(["-mem-limit", str(opt_mem_limit_limit_gb)])
    if cifti is not None:
        cargs.extend(["-cifti", *[a for c in [s.run(execution) for s in cifti] for a in c]])
    ret = CiftiAverageOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_AVERAGE_METADATA",
    "CiftiAverageCifti",
    "CiftiAverageExcludeOutliers",
    "CiftiAverageOutputs",
    "cifti_average",
]
