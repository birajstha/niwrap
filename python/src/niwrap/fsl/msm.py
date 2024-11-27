# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MSM_METADATA = Metadata(
    id="bfab58a91ee8e696e19e1066e4388d1ee9bd9338.boutiques",
    name="msm",
    package="fsl",
    container_image_tag="brainlife/fsl:6.0.4-patched2",
)


class MsmOutputs(typing.NamedTuple):
    """
    Output object returned when calling `msm(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Output file from MSM"""


def msm(
    inmesh: InputPathType,
    out: str,
    refmesh: InputPathType | None = None,
    indata: InputPathType | None = None,
    refdata: InputPathType | None = None,
    trans: InputPathType | None = None,
    in_register: InputPathType | None = None,
    inweight: InputPathType | None = None,
    refweight: InputPathType | None = None,
    format_: str | None = None,
    conf: InputPathType | None = None,
    levels: float | None = None,
    smoothout: float | None = None,
    help_: bool = False,
    verbose: bool = False,
    printoptions: bool = False,
    runner: Runner | None = None,
) -> MsmOutputs:
    """
    MSM (Multimodal Surface Matching) is a tool for aligning brain surface scans
    based on their cortical folding patterns or functional/structural data.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        inmesh: Input mesh (available formats: VTK, ASCII, GIFTI). Needs to be\
            a sphere.
        out: Output basename.
        refmesh: Reference mesh (available formats: VTK, ASCII, GIFTI). Needs\
            to be a sphere. If not included algorithm assumes reference mesh is\
            equivalent input.
        indata: Scalar or multivariate data for input - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        refdata: Scalar or multivariate data for reference - can be ASCII\
            (.asc,.dpv,.txt) or GIFTI (.func.gii or .shape.gii).
        trans: Transformed source mesh (output of a previous registration). Use\
            this to initialise the current registration.
        in_register: Input mesh at data resolution. Used to resample data onto\
            input mesh if data is supplied at a different resolution. Note this\
            mesh HAS to be in alignment with either the input_mesh of (if supplied)\
            the transformed source mesh. Use with supreme caution.
        inweight: Cost function weighting for input - weights data in these\
            vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        refweight: Cost function weighting for reference - weights data in\
            these vertices when calculating similarity (ASCII or GIFTI). Can be\
            multivariate provided dimension equals that of data.
        format_: Format of output files, can be: GIFTI, VTK, ASCII or ASCII_MAT\
            (for full details of output file formats see MSM wiki).
        conf: Configuration file.
        levels: Number of resolution levels (default = number of resolution\
            levels specified by --opt in config file).
        smoothout: Smooth transformed output with this sigma (default=0).
        help_: Display help message.
        verbose: Switch on diagnostic messages.
        printoptions: Print configuration file options.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MsmOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MSM_METADATA)
    cargs = []
    cargs.append("msm")
    cargs.append(execution.input_file(inmesh))
    cargs.extend([
        "-out",
        "-" + out
    ])
    if refmesh is not None:
        cargs.extend([
            "--refmesh",
            execution.input_file(refmesh)
        ])
    if indata is not None:
        cargs.extend([
            "--indata",
            execution.input_file(indata)
        ])
    if refdata is not None:
        cargs.extend([
            "--refdata",
            execution.input_file(refdata)
        ])
    if trans is not None:
        cargs.extend([
            "--trans",
            execution.input_file(trans)
        ])
    if in_register is not None:
        cargs.extend([
            "--in_register",
            execution.input_file(in_register)
        ])
    if inweight is not None:
        cargs.extend([
            "--inweight",
            execution.input_file(inweight)
        ])
    if refweight is not None:
        cargs.extend([
            "--refweight",
            execution.input_file(refweight)
        ])
    if format_ is not None:
        cargs.extend([
            "-f",
            format_
        ])
    if conf is not None:
        cargs.extend([
            "--conf",
            execution.input_file(conf)
        ])
    if levels is not None:
        cargs.extend([
            "--levels",
            str(levels)
        ])
    if smoothout is not None:
        cargs.extend([
            "--smoothout",
            str(smoothout)
        ])
    if help_:
        cargs.append("-h")
    if verbose:
        cargs.append("-v")
    if printoptions:
        cargs.append("-p")
    ret = MsmOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file("[OUTPUT_BASENAME]_output.ext"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MSM_METADATA",
    "MsmOutputs",
    "msm",
]
