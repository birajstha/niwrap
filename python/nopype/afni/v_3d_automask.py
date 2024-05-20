# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


V_3D_AUTOMASK_METADATA = Metadata(
    id="f41cd3ff777cae728b23a3003744395430b9db9e",
    name="3dAutomask",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dAutomaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_automask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    brain_file: OutputPathType
    """Output file from 3dautomask."""
    out_file: OutputPathType
    """Output image file name."""
    brain_file_: OutputPathType
    """Brain file (skull stripped)."""
    out_file_: OutputPathType
    """Mask file."""


def v_3d_automask(
    runner: Runner,
    in_file: InputPathType,
    clfrac: float | int | None = None,
    dilate: int | None = None,
    erode: int | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
) -> V3dAutomaskOutputs:
    """
    Automask, as implemented in Nipype (module: nipype.interfaces.afni.preprocess,
    interface: Automask).
    Create a brain-only mask of the image using AFNI 3dAutomask command
    For complete details, see the `3dAutomask Documentation.
    <https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dAutomask.html>`_
    
    Args:
        runner: Command runner
        in_file: Input file to 3dautomask.
        clfrac: Sets the clip level fraction (must be 0.1-0.9). a small value
            will tend to make the mask larger [default = 0.5].
        dilate: Dilate the mask outwards.
        erode: Erode the mask inwards.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
    Returns:
        NamedTuple of outputs (described in `V3dAutomaskOutputs`).
    """
    execution = runner.start_execution(V_3D_AUTOMASK_METADATA)
    cargs = []
    cargs.append("3dAutomask")
    cargs.append(execution.input_file(in_file))
    cargs.append("[ARGS]")
    cargs.append("[BRAIN_FILE]")
    if clfrac is not None:
        cargs.extend(["-clfrac", str(clfrac)])
    if dilate is not None:
        cargs.extend(["-dilate", str(dilate)])
    cargs.append("[ENVIRON]")
    if erode is not None:
        cargs.extend(["-erode", str(erode)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dAutomaskOutputs(
        root=execution.output_file("."),
        brain_file=execution.output_file(f"{pathlib.Path(in_file).stem}_masked", optional=True),
        out_file=execution.output_file(f"{pathlib.Path(in_file).stem}_mask", optional=True),
        brain_file_=execution.output_file(f"brain_file", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret
