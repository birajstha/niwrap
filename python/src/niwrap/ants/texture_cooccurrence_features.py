# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TEXTURE_COOCCURRENCE_FEATURES_METADATA = Metadata(
    id="91591f77263330ed7a5bfa1c36e1edb089c3c166.boutiques",
    name="TextureCooccurrenceFeatures",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class TextureCooccurrenceFeaturesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `texture_cooccurrence_features(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    features_output: OutputPathType
    """The output file containing the calculated texture co-occurrence
    features."""


def texture_cooccurrence_features(
    image_dimension: int,
    input_image: InputPathType,
    number_of_bins_per_axis: int | None = 256,
    mask_image: InputPathType | None = None,
    mask_label: int | None = 1,
    runner: Runner | None = None,
) -> TextureCooccurrenceFeaturesOutputs:
    """
    Calculates texture co-occurrence features such as Energy, Entropy, Inverse
    Difference Moment, Inertia, Cluster Shade, and Cluster Prominence from an input
    image.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input image, e.g., 2 for 2D\
            images, 3 for 3D images.
        input_image: The input image file for which texture co-occurrence\
            features will be calculated.
        number_of_bins_per_axis: The number of bins per axis to be used in the\
            histogram for texture calculation. Defaults to 256.
        mask_image: Optional mask image to specify the regions of interest in\
            the input image for which features will be calculated.
        mask_label: Label value in the mask image to specify which region to\
            process. Defaults to 1.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TextureCooccurrenceFeaturesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TEXTURE_COOCCURRENCE_FEATURES_METADATA)
    cargs = []
    cargs.append("TextureCooccurrenceFeatures")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(input_image))
    if number_of_bins_per_axis is not None:
        cargs.append(str(number_of_bins_per_axis))
    if mask_image is not None:
        cargs.append(execution.input_file(mask_image))
    if mask_label is not None:
        cargs.append(str(mask_label))
    ret = TextureCooccurrenceFeaturesOutputs(
        root=execution.output_file("."),
        features_output=execution.output_file(pathlib.Path(input_image).name + "_features.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TEXTURE_COOCCURRENCE_FEATURES_METADATA",
    "TextureCooccurrenceFeaturesOutputs",
    "texture_cooccurrence_features",
]
