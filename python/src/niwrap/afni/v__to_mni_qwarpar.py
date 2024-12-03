# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__TO_MNI_QWARPAR_METADATA = Metadata(
    id="04e45eb40a57d1fc1e8c94957315562ee18d3086.boutiques",
    name="@toMNI_Qwarpar",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VToMniQwarparOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__to_mni_qwarpar(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output dataset created after processing."""


def v__to_mni_qwarpar(
    runner: Runner | None = None,
) -> VToMniQwarparOutputs:
    """
    Transforms datasets to MNI space, then collectively re-transforms them to
    produce a refined average.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VToMniQwarparOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__TO_MNI_QWARPAR_METADATA)
    cargs = []
    cargs.append("@toMNI_Qwarpar")
    ret = VToMniQwarparOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("*_uni+tlrc.HEAD"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VToMniQwarparOutputs",
    "V__TO_MNI_QWARPAR_METADATA",
    "v__to_mni_qwarpar",
]