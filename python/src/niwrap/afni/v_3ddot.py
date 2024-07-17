# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DDOT_METADATA = Metadata(
    id="debf6cb85802a4a8ec51b6321fe32b4c15ed75f0",
    name="3ddot",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3ddotOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3ddot(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    result: OutputPathType
    """Resulting coefficient or statistical values printed to stdout"""


def v_3ddot(
    input_datasets: list[InputPathType],
    mask: InputPathType | None = None,
    mrange: list[float | int] | None = None,
    demean: bool = False,
    docor: bool = False,
    dodot: bool = False,
    docoef: bool = False,
    dosums: bool = False,
    doeta2: bool = False,
    dodice: bool = False,
    show_labels: bool = False,
    upper: bool = False,
    full: bool = False,
    v_1_d: bool = False,
    niml: bool = False,
    runner: Runner | None = None,
) -> V3ddotOutputs:
    """
    3ddot by AFNI Team.
    
    Computes correlation coefficients between sub-brick pairs.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3ddot.html
    
    Args:
        input_datasets: List of input datasets to be used (e.g. img1+orig,\
            img2+orig).
        mask: Dataset to be used as a mask; only voxels with nonzero values\
            will be averaged.
        mrange: Restrict mask values to those between a and b (inclusive) for\
            masking purposes.
        demean: Remove the mean from each volume prior to computing the\
            correlation.
        docor: Return the correlation coefficient (default).
        dodot: Return the dot product (unscaled).
        docoef: Return the least square fit coefficients {a,b}.
        dosums: Return xbar, ybar, variance, covariance, and correlation\
            coefficient.
        doeta2: Return eta-squared (Cohen, NeuroImage 2008).
        dodice: Return the Dice coefficient (the Sorensen-Dice index).
        show_labels: Print sub-brick labels to help identify what is being\
            correlated.
        upper: Compute upper triangular matrix.
        full: Compute the whole matrix.
        v_1_d: Add comment headings for the 1D format.
        niml: Write output in NIML 1D format.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3ddotOutputs`).
    """
    runner = runner or get_global_runner()
    if mrange is not None and (len(mrange) != 2): 
        raise ValueError(f"Length of 'mrange' must be 2 but was {len(mrange)}")
    execution = runner.start_execution(V_3DDOT_METADATA)
    cargs = []
    cargs.append("3ddot")
    cargs.append("[OPTIONS]")
    cargs.extend([execution.input_file(f) for f in input_datasets])
    ret = V3ddotOutputs(
        root=execution.output_file("."),
        result=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3ddotOutputs",
    "V_3DDOT_METADATA",
    "v_3ddot",
]
