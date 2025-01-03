# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_TCORRELATE_METADATA = Metadata(
    id="a874b3865df8702baf89b243d1e11b051abda5bf.boutiques",
    name="3dTcorrelate",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dTcorrelateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcorrelate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType | None
    """Output image file name."""


def v_3d_tcorrelate(
    xset: InputPathType,
    yset: InputPathType,
    pearson: bool = False,
    spearman: bool = False,
    quadrant: bool = False,
    ktaub: bool = False,
    covariance: bool = False,
    partial: InputPathType | None = None,
    ycoef: bool = False,
    fisher: bool = False,
    polort: int | None = None,
    ort: InputPathType | None = None,
    autoclip: bool = False,
    automask: bool = False,
    zcensor: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dTcorrelateOutputs:
    """
    3dTcorrelate. Computes the correlation coefficient between corresponding voxel
    time series in two input 3D+time datasets 'xset' and 'yset'.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        xset: Input xset.
        yset: Input yset.
        pearson: Correlation is the normal pearson correlation coefficient.
        spearman: Correlation is the Spearman (rank) correlation coefficient.
        quadrant: Correlation is the quadrant coefficient.
        ktaub: Correlation is Kendall's tau_b coefficient. For continuous or\
            finely discretized data, tau_b and rank correlation are nearly\
            equivalent.
        covariance: Covariance instead of correlation. That would be Pearson\
            correlation without scaling by the product of the standard deviations.
        partial: Partial Pearson's correlation of X & Y, adjusting for Z (the\
            dataset provided here).
        ycoef: Least squares coefficient that best fits y(t) to x(t), after\
            detrending. That is, if yd(t) is the detrended y(t) and xd(t) is the\
            detrended x(t), then the ycoef value is from the OLSQ fit to xd(t) =\
            ycoef & y(t) + error.
        fisher: Apply the Fisher (inverse hyperbolic tangent) transformation to\
            correlation results. Does not make sense with ktaub, covariance, or\
            ycoef.
        polort: Remove polynomial trend of order m. Using m=-1 mean no\
            detrending; this is only useful fro data that has been preprocessed.
        ort: A 1D file. Also detrend using the columbs of the 1D file provided\
            here. Only one -ort option can be given, so if you would like to use\
            more than one, create a temporary file using 1dcat.
        autoclip: Clip off low-intensity regions in the two datasets, so that\
            the correlation is only computed between high-intensity (presumably\
            brain) voxels. The intensity level is determined the same way that\
            3dClipLevel works.
        automask: Clip off low-intensity regions in the two datasets, so that\
            the correlation is only computed between high-intensity (presumably\
            brain) voxels. The intensity level is determined the same way that\
            3dClipLevel works.
        zcensor: Omit (censor out) any time points where the xset volume is all\
            zero OR where the yset volume is all zero (in mask). Please note that\
            using -zcensor with any detrending is unlikely to be useful.
        prefix: Save output into a dataset with this prefix.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTcorrelateOutputs`).
    """
    if polort is not None and not (-1 <= polort <= 9): 
        raise ValueError(f"'polort' must be between -1 <= x <= 9 but was {polort}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCORRELATE_METADATA)
    cargs = []
    cargs.append("3dTcorrelate")
    cargs.append(execution.input_file(xset))
    cargs.append(execution.input_file(yset))
    if pearson:
        cargs.append("-pearson")
    if spearman:
        cargs.append("-spearman")
    if quadrant:
        cargs.append("-quadrant")
    if ktaub:
        cargs.append("-ktaub")
    if covariance:
        cargs.append("-covariance")
    if partial is not None:
        cargs.extend([
            "-partial",
            execution.input_file(partial)
        ])
    if ycoef:
        cargs.append("-ycoef")
    if fisher:
        cargs.append("-Fisher")
    if polort is not None:
        cargs.extend([
            "-polort",
            str(polort)
        ])
    if ort is not None:
        cargs.extend([
            "-ort",
            execution.input_file(ort)
        ])
    if autoclip:
        cargs.append("-autoclip")
    if automask:
        cargs.append("-automask")
    if zcensor:
        cargs.append("-zcensor")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    ret = V3dTcorrelateOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(prefix) if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTcorrelateOutputs",
    "V_3D_TCORRELATE_METADATA",
    "v_3d_tcorrelate",
]
