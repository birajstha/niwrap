# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

REG_TRANSFORM_METADATA = Metadata(
    id="056064e1a05ea59a3628d701f5818d4dc74807fc",
    name="reg_transform",
)


class RegTransformOutputs(typing.NamedTuple):
    """
    Output object returned when calling `reg_transform(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cpp2def_output_file: OutputPathType | None
    """File containing the CPP to DEF converted deformation field."""
    comp1_output_file: OutputPathType | None
    """File containing the composed deformation field from two control point lattices."""
    comp2_output_file: OutputPathType | None
    """File containing the composed deformation field from a deformation field and a control point lattice."""
    comp3_output_file: OutputPathType | None
    """File containing the composed deformation field from two deformation fields."""
    def2disp_output_file: OutputPathType | None
    """File containing the converted displacement field from a deformation field."""
    disp2def_output_file: OutputPathType | None
    """File containing the converted deformation field from a displacement field."""
    upd_sform_output_file: OutputPathType | None
    """File containing the updated image with modified sform."""
    aff2def_output_file: OutputPathType | None
    """File containing the composed deformation field from a non-rigid and an affine transformation."""
    inv_affine_output_file: OutputPathType | None
    """File containing the inverted affine matrix."""
    comp_aff_output_file: OutputPathType | None
    """File containing the composed affine matrix."""


def reg_transform(
    reference_image: InputPathType,
    cpp2def_input: InputPathType | None = None,
    cpp2def_output: InputPathType | None = None,
    comp1_cpp2: InputPathType | None = None,
    comp1_cpp1: InputPathType | None = None,
    comp1_output: InputPathType | None = None,
    comp2_cpp: InputPathType | None = None,
    comp2_def: InputPathType | None = None,
    comp2_output: InputPathType | None = None,
    comp3_def2: InputPathType | None = None,
    comp3_def1: InputPathType | None = None,
    comp3_output: InputPathType | None = None,
    def2disp_input: InputPathType | None = None,
    def2disp_output: InputPathType | None = None,
    disp2def_input: InputPathType | None = None,
    disp2def_output: InputPathType | None = None,
    upd_sform_image: InputPathType | None = None,
    upd_sform_affine: InputPathType | None = None,
    upd_sform_output: InputPathType | None = None,
    aff2def_affine: InputPathType | None = None,
    aff2def_target: InputPathType | None = None,
    aff2def_cpp_or_def: InputPathType | None = None,
    aff2def_output: InputPathType | None = None,
    inv_affine_input: InputPathType | None = None,
    inv_affine_output: InputPathType | None = None,
    comp_aff_1st: InputPathType | None = None,
    comp_aff_2nd: InputPathType | None = None,
    comp_aff_output: InputPathType | None = None,
    runner: Runner = None,
) -> RegTransformOutputs:
    """
    reg_transform by Marc Modat.
    
    Tool for performing various transformation operations on medical images
    including control point to deformation conversion, composition of
    transformations, and converting between deformation and displacement fields.
    
    More information: https://example.com/reg_transform_docs
    
    Args:
        reference_image: Filename of the reference image
        cpp2def_input: Conversion from control point position to deformation
            field. Filename of input lattice of control point positions (CPP).
        cpp2def_output: Filename of the output deformation field image (DEF).
        comp1_cpp2: Composition of two lattices of control points.
            CPP2(CPP1(x)). Filename of lattice of control point that contains the
            second deformation (CPP2).
        comp1_cpp1: Filename of lattice of control point that contains the
            initial deformation (CPP1).
        comp1_output: Filename of the output deformation field.
        comp2_cpp: Composition of a deformation field with a lattice of control
            points. CPP(DEF(x)). Filename of lattice of control point that contains
            the second deformation (CPP).
        comp2_def: Filename of the deformation field to be used as initial
            deformation (DEF).
        comp2_output: Filename of the output deformation field.
        comp3_def2: Composition of two deformation fields. DEF2(DEF1(x)).
            Filename of the second deformation field (DEF2).
        comp3_def1: Filename of the first deformation field (DEF1).
        comp3_output: Filename of the output deformation field.
        def2disp_input: Convert a deformation field into a displacement field.
            Filename of deformation field x'=T(x).
        def2disp_output: Filename of displacement field x'=x+T(x).
        disp2def_input: Convert a displacement field into a deformation field.
            Filename of displacement field x'=x+T(x).
        disp2def_output: Filename of deformation field x'=T(x).
        upd_sform_image: Update the sform of a floating (source) image using an
            affine transformation. Filename of image to be updated.
        upd_sform_affine: Affine transformation defined as Affine x Reference =
            Floating. Filename of affine transformation.
        upd_sform_output: Updated image filename.
        aff2def_affine: Compose a non-rigid with an affine. Filename of affine
            transformation.
        aff2def_target: Image used as a target for the non-rigid step.
        aff2def_cpp_or_def: Reference image (B). Filename of control point
            position or deformation field.
        aff2def_output: Output deformation field filename.
        inv_affine_input: Invert an affine transformation matrix. Filename of
            input affine matrix.
        inv_affine_output: Filename of inverted affine matrix.
        comp_aff_1st: Compose two affine transformation matrices. Filename of
            first affine matrix.
        comp_aff_2nd: Filename of second affine matrix.
        comp_aff_output: Filename of composed affine matrix result.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `RegTransformOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(REG_TRANSFORM_METADATA)
    cargs = []
    cargs.append("reg_transform")
    cargs.append("-ref")
    cargs.extend(["-ref", execution.input_file(reference_image)])
    cargs.append("[OPTIONS]")
    ret = RegTransformOutputs(
        root=execution.output_file("."),
        cpp2def_output_file=execution.output_file(f"{pathlib.Path(cpp2def_output).name}", optional=True) if cpp2def_output is not None else None,
        comp1_output_file=execution.output_file(f"{pathlib.Path(comp1_output).name}", optional=True) if comp1_output is not None else None,
        comp2_output_file=execution.output_file(f"{pathlib.Path(comp2_output).name}", optional=True) if comp2_output is not None else None,
        comp3_output_file=execution.output_file(f"{pathlib.Path(comp3_output).name}", optional=True) if comp3_output is not None else None,
        def2disp_output_file=execution.output_file(f"{pathlib.Path(def2disp_output).name}", optional=True) if def2disp_output is not None else None,
        disp2def_output_file=execution.output_file(f"{pathlib.Path(disp2def_output).name}", optional=True) if disp2def_output is not None else None,
        upd_sform_output_file=execution.output_file(f"{pathlib.Path(upd_sform_output).name}", optional=True) if upd_sform_output is not None else None,
        aff2def_output_file=execution.output_file(f"{pathlib.Path(aff2def_output).name}", optional=True) if aff2def_output is not None else None,
        inv_affine_output_file=execution.output_file(f"{pathlib.Path(inv_affine_output).name}", optional=True) if inv_affine_output is not None else None,
        comp_aff_output_file=execution.output_file(f"{pathlib.Path(comp_aff_output).name}", optional=True) if comp_aff_output is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "REG_TRANSFORM_METADATA",
    "RegTransformOutputs",
    "reg_transform",
]
