# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADJUNCT_VOL_3SLICE_SELECT_METADATA = Metadata(
    id="d87450945a3a21e9af03e7d6fc99f2aadb69979e.boutiques",
    name="adjunct_vol_3slice_select",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class AdjunctVol3sliceSelectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `adjunct_vol_3slice_select(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    ijk_output: OutputPathType
    """File that contains the output indices i j k."""


def adjunct_vol_3slice_select(
    dataset_file: InputPathType,
    coord_x: float,
    coord_y: float,
    coord_z: float,
    runner: Runner | None = None,
) -> AdjunctVol3sliceSelectOutputs:
    """
    Helper script to convert (x, y, z) coordinates to (i, j, k) indices for a
    dataset. It will return an error if any indices are outside the dataset's
    matrix.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dataset_file: The name of the dataset file.
        coord_x: The x-coordinate in the dataset.
        coord_y: The y-coordinate in the dataset.
        coord_z: The z-coordinate in the dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AdjunctVol3sliceSelectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADJUNCT_VOL_3SLICE_SELECT_METADATA)
    cargs = []
    cargs.append("adjunct_vol_3slice_select")
    cargs.append(execution.input_file(dataset_file))
    cargs.append(str(coord_x))
    cargs.append(str(coord_y))
    cargs.append(str(coord_z))
    ret = AdjunctVol3sliceSelectOutputs(
        root=execution.output_file("."),
        ijk_output=execution.output_file("ijk_indices.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADJUNCT_VOL_3SLICE_SELECT_METADATA",
    "AdjunctVol3sliceSelectOutputs",
    "adjunct_vol_3slice_select",
]
