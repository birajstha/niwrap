# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PARSE_FS_LT_LOG_PY_METADATA = Metadata(
    id="461a7f3353df9377e3262853687d63af58ecd6d3",
    name="parse_fs_lt_log.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ParseFsLtLogPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `parse_fs_lt_log_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def parse_fs_lt_log_py(
    logfile: InputPathType,
    labels: list[str],
    show_orig: bool = False,
    show_all_orig: bool = False,
    verbosity: float | int | None = None,
    runner: Runner | None = None,
) -> ParseFsLtLogPyOutputs:
    """
    parse_fs_lt_log.py by AFNI Team.
    
    Parses FreeSurfer labeltable log file and retrieves labeltable indices.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/parse_fs_lt_log.py.html
    
    Args:
        logfile: Specify rank log file.
        labels: Specify a list of labels to search for.
        show_orig: Show original label indices.
        show_all_orig: Show all original label indices.
        verbosity: Specify verbosity level.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ParseFsLtLogPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(PARSE_FS_LT_LOG_PY_METADATA)
    cargs = []
    cargs.append("parse_fs_lt_log.py")
    cargs.append("-logfile")
    cargs.append(execution.input_file(logfile))
    cargs.append("-labels")
    cargs.extend(["-labels", *labels])
    if show_orig:
        cargs.append("-show_orig")
    if show_all_orig:
        cargs.append("-show_all_orig")
    if verbosity is not None:
        cargs.extend(["-verb", str(verbosity)])
    ret = ParseFsLtLogPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PARSE_FS_LT_LOG_PY_METADATA",
    "ParseFsLtLogPyOutputs",
    "parse_fs_lt_log_py",
]
