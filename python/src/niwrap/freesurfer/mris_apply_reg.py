# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_APPLY_REG_METADATA = Metadata(
    id="40a2e3c6f81394afec96eee658a860b6f21b85f5.boutiques",
    name="mris_apply_reg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisApplyRegOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_apply_reg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_result: OutputPathType
    """The output file resulting from registration"""


def mris_apply_reg(
    src_input: InputPathType,
    trg_output: InputPathType,
    streg_pair: str,
    src_label: InputPathType | None = None,
    src_annotation: InputPathType | None = None,
    src_xyz: InputPathType | None = None,
    jacobian: bool = False,
    no_reverse: bool = False,
    rand_noise: bool = False,
    replace_ones: bool = False,
    center_output: bool = False,
    curv_format: bool = False,
    lta_transform: str | None = None,
    lta_patch_transform: str | None = None,
    reverse_surface: str | None = None,
    patch_apply: str | None = None,
    save_vertex_pair: InputPathType | None = None,
    m3z_transform: str | None = None,
    inv_m3z_transform: str | None = None,
    src_reg_scale: float | None = None,
    trg_reg_scale: float | None = None,
    debug_mode: bool = False,
    check_options: bool = False,
    runner: Runner | None = None,
) -> MrisApplyRegOutputs:
    """
    Apply surface registration in FreeSurfer.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        src_input: Source values (surface overlay).
        trg_output: Target output file.
        streg_pair: Source and target registration file pair.
        src_label: Source label file (implies --no-rev).
        src_annotation: Source annotation file (implies --no-rev).
        src_xyz: XYZ coordinates from the given surface file as input.
        jacobian: Use jacobian correction.
        no_reverse: Do not do reverse mapping.
        rand_noise: Replace input with white Gaussian noise.
        replace_ones: Replace input with ones.
        center_output: Place the center of the output surface at (0,0,0).
        curv_format: Save output in curvature file format.
        lta_transform: Apply LTA transform to the surface.
        lta_patch_transform: Apply LTA transform to surface patch.
        reverse_surface: LR reverse surface with optional patch.
        patch_apply: Apply patch for each --streg.
        save_vertex_pair: Save vertex pairs from source and target surfaces.
        m3z_transform: Apply M3Z transform.
        inv_m3z_transform: Apply inverse M3Z transform.
        src_reg_scale: Scale the coordinates of the first surface.
        trg_reg_scale: Scale the coordinates of the last surface.
        debug_mode: Turn on debugging.
        check_options: Check options without executing anything.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisApplyRegOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_APPLY_REG_METADATA)
    cargs = []
    cargs.append("mris_apply_reg")
    cargs.extend([
        "--src",
        execution.input_file(src_input)
    ])
    cargs.extend([
        "--trg",
        execution.input_file(trg_output)
    ])
    cargs.extend([
        "--streg",
        streg_pair
    ])
    cargs.append("[STREG_ADDITIONAL...]")
    if src_label is not None:
        cargs.extend([
            "--src-label",
            execution.input_file(src_label)
        ])
    if src_annotation is not None:
        cargs.extend([
            "--src-annot",
            execution.input_file(src_annotation)
        ])
    if src_xyz is not None:
        cargs.extend([
            "--src-xyz",
            execution.input_file(src_xyz)
        ])
    if jacobian:
        cargs.append("--jac")
    if no_reverse:
        cargs.append("--no-rev")
    if rand_noise:
        cargs.append("--randn")
    if replace_ones:
        cargs.append("--ones")
    if center_output:
        cargs.append("--center")
    if curv_format:
        cargs.append("--curv")
    if lta_transform is not None:
        cargs.extend([
            "--lta",
            lta_transform
        ])
    if lta_patch_transform is not None:
        cargs.extend([
            "--lta-patch",
            lta_patch_transform
        ])
    if reverse_surface is not None:
        cargs.extend([
            "--reverse",
            reverse_surface
        ])
    if patch_apply is not None:
        cargs.extend([
            "--patch",
            patch_apply
        ])
    if save_vertex_pair is not None:
        cargs.extend([
            "--stvpair",
            execution.input_file(save_vertex_pair)
        ])
    if m3z_transform is not None:
        cargs.extend([
            "--m3z",
            m3z_transform
        ])
    if inv_m3z_transform is not None:
        cargs.extend([
            "--inv-m3z",
            inv_m3z_transform
        ])
    if src_reg_scale is not None:
        cargs.extend([
            "--src-reg-scale",
            str(src_reg_scale)
        ])
    if trg_reg_scale is not None:
        cargs.extend([
            "--trg-reg-scale",
            str(trg_reg_scale)
        ])
    if debug_mode:
        cargs.append("--debug")
    if check_options:
        cargs.append("--checkopts")
    ret = MrisApplyRegOutputs(
        root=execution.output_file("."),
        output_result=execution.output_file(pathlib.Path(trg_output).name),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_APPLY_REG_METADATA",
    "MrisApplyRegOutputs",
    "mris_apply_reg",
]