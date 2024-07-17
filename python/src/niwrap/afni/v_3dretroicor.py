# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DRETROICOR_METADATA = Metadata(
    id="a4dfe4401ac6e19545ac1cd2e19534215c5202d4",
    name="3dretroicor",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dretroicorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dretroicor(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    corrected_dataset: OutputPathType | None
    """Corrected dataset output."""
    output_cardiac_phase: OutputPathType | None
    """Cardiac phase output file."""
    output_resp_phase: OutputPathType | None
    """Respiratory phase output file."""


def v_3dretroicor(
    dataset: InputPathType,
    ignore: float | int | None = None,
    prefix: str | None = None,
    card: InputPathType | None = None,
    cardphase: str | None = None,
    threshold: float | int | None = None,
    resp: InputPathType | None = None,
    respphase: str | None = None,
    order: float | int | None = None,
    runner: Runner | None = None,
) -> V3dretroicorOutputs:
    """
    3dretroicor by AFNI Team.
    
    Performs Retrospective Image Correction for physiological motion effects
    using a modified RETROICOR algorithm.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dretroicor.html
    
    Args:
        dataset: 3D+time dataset to process.
        ignore: The number of initial timepoints to ignore in the input. These\
            points will be passed through uncorrected.
        prefix: Prefix for new, corrected dataset.
        card: 1D cardiac data file for cardiac correction.
        cardphase: Filename for 1D cardiac phase output.
        threshold: Threshold for detection of R-wave peaks in input. Make sure\
            it's above the background noise level; try 3/4 or 4/5 times range plus\
            minimum.
        resp: 1D respiratory waveform data for correction.
        respphase: Filename for 1D respiratory phase output.
        order: The order of the correction. Higher-order terms yield little\
            improvement according to Glover et al.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dretroicorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DRETROICOR_METADATA)
    cargs = []
    cargs.append("3dretroicor")
    if ignore is not None:
        cargs.extend(["-ignore", str(ignore)])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if card is not None:
        cargs.extend(["-card", execution.input_file(card)])
    if cardphase is not None:
        cargs.extend(["-cardphase", cardphase])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
    if resp is not None:
        cargs.extend(["-resp", execution.input_file(resp)])
    if respphase is not None:
        cargs.extend(["-respphase", respphase])
    if order is not None:
        cargs.extend(["-order", str(order)])
    cargs.append(execution.input_file(dataset))
    ret = V3dretroicorOutputs(
        root=execution.output_file("."),
        corrected_dataset=execution.output_file(f"{prefix}.nii.gz", optional=True) if prefix is not None else None,
        output_cardiac_phase=execution.output_file(f"{cardphase}", optional=True) if cardphase is not None else None,
        output_resp_phase=execution.output_file(f"{respphase}", optional=True) if respphase is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dretroicorOutputs",
    "V_3DRETROICOR_METADATA",
    "v_3dretroicor",
]
