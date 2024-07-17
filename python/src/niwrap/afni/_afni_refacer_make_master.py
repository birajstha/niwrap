# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_AFNI_REFACER_MAKE_MASTER_METADATA = Metadata(
    id="7e6ac7ad9e731151a33c461f5c124ca5341af742",
    name="@afni_refacer_make_master",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AfniRefacerMakeMasterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_afni_refacer_make_master(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_shell_dataset: OutputPathType
    """Output dataset containing the average 'face' (non-brain tissue)."""


def _afni_refacer_make_master(
    input_datasets: list[InputPathType],
    runner: Runner | None = None,
) -> AfniRefacerMakeMasterOutputs:
    """
    @afni_refacer_make_master by AFNI Team.
    
    This script makes a new mask/shell dataset for use with @afni_refacer_run by
    averaging 'faces' (non-brain tissue) from input datasets.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@afni_refacer_make_master.html
    
    Args:
        input_datasets: List of T1-weighted datasets that have NOT been\
            skull-stripped, defaced, or refaced.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniRefacerMakeMasterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(_AFNI_REFACER_MAKE_MASTER_METADATA)
    cargs = []
    cargs.append("@afni_refacer_make_master")
    cargs.extend([execution.input_file(f) for f in input_datasets])
    ret = AfniRefacerMakeMasterOutputs(
        root=execution.output_file("."),
        output_shell_dataset=execution.output_file(f"afni_refacer_shell.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AfniRefacerMakeMasterOutputs",
    "_AFNI_REFACER_MAKE_MASTER_METADATA",
    "_afni_refacer_make_master",
]
