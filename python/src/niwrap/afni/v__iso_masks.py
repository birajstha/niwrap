# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__ISO_MASKS_METADATA = Metadata(
    id="b73304663d5c985016c46fca12dbb67249f9bdf2.boutiques",
    name="@IsoMasks",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VIsoMasksOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__iso_masks(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v__iso_masks(
    input_dataset: InputPathType,
    isovals: list[float] | None = None,
    runner: Runner | None = None,
) -> VIsoMasksOutputs:
    """
    Creates isosurfaces from isovolume envelopes.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input dataset for creating isosurfaces.
        isovals: Isovalue thresholds for creating isosurfaces.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VIsoMasksOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__ISO_MASKS_METADATA)
    cargs = []
    cargs.append("@IsoMasks")
    cargs.append("-mask")
    cargs.extend([
        "-mask",
        execution.input_file(input_dataset)
    ])
    if isovals is not None:
        cargs.extend(map(str, isovals))
    ret = VIsoMasksOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VIsoMasksOutputs",
    "V__ISO_MASKS_METADATA",
    "v__iso_masks",
]
