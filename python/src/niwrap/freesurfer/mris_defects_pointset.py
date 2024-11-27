# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_DEFECTS_POINTSET_METADATA = Metadata(
    id="83e333d1259fc372d991cc353b27693763bfdd37.boutiques",
    name="mris_defects_pointset",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisDefectsPointsetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_defects_pointset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    pointset_output: OutputPathType
    """Output pointset file containing locations of topological defects"""


def mris_defects_pointset(
    surface: InputPathType,
    defects: InputPathType,
    out: InputPathType,
    label: InputPathType | None = None,
    control: bool = False,
    runner: Runner | None = None,
) -> MrisDefectsPointsetOutputs:
    """
    Produces a pointset file containing the locations of each topological defect in
    a surface.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        surface: Input surface.
        defects: Input defect label (must match the surface dimensions).
        out: Output pointset file (json).
        label: Restrict pointset to this label (must be in input surface space).
        control: Save output in old control point format (v6 compatible).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisDefectsPointsetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_DEFECTS_POINTSET_METADATA)
    cargs = []
    cargs.append("mris_defects_pointset")
    cargs.extend([
        "--surf",
        execution.input_file(surface)
    ])
    cargs.extend([
        "--defects",
        execution.input_file(defects)
    ])
    cargs.extend([
        "--out",
        execution.input_file(out)
    ])
    if label is not None:
        cargs.extend([
            "--label",
            execution.input_file(label)
        ])
    if control:
        cargs.append("--control")
    ret = MrisDefectsPointsetOutputs(
        root=execution.output_file("."),
        pointset_output=execution.output_file(pathlib.Path(out).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_DEFECTS_POINTSET_METADATA",
    "MrisDefectsPointsetOutputs",
    "mris_defects_pointset",
]
