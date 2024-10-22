# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_THICKNESS_COMPARISON_METADATA = Metadata(
    id="f7bfaa75348c833cf839178ebd6fa5750d22af34.boutiques",
    name="mris_thickness_comparison",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisThicknessComparisonOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_thickness_comparison(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def mris_thickness_comparison(
    subject: str,
    hemi: str,
    thickness_file: InputPathType,
    w_file: InputPathType,
    labels: list[str],
    runner: Runner | None = None,
) -> MrisThicknessComparisonOutputs:
    """
    Tool to compare cortical thickness measurements between two or more specified
    labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject identifier.
        hemi: Hemisphere (e.g., lh or rh).
        thickness_file: File containing thickness measurements.
        w_file: W file for cortical thickness comparison.
        labels: List of labels to compare, separated by spaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisThicknessComparisonOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_THICKNESS_COMPARISON_METADATA)
    cargs = []
    cargs.append("/usr/local/freesurfer/bin/mris_thickness_comparison")
    cargs.append(subject)
    cargs.append(hemi)
    cargs.append(execution.input_file(thickness_file))
    cargs.append(execution.input_file(w_file))
    cargs.extend(labels)
    ret = MrisThicknessComparisonOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_THICKNESS_COMPARISON_METADATA",
    "MrisThicknessComparisonOutputs",
    "mris_thickness_comparison",
]