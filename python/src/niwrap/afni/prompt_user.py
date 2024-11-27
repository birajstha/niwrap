# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

PROMPT_USER_METADATA = Metadata(
    id="eeffbea4e522408c1d4978572830a23c9b27d7fb.boutiques",
    name="prompt_user",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class PromptUserOutputs(typing.NamedTuple):
    """
    Output object returned when calling `prompt_user(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def prompt_user(
    pause_message: str,
    timeout_alias: float | None = None,
    runner: Runner | None = None,
) -> PromptUserOutputs:
    """
    Tool that prompts a window requesting user input with a custom message.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        pause_message: Pops a window prompting the user with MESSAGE. If\
            MESSAGE is '-', it is read from stdin.
        timeout_alias: Alias for -timeout.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PromptUserOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PROMPT_USER_METADATA)
    cargs = []
    cargs.append("prompt_user")
    cargs.extend([
        "<-pause>",
        pause_message
    ])
    if timeout_alias is not None:
        cargs.extend([
            "-to",
            str(timeout_alias)
        ])
    ret = PromptUserOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PROMPT_USER_METADATA",
    "PromptUserOutputs",
    "prompt_user",
]
