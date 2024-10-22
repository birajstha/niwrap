# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ADD_NOISE_TO_IMAGE_METADATA = Metadata(
    id="aee6e337d2376b447bd69dfd2552c6049d319f52.boutiques",
    name="AddNoiseToImage",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AddNoiseToImageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `add_noise_to_image(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    noise_corrupted_image: OutputPathType
    """The output is the noise corrupted version of the input image."""


def add_noise_to_image(
    input_image: InputPathType,
    noise_model: typing.Literal["AdditiveGaussian", "SaltAndPepper", "Shot", "Speckle"],
    output: InputPathType,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AddNoiseToImageOutputs:
    """
    Add various types of noise to an image.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        input_image: A scalar image is expected as input for noise correction.
        noise_model: Use different noise models each with its own (default)\
            parameters.
        output: The output consists of the noise corrupted version of the input\
            image.
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AddNoiseToImageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADD_NOISE_TO_IMAGE_METADATA)
    cargs = []
    cargs.append("AddNoiseToImage")
    if image_dimensionality is not None:
        cargs.extend([
            "--image-dimensionality",
            str(image_dimensionality)
        ])
    cargs.extend([
        "--input-image",
        execution.input_file(input_image)
    ])
    cargs.extend([
        "--noise-model",
        noise_model
    ])
    cargs.extend([
        "--output",
        execution.input_file(output)
    ])
    if verbose is not None:
        cargs.extend([
            "--verbose",
            str(verbose)
        ])
    ret = AddNoiseToImageOutputs(
        root=execution.output_file("."),
        noise_corrupted_image=execution.output_file(pathlib.Path(output).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADD_NOISE_TO_IMAGE_METADATA",
    "AddNoiseToImageOutputs",
    "add_noise_to_image",
]
