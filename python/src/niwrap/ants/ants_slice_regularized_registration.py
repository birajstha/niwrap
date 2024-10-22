# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

ANTS_SLICE_REGULARIZED_REGISTRATION_METADATA = Metadata(
    id="69743077b44aed29658d8f89290ab7fb83d6285f.boutiques",
    name="antsSliceRegularizedRegistration",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class AntsSliceRegularizedRegistrationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `ants_slice_regularized_registration(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    polynomial_fit: OutputPathType
    """Output is the polynomial fit to Tx & Ty."""
    transformed_image: OutputPathType
    """Output is the transformed image."""


def ants_slice_regularized_registration(
    polydegree: int,
    output: str,
    metric: str,
    transform: str,
    iterations: str,
    shrink_factors: str,
    smoothing_sigmas: str,
    mask: InputPathType | None = None,
    interpolation: typing.Literal["Linear", "NearestNeighbor", "MultiLabel", "Gaussian", "BSpline", "CosineWindowedSinc", "WelchWindowedSinc", "HammingWindowedSinc", "LanczosWindowedSinc", "GenericLabel"] | None = None,
    verbose: typing.Literal[0] | None = None,
    runner: Runner | None = None,
) -> AntsSliceRegularizedRegistrationOutputs:
    """
    This program is a user-level application for slice-by-slice translation
    registration. Results are regularized in z using polynomial regression. The
    program is targeted at spinal cord MRI. Only one stage is supported where a
    stage consists of a transform; an image metric; and iterations, shrink factors,
    and smoothing sigmas for each level. Specialized for 3D data: fixed image is 3D,
    moving image is 3D. Registration is performed slice-by-slice then regularized in
    z. The parameter -p controls the polynomial degree. -p 0 means no
    regularization.
    
    Author: ANTs developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        polydegree: Degree of polynomial up to zDimension-2. Controls the\
            polynomial degree. 0 means no regularization.
        output: Specify the output transform prefix (output format is .nii.gz).\
            Optionally, one can choose to warp the moving image to the fixed space,\
            and if the inverse transform exists, one can also output the warped\
            fixed image.
        metric: Four image metrics are available: GC: global correlation, CC:\
            ANTS neighborhood cross correlation, MI: Mutual information, and\
            MeanSquares: mean-squares intensity difference.
        transform: Several transform options are available. The gradientStep or\
            learningRate characterizes the gradient descent optimization.
        iterations: Specify the number of iterations at each level.
        shrink_factors: Specify the shrink factor for the virtual domain\
            (typically the fixed image) at each level.
        smoothing_sigmas: Specify the amount of smoothing at each level.
        mask: Fixed image mask to limit voxels considered by the metric.
        interpolation: Several interpolation options are available in ITK.
        verbose: Verbose option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AntsSliceRegularizedRegistrationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ANTS_SLICE_REGULARIZED_REGISTRATION_METADATA)
    cargs = []
    cargs.append("antsSliceRegularizedRegistration")
    cargs.extend([
        "-p",
        str(polydegree)
    ])
    cargs.extend([
        "-o",
        output
    ])
    cargs.extend([
        "-m",
        metric
    ])
    cargs.extend([
        "-t",
        transform
    ])
    cargs.extend([
        "-i",
        iterations
    ])
    cargs.extend([
        "-f",
        shrink_factors
    ])
    cargs.extend([
        "-s",
        smoothing_sigmas
    ])
    if mask is not None:
        cargs.extend([
            "-x",
            execution.input_file(mask)
        ])
    if interpolation is not None:
        cargs.extend([
            "-n",
            interpolation
        ])
    if verbose is not None:
        cargs.extend([
            "-v",
            str(verbose)
        ])
    ret = AntsSliceRegularizedRegistrationOutputs(
        root=execution.output_file("."),
        polynomial_fit=execution.output_file("[OUTPUT_PREFIX]TxTy_poly.csv"),
        transformed_image=execution.output_file("[OUTPUT_PREFIX].nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ANTS_SLICE_REGULARIZED_REGISTRATION_METADATA",
    "AntsSliceRegularizedRegistrationOutputs",
    "ants_slice_regularized_registration",
]
