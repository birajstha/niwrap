# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

STRBLAST_METADATA = Metadata(
    id="7ddd88547125dcb844ee7f06e4439fc5470f2937",
    name="strblast",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class StrblastOutputs(typing.NamedTuple):
    """
    Output object returned when calling `strblast(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def strblast(
    targetstring: str,
    input_files: list[InputPathType],
    new_char: str | None = None,
    new_string: str | None = None,
    unescape: bool = False,
    quiet: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> StrblastOutputs:
    """
    strblast by AFNI Team.
    
    Finds exact copies of the target string in each of the input files, and
    replaces all characters with some junk string.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/strblast.html
    
    Args:
        targetstring: Target string to search for in the input files.
        input_files: Input files to search for the target string.
        new_char: Replace TARGETSTRING with CHAR (repeated).
        new_string: Replace TARGETSTRING with STRING.
        unescape: Parse TARGETSTRING for escaped characters (includes '\t',\
            '\n', '\r').
        quiet: Do not report files with no strings found. Use -quiet -quiet to\
            avoid any reporting.
        help_: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `StrblastOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(STRBLAST_METADATA)
    cargs = []
    cargs.append("strblast")
    cargs.append("[OPTIONS]")
    cargs.append("TARGETSTRING")
    cargs.append("[INPUT_FILES...]")
    ret = StrblastOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "STRBLAST_METADATA",
    "StrblastOutputs",
    "strblast",
]
