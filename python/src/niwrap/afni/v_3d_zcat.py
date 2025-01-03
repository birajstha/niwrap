# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_ZCAT_METADATA = Metadata(
    id="a00d1d033ba00163e081549b0d7b74b2c667d65a.boutiques",
    name="3dZcat",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dZcatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_zcat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_head: OutputPathType | None
    """AFNI HEAD file of the output dataset"""
    out_brik: OutputPathType | None
    """AFNI BRIK file of the output dataset"""


def v_3d_zcat(
    input_files: list[InputPathType],
    prefix: str | None = None,
    datum: typing.Literal["byte", "short", "float"] | None = None,
    fscale: bool = False,
    nscale: bool = False,
    verb: bool = False,
    frugal: bool = False,
    runner: Runner | None = None,
) -> V3dZcatOutputs:
    """
    Concatenates datasets in the slice (z) direction.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        input_files: Input datasets.
        prefix: Use 'pname' for the output dataset prefix name.\
            [default='zcat'].
        datum: Coerce the output data to be stored as the given type, which may\
            be byte, short, or float.
        fscale: Force scaling of the output to the maximum integer range. This\
            only has effect if the output datum is byte or short (either forced or\
            defaulted). This option is sometimes necessary to eliminate unpleasant\
            truncation artifacts.
        nscale: Don't do any scaling on output to byte or short datasets. This\
            may be especially useful when operating on mask datasets whose output\
            values are only 0's and 1's.
        verb: Print out some verbosity as the program proceeds.
        frugal: Be 'frugal' in the use of memory, at the cost of I/O time. Only\
            needed if the program runs out of memory. Note frugality cannot be\
            combined with NIFTI output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dZcatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_ZCAT_METADATA)
    cargs = []
    cargs.append("3dZcat")
    if prefix is not None:
        cargs.extend([
            "-prefix",
            prefix
        ])
    if datum is not None:
        cargs.extend([
            "-datum",
            datum
        ])
    if fscale:
        cargs.append("-fscale")
    if nscale:
        cargs.append("-nscale")
    if verb:
        cargs.append("-verb")
    if frugal:
        cargs.append("-frugal")
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V3dZcatOutputs(
        root=execution.output_file("."),
        out_head=execution.output_file(prefix + "+orig.HEAD") if (prefix is not None) else None,
        out_brik=execution.output_file(prefix + "+orig.BRIK") if (prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dZcatOutputs",
    "V_3D_ZCAT_METADATA",
    "v_3d_zcat",
]
