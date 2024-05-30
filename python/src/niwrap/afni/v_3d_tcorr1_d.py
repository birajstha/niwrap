# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


V_3D_TCORR1_D_METADATA = Metadata(
    id="10b7d3d570d9e43a0d7545f8685ae04a9441c403",
    name="3dTcorr1D",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTcorr1DOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcorr1_d(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output filename prefix."""
    out_file_: OutputPathType
    """Output file containing correlations."""


def v_3d_tcorr1_d(
    xset: InputPathType,
    y_1d: InputPathType,
    ktaub: bool = False,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    pearson: bool = False,
    quadrant: bool = False,
    spearman: bool = False,
    runner: Runner = None,
) -> V3dTcorr1DOutputs:
    """
    3dTcorr1D by Nipype (interface).
    
    Computes the correlation coefficient between each voxel time series in the
    input 3D+time dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTcorr1D.html
    
    Args:
        xset: 3d+time dataset input.
        y_1d: 1d time series file input.
        ktaub: Correlation is the kendall's tau_b correlation coefficient.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        pearson: Correlation is the normal pearson correlation coefficient.
        quadrant: Correlation is the quadrant correlation coefficient.
        spearman: Correlation is the spearman (rank) correlation coefficient.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dTcorr1DOutputs`).
    """
    runner = runner or get_global_runner()
    if (
        ktaub +
        spearman +
        quadrant +
        pearson
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "ktaub,\n"
            "spearman,\n"
            "quadrant,\n"
            "pearson"
        )
    execution = runner.start_execution(V_3D_TCORR1_D_METADATA)
    cargs = []
    cargs.append("3dTcorr1D")
    cargs.extend(["", execution.input_file(xset)])
    if spearman:
        cargs.append("-spearman")
    cargs.extend(["", execution.input_file(y_1d)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dTcorr1DOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(xset).name}_correlation.nii.gz", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTcorr1DOutputs",
    "V_3D_TCORR1_D_METADATA",
    "v_3d_tcorr1_d",
]
