# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TCALC_METADATA = Metadata(
    id="e56e37a68d36f10479f279575f325cac47436e0b",
    name="tcalc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl:6.0.5",
)


class TcalcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tcalc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image_file: OutputPathType
    """The output image generated after resampling"""
    original_output_image_file: OutputPathType
    """The original non-resampled output image, if save flag is used"""


def tcalc(
    input_image: InputPathType,
    output_image: str,
    echo_time: float | int | None = None,
    repetition_time: float | int | None = None,
    mrpar_file: InputPathType | None = None,
    num_voxel_x: float | int | None = None,
    num_voxel_y: float | int | None = None,
    num_voxel_z: float | int | None = None,
    voxel_size_x: float | int | None = None,
    voxel_size_y: float | int | None = None,
    voxel_size_z: float | int | None = None,
    start_position: float | int | None = None,
    noise_sigma: float | int | None = None,
    save_flag: bool = False,
    verbose_flag: bool = False,
    runner: Runner | None = None,
) -> TcalcOutputs:
    """
    tcalc by Tejas Pendse.
    
    Resample a 4D phantom for theoretical calculations.
    
    Args:
        input_image: Input image (4D phantom for theoretical calculations).
        output_image: Output image.
        echo_time: Echo Time (TE) in seconds [e.g., T1-weighted images for 3T\
            TE=0.01 s].
        repetition_time: Repetition Time (TR) in seconds [e.g., T1-weighted\
            images for 3T TR=0.7 s].
        mrpar_file: MRpar File.
        num_voxel_x: Number of Voxels along X (default: phantom).
        num_voxel_y: Number of Voxels along Y (default: phantom).
        num_voxel_z: Number of Voxels along Z (default: phantom).
        voxel_size_x: Size of voxels along X (default: phantom).
        voxel_size_y: Size of voxels along Y (default: phantom).
        voxel_size_z: Size of voxels along Z i.e., number of slices (default:\
            phantom).
        start_position: Starting position of the volume in mm (default = 0mm).
        noise_sigma: Add noise with given sigma (default: 0 i.e., no noise).
        save_flag: Save original non-resample output image.
        verbose_flag: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TcalcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCALC_METADATA)
    cargs = []
    cargs.append("resample")
    cargs.append("-i")
    cargs.extend(["--input", execution.input_file(input_image)])
    cargs.append("-o")
    cargs.extend(["--output", output_image])
    if echo_time is not None:
        cargs.extend(["--te", str(echo_time)])
    if repetition_time is not None:
        cargs.extend(["--tr", str(repetition_time)])
    if mrpar_file is not None:
        cargs.extend(["--mrpar", execution.input_file(mrpar_file)])
    if num_voxel_x is not None:
        cargs.extend(["--nx", str(num_voxel_x)])
    if num_voxel_y is not None:
        cargs.extend(["--ny", str(num_voxel_y)])
    if num_voxel_z is not None:
        cargs.extend(["--nz", str(num_voxel_z)])
    if voxel_size_x is not None:
        cargs.extend(["--dx", str(voxel_size_x)])
    if voxel_size_y is not None:
        cargs.extend(["--dy", str(voxel_size_y)])
    if voxel_size_z is not None:
        cargs.extend(["--dz", str(voxel_size_z)])
    if start_position is not None:
        cargs.extend(["--zstart", str(start_position)])
    if noise_sigma is not None:
        cargs.extend(["--sigma", str(noise_sigma)])
    if save_flag:
        cargs.append("--save")
    if verbose_flag:
        cargs.append("--verbose")
    ret = TcalcOutputs(
        root=execution.output_file("."),
        output_image_file=execution.output_file(f"{output_image}"),
        original_output_image_file=execution.output_file(f"{output_image}_original", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCALC_METADATA",
    "TcalcOutputs",
    "tcalc",
]
