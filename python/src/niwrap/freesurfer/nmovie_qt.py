# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

NMOVIE_QT_METADATA = Metadata(
    id="40a52c883b6ef1eabbaca98341ef5cfeff36ee79.boutiques",
    name="nmovie_qt",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class NmovieQtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nmovie_qt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def nmovie_qt(
    images: list[InputPathType],
    runner: Runner | None = None,
) -> NmovieQtOutputs:
    """
    An image viewer using Qt for displaying images in sequence.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        images: Input image files to be displayed. Multiple files can be\
            provided.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `NmovieQtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NMOVIE_QT_METADATA)
    cargs = []
    cargs.append("nmovie_qt")
    cargs.extend([execution.input_file(f) for f in images])
    ret = NmovieQtOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NMOVIE_QT_METADATA",
    "NmovieQtOutputs",
    "nmovie_qt",
]
