# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

C3D_AFFINE_TOOL_METADATA = Metadata(
    id="8d8ee864fd8cb9cd3fa4f3747a017ca95294bc58",
    name="C3dAffineTool",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class C3dAffineToolOutputs(typing.NamedTuple):
    """
    Output object returned when calling `c3d_affine_tool(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    itk_transform_outfile: OutputPathType | None
    """Output ITK transform file."""
    irtk_transform_outfile: OutputPathType | None
    """Output IRTK transform file."""
    matrix_transform_outfile: OutputPathType | None
    """Write output matrix."""


def c3d_affine_tool(
    transform_file: InputPathType,
    reference_file: InputPathType | None = None,
    source_file: InputPathType | None = None,
    fsl2ras: bool = False,
    ras2fsl: bool = False,
    determinant: bool = False,
    invert: bool = False,
    multiply: bool = False,
    sqrt: bool = False,
    out_matfile: str | None = None,
    sform_file: InputPathType | None = None,
    itk_transform: InputPathType | None = None,
    out_itk_transform: str | None = None,
    irtk_transform: InputPathType | None = None,
    out_irtk_transform: str | None = None,
    info: bool = False,
    info_full: bool = False,
    runner: Runner = None,
) -> C3dAffineToolOutputs:
    """
    C3dAffineTool by ITK-Snap Team.
    
    RAS affine transform tool.
    
    Args:
        transform_file: file or string representing the transform.
        reference_file: Set reference (fixed) image - only for -fsl2ras and\
            -ras2fsl.
        source_file: Set source (moving) image - only for -fsl2ras and\
            -ras2fsl.
        fsl2ras: Convert FSL to RAS.
        ras2fsl: Convert RAS to FSL.
        determinant: Print the determinant.
        invert: Invert matrix.
        multiply: Multiply matrices.
        sqrt: Matrix square root (i.e., Q s.t. A = Q * Q).
        out_matfile: Write output matrix.
        sform_file: Read matrix from NifTI sform.
        itk_transform: Import ITK transform.
        out_itk_transform: Export ITK transform.
        irtk_transform: Import IRTK .dof format transform.
        out_irtk_transform: Export IRTK .dof format transform.
        info: Print matrix.
        info_full: Print matrix and more detail about the transform.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `C3dAffineToolOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(C3D_AFFINE_TOOL_METADATA)
    cargs = []
    cargs.append("c3d_affine_tool")
    if reference_file is not None:
        cargs.extend(["-ref", execution.input_file(reference_file)])
    if source_file is not None:
        cargs.extend(["-src", execution.input_file(source_file)])
    cargs.append(execution.input_file(transform_file))
    if sform_file is not None:
        cargs.extend(["-sform", execution.input_file(sform_file)])
    if out_matfile is not None:
        cargs.extend(["-o", out_matfile])
    if fsl2ras:
        cargs.append("-fsl2ras")
    if ras2fsl:
        cargs.append("-ras2fsl")
    if invert:
        cargs.append("-inv")
    if determinant:
        cargs.append("-det")
    if multiply:
        cargs.append("-mult")
    if sqrt:
        cargs.append("-sqrt")
    if itk_transform is not None:
        cargs.extend(["-itk", execution.input_file(itk_transform)])
    if out_itk_transform is not None:
        cargs.extend(["-oitk", out_itk_transform])
    if irtk_transform is not None:
        cargs.extend(["-irtk", execution.input_file(irtk_transform)])
    if out_irtk_transform is not None:
        cargs.extend(["-oirtk", out_irtk_transform])
    if info:
        cargs.append("-info")
    if info_full:
        cargs.append("-info-full")
    ret = C3dAffineToolOutputs(
        root=execution.output_file("."),
        itk_transform_outfile=execution.output_file(f"{out_itk_transform}.txt", optional=True) if out_itk_transform is not None else None,
        irtk_transform_outfile=execution.output_file(f"{out_irtk_transform}.dof", optional=True) if out_irtk_transform is not None else None,
        matrix_transform_outfile=execution.output_file(f"{out_matfile}.mat", optional=True) if out_matfile is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "C3D_AFFINE_TOOL_METADATA",
    "C3dAffineToolOutputs",
    "c3d_affine_tool",
]
