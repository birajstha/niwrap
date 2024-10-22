# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCRIPT_CHECKER_METADATA = Metadata(
    id="e2aa93fc3f80f4097fc9ac1c3236a80a91ec530f.boutiques",
    name="ScriptChecker",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class ScriptCheckerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `script_checker(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    uncleaned_file: OutputPathType
    """Uncleaned original file with specified suffix"""
    cleaned_file: OutputPathType
    """Cleaned file if -clean option is used"""


def script_checker(
    scripts: list[InputPathType],
    clean: bool = False,
    suffix: str | None = None,
    runner: Runner | None = None,
) -> ScriptCheckerOutputs:
    """
    Checks scripts for improperly terminated lines and optionally cleans them.
    
    Author: AFNI Team
    
    URL: https://afni.nimh.nih.gov/pub/dist/doc/program_help/@ScriptCheck.html
    
    Args:
        scripts: Scripts to be checked for improperly terminated lines.
        clean: Clean bad line breaks.
        suffix: Rename uncleaned file with specified suffix. Default is .uncln.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ScriptCheckerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCRIPT_CHECKER_METADATA)
    cargs = []
    cargs.append("ScriptChecker")
    if clean:
        cargs.append("-clean")
    if suffix is not None:
        cargs.extend([
            "-suffix",
            suffix
        ])
    cargs.extend([execution.input_file(f) for f in scripts])
    ret = ScriptCheckerOutputs(
        root=execution.output_file("."),
        uncleaned_file=execution.output_file("{SCRIPT}.uncln"),
        cleaned_file=execution.output_file("{SCRIPT}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCRIPT_CHECKER_METADATA",
    "ScriptCheckerOutputs",
    "script_checker",
]