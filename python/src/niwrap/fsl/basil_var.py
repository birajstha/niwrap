# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

BASIL_VAR_METADATA = Metadata(
    id="dbad0f561e04c1b6ad685a18bfffc13d1e96e10a",
    name="basil_var",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class BasilVarOutputs(typing.NamedTuple):
    """
    Output object returned when calling `basil_var(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def basil_var(
    results_dir: str,
    mask_image: InputPathType,
    runner: Runner | None = None,
) -> BasilVarOutputs:
    """
    basil_var by FMRIB Software Library (FSL).
    
    Variance calculator for BASIL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BASIL
    
    Args:
        results_dir: BASIL results directory.
        mask_image: Mask image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BasilVarOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(BASIL_VAR_METADATA)
    cargs = []
    cargs.append("basil_var")
    cargs.append("-d")
    cargs.extend(["-d", results_dir])
    cargs.append("-m")
    cargs.extend(["-m", execution.input_file(mask_image)])
    ret = BasilVarOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BASIL_VAR_METADATA",
    "BasilVarOutputs",
    "basil_var",
]
