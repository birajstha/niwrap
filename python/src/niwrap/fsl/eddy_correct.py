# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EDDY_CORRECT_METADATA = Metadata(
    id="b3db82860cab20dc3434db50628877de4771c002.boutiques",
    name="eddy_correct",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class EddyCorrectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `eddy_correct(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_4d_output: OutputPathType
    """Corrected 4D output image file"""


def eddy_correct(
    v_4d_input: InputPathType,
    v_4d_output: str,
    reference_no: int,
    interp_method: typing.Literal["trilinear", "spline"] | None = "trilinear",
    runner: Runner | None = None,
) -> EddyCorrectOutputs:
    """
    Eddy current correction tool for FSL.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        v_4d_input: Input 4D image file (e.g., dti.nii.gz).
        v_4d_output: Output 4D image file (e.g., dti_corrected.nii.gz).
        reference_no: Reference number.
        interp_method: Interpolation method to use: 'trilinear' or 'spline'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EddyCorrectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EDDY_CORRECT_METADATA)
    cargs = []
    cargs.append("eddy_correct")
    cargs.append(execution.input_file(v_4d_input))
    cargs.append(v_4d_output)
    cargs.append(str(reference_no))
    if interp_method is not None:
        cargs.append(interp_method)
    ret = EddyCorrectOutputs(
        root=execution.output_file("."),
        corrected_4d_output=execution.output_file(v_4d_output + ".nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EDDY_CORRECT_METADATA",
    "EddyCorrectOutputs",
    "eddy_correct",
]
