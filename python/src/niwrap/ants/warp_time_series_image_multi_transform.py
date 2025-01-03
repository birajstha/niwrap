# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA = Metadata(
    id="6ce7851c544e610fc5a77e4703824ad332c7d885.boutiques",
    name="WarpTimeSeriesImageMultiTransform",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class WarpTimeSeriesImageMultiTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warp_time_series_image_multi_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_result: OutputPathType
    """The transformed image that is saved as output."""


def warp_time_series_image_multi_transform(
    image_dimension: typing.Literal[3, 4],
    moving_image: InputPathType,
    output_image: InputPathType,
    reference_image: InputPathType,
    transforms: list[str],
    interpolation: typing.Literal["NearestNeighbor", "BSpline"] | None = None,
    runner: Runner | None = None,
) -> WarpTimeSeriesImageMultiTransformOutputs:
    """
    WarpTimeSeriesImageMultiTransform is a tool used to apply a series of
    transformations to a time series image, either forward or reverse, using affine
    transforms and warps.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        image_dimension: The dimensionality of the input images (3D or 4D).
        moving_image: The image to which the transformation will be applied. It\
            can be a 3D image with vector voxels or a 4D image with scalar voxels.
        output_image: The output image after transformation. It is resampled\
            based on the reference image domain.
        reference_image: The reference image that defines the space into which\
            the input image will be warped.
        transforms: A list of transformation files, such as affine\
            transformation matrices and warps, applied in sequence.
        interpolation: Specifies the type of interpolation to use: Nearest\
            Neighbor or 3rd order B-Spline.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WarpTimeSeriesImageMultiTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA)
    cargs = []
    cargs.append("WarpTimeSeriesImageMultiTransform")
    cargs.append(str(image_dimension))
    cargs.append(execution.input_file(moving_image))
    cargs.append(execution.input_file(output_image))
    cargs.extend([
        "-R",
        execution.input_file(reference_image)
    ])
    cargs.extend(transforms)
    if interpolation is not None:
        cargs.append(interpolation)
    ret = WarpTimeSeriesImageMultiTransformOutputs(
        root=execution.output_file("."),
        output_image_result=execution.output_file(pathlib.Path(output_image).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WARP_TIME_SERIES_IMAGE_MULTI_TRANSFORM_METADATA",
    "WarpTimeSeriesImageMultiTransformOutputs",
    "warp_time_series_image_multi_transform",
]
