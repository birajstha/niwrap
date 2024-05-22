# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


V_3D_BLUR_TO_FWHM_METADATA = Metadata(
    id="bfa4a9cfcba16a02c729a45e50647d824f207141",
    name="3dBlurToFWHM",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dBlurToFwhmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_blur_to_fwhm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""


def v_3d_blur_to_fwhm(
    in_file: InputPathType,
    automask: bool = False,
    blurmaster: InputPathType | None = None,
    fwhm: float | int | None = None,
    fwhmxy: float | int | None = None,
    mask: InputPathType | None = None,
    num_threads: int | None = 1,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    runner: Runner = None,
) -> V3dBlurToFwhmOutputs:
    """
    3dBlurToFWHM by Nipype (interface).
    
    Blurs a 'master' dataset until it reaches a specified FWHM smoothness
    (approximately).
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dBlurToFWHM.html
    
    Args:
        in_file: The dataset that will be smoothed.
        automask: Create an automask from the input dataset.
        blurmaster: The dataset whose smoothness controls the process.
        fwhm: Blur until the 3d fwhm reaches this value (in mm).
        fwhmxy: Blur until the 2d (x,y)-plane fwhm reaches this value (in mm).
        mask: Mask dataset, if desired. voxels not in mask will be set to zero
            in output.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `V3dBlurToFwhmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_BLUR_TO_FWHM_METADATA)
    cargs = []
    cargs.append("3dBlurToFWHM")
    if automask:
        cargs.append("-automask")
    if blurmaster is not None:
        cargs.extend(["-blurmaster", execution.input_file(blurmaster)])
    if fwhm is not None:
        cargs.extend(["-FWHM", str(fwhm)])
    if fwhmxy is not None:
        cargs.extend(["-FWHMxy", str(fwhmxy)])
    cargs.extend(["-input", execution.input_file(in_file)])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if num_threads is not None:
        cargs.append(str(num_threads))
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    ret = V3dBlurToFwhmOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).stem}_afni", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dBlurToFwhmOutputs",
    "V_3D_BLUR_TO_FWHM_METADATA",
    "v_3d_blur_to_fwhm",
]
