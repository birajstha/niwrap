# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MRIS_WARP_METADATA = Metadata(
    id="a60346ae5a51f63c7f32e60f45dc20db2e519c51.boutiques",
    name="mris_warp",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MrisWarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mris_warp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_surface: OutputPathType | None
    """Output surface file"""


def mris_warp(
    deformvol: str | None = None,
    m3z: str | None = None,
    regfile: str | None = None,
    surf: str | None = None,
    out: str | None = None,
    abs_: bool = False,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> MrisWarpOutputs:
    """
    This program will warp a surface using a specified deformation field.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        deformvol: Volume containing deformation.
        m3z: M3Z file containing deformation.
        regfile: register.dat file between surface and volume.
        surf: Surface file to warp.
        out: Name for output surface (if does not contain '/', outputs to same\
            directory as input surface).
        abs_: Absolute coordinate displacement convention (default).
        help_: Print out information on how to use this program.
        version: Print out version and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MrisWarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MRIS_WARP_METADATA)
    cargs = []
    cargs.append("mris_warp")
    if deformvol is not None:
        cargs.extend([
            "--deformvol",
            deformvol
        ])
    if m3z is not None:
        cargs.extend([
            "--m3z",
            m3z
        ])
    if regfile is not None:
        cargs.extend([
            "--reg",
            regfile
        ])
    if surf is not None:
        cargs.extend([
            "--surf",
            surf
        ])
    if out is not None:
        cargs.extend([
            "--out",
            out
        ])
    if abs_:
        cargs.append("--abs")
    if help_:
        cargs.append("--help")
    if version:
        cargs.append("--version")
    ret = MrisWarpOutputs(
        root=execution.output_file("."),
        output_surface=execution.output_file(out) if (out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MRIS_WARP_METADATA",
    "MrisWarpOutputs",
    "mris_warp",
]
