# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMRM_METADATA = Metadata(
    id="9ac843bdac39040cdf7f53718543f9fee87d5b83",
    name="imrm",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class ImrmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `imrm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def imrm(
    images_to_remove: list[str],
    runner: Runner | None = None,
) -> ImrmOutputs:
    """
    imrm by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Remove specified image files.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/
    
    Args:
        images_to_remove: List of image names to remove. Filenames can be\
            basenames or full names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImrmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMRM_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/imrm")
    cargs.extend(images_to_remove)
    ret = ImrmOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMRM_METADATA",
    "ImrmOutputs",
    "imrm",
]
