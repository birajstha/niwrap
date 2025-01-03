# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANATOMI_CUTS_UTILS_METADATA = Metadata(
    id="7198fe86c99847a1acd99691b128d75fcca8f4b4.boutiques",
    name="anatomiCutsUtils",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class AnatomiCutsUtilsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `anatomi_cuts_utils(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def anatomi_cuts_utils(
    modules: list[str] | None = None,
    runner: Runner | None = None,
) -> AnatomiCutsUtilsOutputs:
    """
    A tool for anatomical segmentation using graph-based methods.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        modules: Specify the modules to import for processing. Ensure necessary\
            modules like 'graph_tools' are installed.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AnatomiCutsUtilsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANATOMI_CUTS_UTILS_METADATA)
    cargs = []
    cargs.append("anatomiCutsUtils")
    if modules is not None:
        cargs.extend(modules)
    ret = AnatomiCutsUtilsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANATOMI_CUTS_UTILS_METADATA",
    "AnatomiCutsUtilsOutputs",
    "anatomi_cuts_utils",
]
