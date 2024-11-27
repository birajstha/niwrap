# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_SLICE_NDICE_METADATA = Metadata(
    id="2632d37affeb0b9dca727cb8206f5ac9def40039.boutiques",
    name="3dSliceNDice",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dSliceNdiceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_slice_ndice(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_rl: OutputPathType
    """Output file containing Dice coefficients along the right-left axis."""
    output_ap: OutputPathType
    """Output file containing Dice coefficients along the anterior-posterior
    axis."""
    output_is: OutputPathType
    """Output file containing Dice coefficients along the inferior-superior
    axis."""


def v_3d_slice_ndice(
    infile_a: InputPathType,
    infile_b: InputPathType,
    output_prefix: str,
    out_domain: typing.Literal["all", "AorB", "AandB", "Amask", "Bmask"] | None = None,
    no_cmd_echo: bool = False,
    runner: Runner | None = None,
) -> V3dSliceNdiceOutputs:
    """
    Calculates the Dice coefficient between two volumes on a slice-by-slice basis.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        infile_a: Input dataset A (e.g. mask_1.nii.gz).
        infile_b: Input dataset B (e.g. mask_2.nii.gz).
        output_prefix: Prefix for output files (e.g. result_prefix).
        out_domain: Specify which slices to include in the Dice coefficient\
            report. Options are: all (default), AorB, AandB, Amask, Bmask.
        no_cmd_echo: Turn OFF recording the command line call in the output\
            *.1D files. Default is to do the recording.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dSliceNdiceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_SLICE_NDICE_METADATA)
    cargs = []
    cargs.append("3dSliceNDice")
    cargs.extend([
        "-insetA",
        execution.input_file(infile_a)
    ])
    cargs.extend([
        "-insetB",
        execution.input_file(infile_b)
    ])
    cargs.extend([
        "-prefix",
        output_prefix
    ])
    if out_domain is not None:
        cargs.extend([
            "-out_domain",
            out_domain
        ])
    if no_cmd_echo:
        cargs.append("-no_cmd_echo")
    ret = V3dSliceNdiceOutputs(
        root=execution.output_file("."),
        output_rl=execution.output_file(output_prefix + "_0_RL.1D"),
        output_ap=execution.output_file(output_prefix + "_1_AP.1D"),
        output_is=execution.output_file(output_prefix + "_2_IS.1D"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dSliceNdiceOutputs",
    "V_3D_SLICE_NDICE_METADATA",
    "v_3d_slice_ndice",
]
