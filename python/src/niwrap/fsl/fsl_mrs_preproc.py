# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FSL_MRS_PREPROC_METADATA = Metadata(
    id="7a79f97775572bbd9f9a0a068010017a5746f2a9",
    name="fsl_mrs_preproc",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class FslMrsPreprocOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_mrs_preproc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_folder: OutputPathType
    """Output folder containing preprocessed data"""


def fsl_mrs_preproc(
    data: InputPathType,
    reference: InputPathType,
    output: str,
    quant: InputPathType | None = None,
    ecc: InputPathType | None = None,
    noaverage: bool = False,
    hlsvd: bool = False,
    leftshift: float | int | None = None,
    t1: InputPathType | None = None,
    verbose: bool = False,
    conjugate: bool = False,
    overwrite: bool = False,
    report: bool = False,
    config: InputPathType | None = None,
    runner: Runner = None,
) -> FslMrsPreprocOutputs:
    """
    fsl_mrs_preproc by FMRIB Analysis Group, Oxford University.
    
    FSL Magnetic Resonance Spectroscopy - Complete non-edited SVS Preprocessing.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FSL
    
    Args:
        data: Input file(s)
        reference: Reference non-water suppressed file
        output: Output folder
        quant: Water reference data for quantification (Optional)
        ecc: Water reference data for eddy current correction (Optional)
        noaverage: Do not average repetitions
        hlsvd: Apply HLSVD for residual water removal
        leftshift: Remove points at the start of the fid
        t1: Structural image (for report)
        verbose: Spit out verbose info
        conjugate: Apply conjugate to FID
        overwrite: Overwrite existing output folder
        report: Generate report in output folder
        config: Configuration file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FslMrsPreprocOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_MRS_PREPROC_METADATA)
    cargs = []
    cargs.append("fsl_mrs_preproc")
    cargs.append(execution.input_file(data))
    cargs.append(execution.input_file(reference))
    cargs.append(output)
    if quant is not None:
        cargs.append(execution.input_file(quant))
    if ecc is not None:
        cargs.append(execution.input_file(ecc))
    if noaverage:
        cargs.append("--noaverage")
    if hlsvd:
        cargs.append("--hlsvd")
    if leftshift is not None:
        cargs.extend(["--leftshift", str(leftshift)])
    if t1 is not None:
        cargs.append(execution.input_file(t1))
    if verbose:
        cargs.append("--verbose")
    if conjugate:
        cargs.append("--conjugate")
    if overwrite:
        cargs.append("--overwrite")
    if report:
        cargs.append("--report")
    if config is not None:
        cargs.append(execution.input_file(config))
    ret = FslMrsPreprocOutputs(
        root=execution.output_file("."),
        output_folder=execution.output_file(f"{output}", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_MRS_PREPROC_METADATA",
    "FslMrsPreprocOutputs",
    "fsl_mrs_preproc",
]
