# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

AFNI_PROC_PY_METADATA = Metadata(
    id="a4908cc703567652b0ff66dd10430d6df6144142.boutiques",
    name="afni_proc.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AfniProcPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afni_proc_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """All output files stored in the specified output directory."""


def afni_proc_py(
    dsets: list[InputPathType],
    subj_id: str,
    anat: InputPathType,
    out_dir: str | None = None,
    blocks: list[str] | None = None,
    echo_times: list[float] | None = None,
    stim_times: list[InputPathType] | None = None,
    stim_files: list[InputPathType] | None = None,
    copy_files: list[InputPathType] | None = None,
    copy_anat: InputPathType | None = None,
    regress_params: list[str] | None = None,
    runner: Runner | None = None,
) -> AfniProcPyOutputs:
    """
    Generate a tcsh script for an AFNI single subject processing stream.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dsets: Specify the EPI dataset files. (e.g. epi_run1+orig,\
            epi_run2+orig).
        subj_id: Specify the subject ID for the script.
        anat: Specify the anatomical dataset.
        out_dir: Specify the output directory for the script.
        blocks: Specify the processing blocks to apply (e.g. tshift volreg blur\
            mask scale regress).
        echo_times: Specify echo times for multi-echo data processing.
        stim_times: Specify files used for stimulus timing in -stim_times.
        stim_files: Specify TR-locked stim files for 3dDeconvolve -stim_file\
            instead of -stim_times.
        copy_files: Specify additional files to be copied to the results\
            directory.
        copy_anat: Copy the anatomical dataset(s) to the results directory.
        regress_params: Specify extra options for 3dDeconvolve.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AfniProcPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFNI_PROC_PY_METADATA)
    cargs = []
    cargs.append("afni_proc.py")
    cargs.extend([execution.input_file(f) for f in dsets])
    cargs.append(subj_id)
    if out_dir is not None:
        cargs.append(out_dir)
    if blocks is not None:
        cargs.extend(blocks)
    cargs.append(execution.input_file(anat))
    if echo_times is not None:
        cargs.extend(map(str, echo_times))
    if stim_times is not None:
        cargs.extend([execution.input_file(f) for f in stim_times])
    if stim_files is not None:
        cargs.extend([execution.input_file(f) for f in stim_files])
    if copy_files is not None:
        cargs.extend([execution.input_file(f) for f in copy_files])
    if copy_anat is not None:
        cargs.append(execution.input_file(copy_anat))
    if regress_params is not None:
        cargs.extend([
            "-regress_opts_3dD",
            *regress_params
        ])
    ret = AfniProcPyOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(out_dir + "/*") if (out_dir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFNI_PROC_PY_METADATA",
    "AfniProcPyOutputs",
    "afni_proc_py",
]
