# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


V_3D_SKULL_STRIP_METADATA = Metadata(
    id="007e686776f36f21fa2495fa88429784cca895ba",
    name="3dSkullStrip",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dSkullStripOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_skull_strip(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_skull_strip(
    runner: Runner,
    in_file: InputPathType,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
) -> V3dSkullStripOutputs:
    """
    A program to extract the brain from surrounding tissue from MRI T1-weighted
    images.
    
    Args:
        runner: Command runner
        in_file: Input file to 3dskullstrip.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
    Returns:
        NamedTuple of outputs (described in `V3dSkullStripOutputs`).
    """
    execution = runner.start_execution(V_3D_SKULL_STRIP_METADATA)
    cargs = []
    cargs.append("3dSkullStrip")
    cargs.extend(["-input", execution.input_file(in_file)])
    cargs.append("[ARGS]")
    cargs.append("[ENVIRON]")
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dSkullStripOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).stem}_skullstrip", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
