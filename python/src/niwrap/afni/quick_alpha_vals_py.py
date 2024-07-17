# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

QUICK_ALPHA_VALS_PY_METADATA = Metadata(
    id="a02d8b48e4b639b6d866edfe5a0cbfa329f388c8",
    name="quick.alpha.vals.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class QuickAlphaValsPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quick_alpha_vals_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    alpha_table: OutputPathType
    """Generated alpha table file"""


def quick_alpha_vals_py(
    max_file: InputPathType,
    niter: int | None = None,
    runner: Runner | None = None,
) -> QuickAlphaValsPyOutputs:
    """
    quick.alpha.vals.py by AFNI Team.
    
    Generate an alpha table from slow_surf_clustsim.py results.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/quick.alpha.vals.py.html
    
    Args:
        max_file: File containing maximum z values.
        niter: Number of iterations that should be in the z file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuickAlphaValsPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUICK_ALPHA_VALS_PY_METADATA)
    cargs = []
    cargs.append("quick.alpha.vals.py")
    if niter is not None:
        cargs.extend(["-niter", str(niter)])
    cargs.append(execution.input_file(max_file))
    ret = QuickAlphaValsPyOutputs(
        root=execution.output_file("."),
        alpha_table=execution.output_file(f"alpha_table.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QUICK_ALPHA_VALS_PY_METADATA",
    "QuickAlphaValsPyOutputs",
    "quick_alpha_vals_py",
]
