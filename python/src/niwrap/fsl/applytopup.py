# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

APPLYTOPUP_METADATA = Metadata(
    id="9351040d516e40d391172d1c29d310306c2e148d",
    name="applytopup",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class ApplytopupOutputs(typing.NamedTuple):
    """
    Output object returned when calling `applytopup(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """The output warped image."""


def applytopup(
    imain: list[str],
    datain: InputPathType,
    inindex: list[str],
    topup: InputPathType,
    out: str,
    method: typing.Literal["jac", "lsr"] | None = None,
    interp: typing.Literal["trilinear", "spline"] | None = None,
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    verbose: bool = False,
    runner: Runner = None,
) -> ApplytopupOutputs:
    """
    applytopup by University of Oxford (Jesper Andersson).
    
    applytopup applies corrections to images using the field estimates produced
    by topup.
    
    Args:
        imain: Comma separated list of names of input image (to be corrected).
        datain: Name of text file with PE directions/times.
        inindex: Comma separated list of indices into --datain of the input\
            image (to be corrected).
        topup: Name of field/movements (from topup).
        out: Basename for output (warped) image.
        method: Use jacobian modulation (jac) or least-squares resampling\
            (lsr), default=lsr.
        interp: Interpolation method {trilinear, spline}, default=spline.
        datatype: Force output data type [char short int float double].
        verbose: Switch on diagnostic messages.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ApplytopupOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(APPLYTOPUP_METADATA)
    cargs = []
    cargs.append("applytopup")
    cargs.extend(["-i", *imain])
    cargs.extend(["-a", execution.input_file(datain)])
    cargs.extend(["-x", *inindex])
    cargs.extend(["-t", execution.input_file(topup)])
    cargs.extend(["-o", out])
    if method is not None:
        cargs.extend(["-m", method])
    if interp is not None:
        cargs.extend(["-n", interp])
    if datatype is not None:
        cargs.extend(["-d", datatype])
    if verbose:
        cargs.append("-v")
    ret = ApplytopupOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"{out}_abswarp.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "APPLYTOPUP_METADATA",
    "ApplytopupOutputs",
    "applytopup",
]
