# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


V_3D_TCAT_METADATA = Metadata(
    id="56e988f3745e66d3c04e67286b1f710c01c03196",
    name="3dTcat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_tcat(
    in_files: InputPathType,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    rlt: typing.Literal["", "+", "++"] | None = None,
    verbose: bool = False,
    runner: Runner = None,
) -> V3dTcatOutputs:
    """
    3dTcat by Nipype (interface).
    
    Concatenate sub-bricks from input datasets into one big 3D+time dataset.
    TODO Replace InputMultiPath in_files with Traits.List, if possible. Current
    version adds extra whitespace.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTcat.html
    
    Args:
        in_files: Input file to 3dtcat.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        rlt: '' or '+' or '++'. Remove linear trends in each voxel time series
            loaded from each input dataset, separately. option -rlt removes the
            least squares fit of 'a+b*t' to each voxel time series. option -rlt+
            adds dataset mean back in. option -rlt++ adds overall mean of all
            dataset timeseries back in.
        verbose: Print out some verbose output as the program.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dTcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TCAT_METADATA)
    cargs = []
    cargs.append("3dTcat")
    if rlt is not None:
        cargs.extend(["-rlt", rlt])
    cargs.extend(["", execution.input_file(in_files)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if verbose:
        cargs.append("-verb")
    ret = V3dTcatOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_files).stem}_tcat", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTcatOutputs",
    "V_3D_TCAT_METADATA",
    "v_3d_tcat",
]
