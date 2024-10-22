# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

CIFTI_MERGE_DENSE_METADATA = Metadata(
    id="c07846f7ec6e365acb0850a975af15334fd9d94a.boutiques",
    name="cifti-merge-dense",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class CiftiMergeDenseCifti:
    """
    specify an input cifti file.
    """
    cifti_in: InputPathType
    """a cifti file to merge"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-cifti")
        cargs.append(execution.input_file(self.cifti_in))
        return cargs


class CiftiMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_merge_dense(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_merge_dense(
    direction: str,
    cifti_out: str,
    opt_label_collision_action: str | None = None,
    cifti: list[CiftiMergeDenseCifti] | None = None,
    runner: Runner | None = None,
) -> CiftiMergeDenseOutputs:
    """
    Merge cifti files along dense dimension.
    
    The input cifti files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN.
        cifti_out: the output cifti file.
        opt_label_collision_action: how to handle conflicts between label keys:\
            'ERROR', 'FIRST', or 'LEGACY', default 'ERROR', use 'LEGACY' to match\
            v1.4.2 and earlier.
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiMergeDenseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-merge-dense")
    cargs.append(direction)
    cargs.append(cifti_out)
    if opt_label_collision_action is not None:
        cargs.extend([
            "-label-collision",
            opt_label_collision_action
        ])
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiMergeDenseOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(cifti_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_MERGE_DENSE_METADATA",
    "CiftiMergeDenseCifti",
    "CiftiMergeDenseOutputs",
    "cifti_merge_dense",
]
