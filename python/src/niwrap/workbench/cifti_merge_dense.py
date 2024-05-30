# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CIFTI_MERGE_DENSE_METADATA = Metadata(
    id="d78106e9be3ae37f76e68fba18dfc0e0ea3c28bb",
    name="cifti-merge-dense",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class CiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Cifti.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Cifti:
    """
    specify an input cifti file
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
    ) -> CiftiOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `CiftiOutputs`).
        """
        ret = CiftiOutputs(
            root=execution.output_file("."),
        )
        return ret


class CiftiMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge_dense(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""
    cifti: CiftiOutputs
    """Subcommand outputs"""


def cifti_merge_dense(
    direction: str,
    cifti_out: InputPathType,
    opt_label_collision_action: str | None = None,
    cifti: list[Cifti] = None,
    runner: Runner = None,
) -> CiftiMergeDenseOutputs:
    """
    cifti-merge-dense by Washington University School of Medicin.
    
    Merge cifti files along dense dimension.
    
    The input cifti files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN
        cifti_out: the output cifti file
        opt_label_collision_action: how to handle conflicts between label keys:
            'ERROR', 'FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY' to match
            v1.4.2 and earlier
        cifti: specify an input cifti file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiMergeDenseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge-dense")
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_label_collision_action is not None:
        cargs.extend(["-label-collision", opt_label_collision_action])
    if cifti is not None:
        cargs.extend(["-cifti", *[a for c in [s.run(execution) for s in cifti] for a in c]])
    ret = CiftiMergeDenseOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
        cifti=[cifti.outputs(execution) for cifti in cifti],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_MERGE_DENSE_METADATA",
    "Cifti",
    "CiftiMergeDenseOutputs",
    "CiftiOutputs",
    "cifti_merge_dense",
]
