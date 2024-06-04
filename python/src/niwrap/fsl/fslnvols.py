# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSLNVOLS_METADATA = Metadata(
    id="c22c4accd56834e986d210fe0eff08eba6971654",
    name="fslnvols",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslnvolsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fslnvols(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fslnvols(
    infile: InputPathType,
    runner: Runner = None,
) -> FslnvolsOutputs:
    """
    fslnvols by FMRIB Centre, University of Oxford.
    
    Retrieve the number of volumes in a 4D NIfTI file.
    
    Args:
        infile: Input NIfTI file (e.g., fmri.nii.gz)
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslnvolsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSLNVOLS_METADATA)
    cargs = []
    cargs.append("fslnvols")
    cargs.append(execution.input_file(infile))
    ret = FslnvolsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSLNVOLS_METADATA",
    "FslnvolsOutputs",
    "fslnvols",
]
