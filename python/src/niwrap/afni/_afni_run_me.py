# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_AFNI_RUN_ME_METADATA = Metadata(
    id="f53ea975be48684eb226ef5dee3840314ae33a03",
    name="@afni.run.me",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniRunMeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_afni_run_me(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _afni_run_me(
    help_: bool = False,
    go: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> AfniRunMeOutputs:
    """
    @afni.run.me by AFNI Team.
    
    A tool to execute a specific command.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni.run.me.html
    
    Args:
        help_: Show help message.
        go: Execute the work.
        curl: Default to curl instead of wget.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniRunMeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_AFNI_RUN_ME_METADATA)
    cargs = []
    cargs.append("@afni.run.me")
    if go:
        cargs.append("-go")
    if curl:
        cargs.append("-curl")
    if help_:
        cargs.append("-help")
    ret = AfniRunMeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AfniRunMeOutputs",
    "_AFNI_RUN_ME_METADATA",
    "_afni_run_me",
]
