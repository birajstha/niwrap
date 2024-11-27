# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ORIENT_LAS_METADATA = Metadata(
    id="c8cbae7a0ae48bc5ff23e10ecc70110ddd8919ae.boutiques",
    name="orientLAS",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class OrientLasOutputs(typing.NamedTuple):
    """
    Output object returned when calling `orient_las(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_las_image: OutputPathType
    """Output image with LAS orientation"""


def orient_las(
    input_image: InputPathType,
    output_image: str,
    check: bool = False,
    runner: Runner | None = None,
) -> OrientLasOutputs:
    """
    Convert image to LAS orientation.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        input_image: Input image in NIfTI format.
        output_image: Output image in NIfTI format with LAS orientation.
        check: Check the match of input and output images using tkregister, and\
            for diffusion data, run dtifit and show tensors with fslview.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `OrientLasOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ORIENT_LAS_METADATA)
    cargs = []
    cargs.append("orientLAS")
    cargs.append(execution.input_file(input_image))
    cargs.append(output_image)
    if check:
        cargs.append("--check")
    ret = OrientLasOutputs(
        root=execution.output_file("."),
        output_las_image=execution.output_file(output_image),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ORIENT_LAS_METADATA",
    "OrientLasOutputs",
    "orient_las",
]
