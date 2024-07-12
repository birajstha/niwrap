# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_1_PREPROC_METADATA = Metadata(
    id="f76d4b1376fdbeb5efe826480805b7a90b94d549",
    name="tbss_1_preproc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class Tbss1PreprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_1_preproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def tbss_1_preproc(
    images: list[InputPathType],
    runner: Runner | None = None,
) -> Tbss1PreprocOutputs:
    """
    tbss_1_preproc by FSL (FMRIB Software Library).
    
    TBSS (Tract-Based Spatial Statistics) - Step 1: Preprocessing.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS
    
    Args:
        images: List of input images (e.g. subj1_FA.nii.gz subj2_FA.nii.gz ...).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tbss1PreprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_1_PREPROC_METADATA)
    cargs = []
    cargs.append("tbss_1_preproc")
    cargs.extend([execution.input_file(f) for f in images])
    ret = Tbss1PreprocOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_1_PREPROC_METADATA",
    "Tbss1PreprocOutputs",
    "tbss_1_preproc",
]
