# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__COMMAND_GLOBB_METADATA = Metadata(
    id="c2faf81a08e05a3e16060acc326e418fbdfeaad0.boutiques",
    name="@CommandGlobb",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VCommandGlobbOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__command_globb(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated by the specified program command line."""


def v__command_globb(
    program_command: str,
    output_dir: str,
    brick_list: list[str],
    extension: str | None = None,
    runner: Runner | None = None,
) -> VCommandGlobbOutputs:
    """
    A command-line tool to execute a specified program command line on a list of
    input bricks.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        program_command: The entire command line for the program desired. The\
            command is best put between single quotes, do not use the \\ to break a\
            long line within the quotes.
        output_dir: The output directory where the results will be saved.
        brick_list: A list of bricks (or anything) on which the program command\
            will be executed.
        extension: If the program requires a -prefix option, then you can\
            specify the extension which will get appended to the Brick names before\
            +orig.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VCommandGlobbOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__COMMAND_GLOBB_METADATA)
    cargs = []
    cargs.append("@CommandGlobb")
    cargs.append("-com")
    cargs.append(program_command)
    cargs.append("-session")
    cargs.append(output_dir)
    cargs.append("-newxt")
    if extension is not None:
        cargs.append(extension)
    cargs.extend([
        "-list",
        *brick_list
    ])
    ret = VCommandGlobbOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(output_dir + "/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VCommandGlobbOutputs",
    "V__COMMAND_GLOBB_METADATA",
    "v__command_globb",
]
