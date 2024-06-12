# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ESTNOISE_METADATA = Metadata(
    id="95101a6cbc8442338f8f27a7827383378e6a137a",
    name="estnoise",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class EstnoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `estnoise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_noise_file: OutputPathType
    """Output text file containing noise estimates"""


def estnoise(
    input_4d_data: InputPathType,
    spatial_sigma: float | int | None = None,
    temp_hp_sigma: float | int | None = None,
    temp_lp_sigma: float | int | None = None,
    runner: Runner = None,
) -> EstnoiseOutputs:
    """
    estnoise by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Estimate noise in 4D fMRI data.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FEAT
    
    Args:
        input_4d_data: Input 4D fMRI data (e.g., fmri_data.nii.gz).
        spatial_sigma: Spatial smoothing sigma.
        temp_hp_sigma: Temporal high-pass filter sigma.
        temp_lp_sigma: Temporal low-pass filter sigma.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EstnoiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ESTNOISE_METADATA)
    cargs = []
    cargs.append("estnoise")
    cargs.append(execution.input_file(input_4d_data))
    if spatial_sigma is not None:
        cargs.append(str(spatial_sigma))
    if temp_hp_sigma is not None:
        cargs.append(str(temp_hp_sigma))
    if temp_lp_sigma is not None:
        cargs.append(str(temp_lp_sigma))
    ret = EstnoiseOutputs(
        root=execution.output_file("."),
        output_noise_file=execution.output_file(f"noise_estimate.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ESTNOISE_METADATA",
    "EstnoiseOutputs",
    "estnoise",
]
