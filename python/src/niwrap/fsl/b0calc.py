# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

B0CALC_METADATA = Metadata(
    id="5c6e6293eb09efa71410f03633aab4698727a978",
    name="b0calc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class B0calcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `b0calc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    b0_output: OutputPathType
    """B0 output volume"""
    b0_output_x: OutputPathType
    """B0 x-component output volume (if --xyz is specified)"""
    b0_output_y: OutputPathType
    """B0 y-component output volume (if --xyz is specified)"""
    b0_output_z: OutputPathType
    """B0 z-component output volume (if --xyz is specified)"""


def b0calc(
    input_file: InputPathType,
    output_file: str,
    zero_order_x: float | int | None = None,
    zero_order_y: float | int | None = None,
    zero_order_z: float | int | None = None,
    b0_x: float | int | None = None,
    b0_y: float | int | None = None,
    b0_z: float | int | None = None,
    delta: float | int | None = None,
    chi0: float | int | None = None,
    xyz_flag: bool = False,
    extend_boundary: float | int | None = None,
    direct_conv: bool = False,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner | None = None,
) -> B0calcOutputs:
    """
    b0calc by University of Oxford.
    
    B0 field calculation program.
    
    More information:
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FUGUE/Guide#fieldmapcreation
    
    Args:
        input_file: Filename of input image (usually a tissue/air segmentation).
        output_file: Filename of B0 output volume.
        zero_order_x: Value for zeroth-order x-gradient field (per mm);\
            default=0.
        zero_order_y: Value for zeroth-order y-gradient field (per mm);\
            default=0.
        zero_order_z: Value for zeroth-order z-gradient field (per mm);\
            default=0.
        b0_x: Value for zeroth-order B0 field (x-component); default=0.
        b0_y: Value for zeroth-order B0 field (y-component); default=0.
        b0_z: Value for zeroth-order B0 field (z-component); default=1.
        delta: Delta value (chi_tissue - chi_air); default=-9.45e-6.
        chi0: Value for susceptibility of air; default=+4e-7.
        xyz_flag: Calculate and save all 3 field components (i.e. x,y,z).
        extend_boundary: Relative proportion to extend voxels at boundary;\
            default=1.
        direct_conv: Use direct (image space) convolution, not FFT.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `B0calcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(B0CALC_METADATA)
    cargs = []
    cargs.append("b0calc")
    cargs.append("-i")
    cargs.extend(["-i", execution.input_file(input_file)])
    cargs.append("-o")
    cargs.extend(["-o", output_file])
    if zero_order_x is not None:
        cargs.extend(["--gx", str(zero_order_x)])
    if zero_order_y is not None:
        cargs.extend(["--gy", str(zero_order_y)])
    if zero_order_z is not None:
        cargs.extend(["--gz", str(zero_order_z)])
    if b0_x is not None:
        cargs.extend(["--b0x", str(b0_x)])
    if b0_y is not None:
        cargs.extend(["--b0y", str(b0_y)])
    if b0_z is not None:
        cargs.extend(["--b0", str(b0_z)])
    if delta is not None:
        cargs.extend(["-d", str(delta)])
    if chi0 is not None:
        cargs.extend(["--chi0", str(chi0)])
    if xyz_flag:
        cargs.append("--xyz")
    if extend_boundary is not None:
        cargs.extend(["--extendboundary", str(extend_boundary)])
    if direct_conv:
        cargs.append("--directconv")
    if verbose_flag:
        cargs.append("-v")
    ret = B0calcOutputs(
        root=execution.output_file("."),
        b0_output=execution.output_file(f"{output_file}"),
        b0_output_x=execution.output_file(f"{output_file}_x", optional=True),
        b0_output_y=execution.output_file(f"{output_file}_y", optional=True),
        b0_output_z=execution.output_file(f"{output_file}_z", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "B0CALC_METADATA",
    "B0calcOutputs",
    "b0calc",
]
