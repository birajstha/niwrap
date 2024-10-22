# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_SELECT_STR_PY_METADATA = Metadata(
    id="f2bb90308c31e2b8fa45573c0f2201da8c5ca476.boutiques",
    name="adjunct_select_str.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctSelectStrPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_select_str_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def adjunct_select_str_py(
    input_file: InputPathType,
    num_bricks: float,
    output_file: str,
    runner: Runner | None = None,
) -> AdjunctSelectStrPyOutputs:
    """
    A simple helper function for the fat_proc* scripts.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_file: File containing a list of integers.
        num_bricks: The number N of bricks in the dataset (so max index is N-1).
        output_file: Output file name.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctSelectStrPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_SELECT_STR_PY_METADATA)
    cargs = []
    cargs.append("/opt/afni/src/../install/adjunct_select_str.py")
    cargs.append(execution.input_file(input_file))
    cargs.append(str(num_bricks))
    cargs.append(output_file)
    ret = AdjunctSelectStrPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_SELECT_STR_PY_METADATA",
    "AdjunctSelectStrPyOutputs",
    "adjunct_select_str_py",
]
