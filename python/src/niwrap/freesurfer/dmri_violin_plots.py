# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

DMRI_VIOLIN_PLOTS_METADATA = Metadata(
    id="a193f3c5d1fcce153b59c31f2df32aafdf44cb45.boutiques",
    name="dmri_violinPlots",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class DmriViolinPlotsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `dmri_violin_plots(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def dmri_violin_plots(
    input_directory: str,
    labels: InputPathType,
    structure: str,
    runner: Runner | None = None,
) -> DmriViolinPlotsOutputs:
    """
    Generate violin plots for dMRI data.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_directory: Directory with all subjects.
        labels: CSV file with group labels.
        structure: Name of the structure.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DmriViolinPlotsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(DMRI_VIOLIN_PLOTS_METADATA)
    cargs = []
    cargs.append("dmri_violinPlots")
    cargs.extend([
        "-i",
        input_directory
    ])
    cargs.extend([
        "-l",
        execution.input_file(labels)
    ])
    cargs.extend([
        "-s",
        structure
    ])
    ret = DmriViolinPlotsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DMRI_VIOLIN_PLOTS_METADATA",
    "DmriViolinPlotsOutputs",
    "dmri_violin_plots",
]
