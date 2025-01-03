# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QUANTIFY_THALAMIC_NUCLEI_SH_METADATA = Metadata(
    id="b433f3a14e198e3262f3306d8a51e090717c6fe0.boutiques",
    name="quantifyThalamicNuclei.sh",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class QuantifyThalamicNucleiShOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quantify_thalamic_nuclei_sh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    results_file: OutputPathType
    """The output file containing quantified thalamic nuclei results."""


def quantify_thalamic_nuclei_sh(
    output_file: str,
    analysis_id: str,
    subjects_directory: str | None = None,
    runner: Runner | None = None,
) -> QuantifyThalamicNucleiShOutputs:
    """
    Command-line tool to quantify thalamic nuclei using FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        output_file: Output file for the results.
        analysis_id: Analysis ID for specificity.
        subjects_directory: Directory containing subject data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuantifyThalamicNucleiShOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUANTIFY_THALAMIC_NUCLEI_SH_METADATA)
    cargs = []
    cargs.append("quantifyThalamicNuclei.sh")
    cargs.append(output_file)
    cargs.append(analysis_id)
    if subjects_directory is not None:
        cargs.append(subjects_directory)
    ret = QuantifyThalamicNucleiShOutputs(
        root=execution.output_file("."),
        results_file=execution.output_file(output_file),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QUANTIFY_THALAMIC_NUCLEI_SH_METADATA",
    "QuantifyThalamicNucleiShOutputs",
    "quantify_thalamic_nuclei_sh",
]
