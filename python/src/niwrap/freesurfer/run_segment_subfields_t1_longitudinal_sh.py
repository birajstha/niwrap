# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA = Metadata(
    id="06a7bfba6231f999f1b4d6fa26f1a22c4fe4eb12.boutiques",
    name="run_SegmentSubfieldsT1Longitudinal.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class RunSegmentSubfieldsT1LongitudinalShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_segment_subfields_t1_longitudinal_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def run_segment_subfields_t1_longitudinal_sh(
    deployed_mcr_root: str,
    additional_args: str | None = None,
    runner: Runner | None = None,
) -> RunSegmentSubfieldsT1LongitudinalShOutputs:
    """
    Script for segmenting subfields from T1-weighted longitudinal data using
    FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        deployed_mcr_root: Root directory for the deployed MATLAB Runtime\
            environment.
        additional_args: Additional arguments for the script.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunSegmentSubfieldsT1LongitudinalShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA)
    cargs = []
    cargs.append("run_SegmentSubfieldsT1Longitudinal.sh")
    cargs.append(deployed_mcr_root)
    if additional_args is not None:
        cargs.append(additional_args)
    ret = RunSegmentSubfieldsT1LongitudinalShOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_SEGMENT_SUBFIELDS_T1_LONGITUDINAL_SH_METADATA",
    "RunSegmentSubfieldsT1LongitudinalShOutputs",
    "run_segment_subfields_t1_longitudinal_sh",
]
