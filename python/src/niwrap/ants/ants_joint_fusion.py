# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_JOINT_FUSION_METADATA = Metadata(
    id="e3c0355412de6dbc842f99d135c2be7604cb670d.boutiques",
    name="antsJointFusion",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsJointFusionOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_joint_fusion(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    label_fusion_image: OutputPathType
    """The output label fusion image."""
    intensity_fusion_image: OutputPathType
    """The output intensity fusion image format."""
    label_posterior_probability_image: OutputPathType
    """The output label posterior probability image format."""
    atlas_voting_weight_image: OutputPathType
    """The output atlas voting weight image format."""


def ants_joint_fusion(
    target_image: list[InputPathType],
    atlas_image: list[InputPathType],
    atlas_segmentation: InputPathType,
    output: str,
    image_dimensionality: typing.Literal[2, 3, 4] | None = None,
    alpha: float | None = 0.1,
    beta: float | None = 2.0,
    constrain_nonnegative: typing.Literal[0, 1] | None = None,
    patch_radius: str | None = "2x2x2",
    patch_metric: typing.Literal["PC", "MSQ"] | None = "PC",
    search_radius: str | None = "3x3x3",
    exclusion_image: InputPathType | None = None,
    mask_image: InputPathType | None = None,
    verbose: typing.Literal[0, 1] | None = None,
    runner: Runner | None = None,
) -> AntsJointFusionOutputs:
    """
    antsJointFusion is an image fusion algorithm developed by Hongzhi Wang and Paul
    Yushkevich. This implementation is based on Paul's original ITK-style
    implementation and Brian's ANTsR implementation. The original label fusion
    framework was extended to accommodate intensities.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        target_image: The target image (or multimodal target images) assumed to\
            be aligned to a common image domain.
        atlas_image: The atlas image (or multimodal atlas images) assumed to be\
            aligned to a common image domain.
        atlas_segmentation: The atlas segmentation images. For performing label\
            fusion the number of specified segmentations should be identical to the\
            number of atlas image sets.
        output: The output is the intensity and/or label fusion image.\
            Additional optional outputs include the label posterior probability\
            images and the atlas voting weight images.
        image_dimensionality: This option forces the image to be treated as a\
            specified-dimensional image. If not specified, the program tries to\
            infer the dimensionality from the input image.
        alpha: Regularization term added to matrix Mx for calculating the\
            inverse. Default = 0.1.
        beta: Exponent for mapping intensity difference to the joint error.\
            Default = 2.0.
        constrain_nonnegative: Constrain solution to non-negative weights.
        patch_radius: Patch radius for similarity measures. Default = 2x2x2.
        patch_metric: Metric to be used in determining the most similar\
            neighborhood patch. Options include Pearson's correlation (PC) and mean\
            squares (MSQ). Default = PC (Pearson correlation).
        search_radius: Search radius for similarity measures. Default = 3x3x3.\
            One can also specify an image where the value at the voxel specifies\
            the isotropic search radius at that voxel.
        exclusion_image: Specify an exclusion region for the given label.
        mask_image: If a mask image is specified, fusion is only performed in\
            the mask region.
        verbose: Verbose output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsJointFusionOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_JOINT_FUSION_METADATA)
    cargs = []
    cargs.append("antsJointFusion")
    if image_dimensionality is not None:
        cargs.extend([
            "--image-dimensionality",
            str(image_dimensionality)
        ])
    cargs.extend([
        "--target-image",
        *[execution.input_file(f) for f in target_image]
    ])
    cargs.extend([
        "--atlas-image",
        *[execution.input_file(f) for f in atlas_image]
    ])
    cargs.extend([
        "--atlas-segmentation",
        execution.input_file(atlas_segmentation)
    ])
    if alpha is not None:
        cargs.extend([
            "--alpha",
            str(alpha)
        ])
    if beta is not None:
        cargs.extend([
            "--beta",
            str(beta)
        ])
    if constrain_nonnegative is not None:
        cargs.extend([
            "--constrain-nonnegative",
            str(constrain_nonnegative)
        ])
    if patch_radius is not None:
        cargs.extend([
            "--patch-radius",
            patch_radius
        ])
    if patch_metric is not None:
        cargs.extend([
            "--patch-metric",
            patch_metric
        ])
    if search_radius is not None:
        cargs.extend([
            "--search-radius",
            search_radius
        ])
    if exclusion_image is not None:
        cargs.extend([
            "--exclusion-image",
            execution.input_file(exclusion_image)
        ])
    if mask_image is not None:
        cargs.extend([
            "--mask-image",
            execution.input_file(mask_image)
        ])
    cargs.extend([
        "--output",
        output
    ])
    if verbose is not None:
        cargs.extend([
            "--verbose",
            str(verbose)
        ])
    ret = AntsJointFusionOutputs(
        root=execution.output_file("."),
        label_fusion_image=execution.output_file("[LABELFUSIONIMAGE]"),
        intensity_fusion_image=execution.output_file("[INTENSITYFUSIONIMAGEFILENAMEFORMAT]"),
        label_posterior_probability_image=execution.output_file("[LABELPOSTERIORPROBABILITYIMAGEFILENAMEFORMAT]"),
        atlas_voting_weight_image=execution.output_file("[ATLASVOTINGWEIGHTIMAGEFILENAMEFORMAT]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_JOINT_FUSION_METADATA",
    "AntsJointFusionOutputs",
    "ants_joint_fusion",
]
