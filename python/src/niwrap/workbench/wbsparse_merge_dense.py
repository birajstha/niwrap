# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


WBSPARSE_MERGE_DENSE_METADATA = Metadata(
    id="bd404bd66af73c87abf735ee1f81a49687bb0945",
    name="wbsparse-merge-dense",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class WbsparseMergeDenseWbsparse:
    """
    specify an input wbsparse file
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


class WbsparseMergeDenseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wbsparse_merge_dense(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def wbsparse_merge_dense(
    direction: str,
    wbsparse_out: str,
    wbsparse: list[WbsparseMergeDenseWbsparse] = None,
    runner: Runner = None,
) -> WbsparseMergeDenseOutputs:
    """
    wbsparse-merge-dense by Washington University School of Medicin.
    
    Merge wbsparse files along dense dimension.
    
    The input wbsparse files must have matching mappings along the direction not
    specified, and the mapping along the specified direction must be brain
    models.
    
    Args:
        direction: which dimension to merge along, ROW or COLUMN
        wbsparse_out: output - the output wbsparse file
        wbsparse: specify an input wbsparse file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `WbsparseMergeDenseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WBSPARSE_MERGE_DENSE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-wbsparse-merge-dense")
    cargs.append(direction)
    cargs.append(wbsparse_out)
    if wbsparse is not None:
        cargs.extend(["-wbsparse", *[a for c in [s.run(execution) for s in wbsparse] for a in c]])
    ret = WbsparseMergeDenseOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WBSPARSE_MERGE_DENSE_METADATA",
    "WbsparseMergeDenseOutputs",
    "WbsparseMergeDenseWbsparse",
    "wbsparse_merge_dense",
]
