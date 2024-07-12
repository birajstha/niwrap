# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ASL_FILE_METADATA = Metadata(
    id="c11d9e14e30189e2b62f082af560bb0efca692b3",
    name="asl_file",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class AslFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `asl_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_data: OutputPathType
    """Primary output data file"""
    output_mean: OutputPathType
    """Mean output data file"""


def asl_file(
    datafile: InputPathType,
    ntis: float | int,
    outfile: str,
    mask: InputPathType | None = None,
    inblockform: typing.Literal["rpt", "tis"] | None = None,
    inaslform: typing.Literal["diff", "tc", "ct", "tcb", "ctb"] | None = "diff",
    rpts: str | None = None,
    pairs: bool = False,
    spairs: bool = False,
    diff: bool = False,
    surrdiff: bool = False,
    extrapolate: bool = False,
    neighbour: float | int | None = None,
    pvgm: InputPathType | None = None,
    pvwm: InputPathType | None = None,
    kernel: float | int | None = None,
    outblockform: typing.Literal["rpt", "tis"] | None = None,
    mean: bool = False,
    split: str | None = None,
    epoch: bool = False,
    epoch_length: float | int | None = None,
    epoch_overlap: float | int | None = None,
    epoch_unit: typing.Literal["rpt", "tis"] | None = None,
    deconv: bool = False,
    aif: InputPathType | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AslFileOutputs:
    """
    asl_file by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    ASL data manipulation tool for FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/AslFile
    
    Args:
        datafile: ASL data file.
        ntis: Number of TIs in the file.
        outfile: Output data file.
        mask: Mask file.
        inblockform: Input block format.
        inaslform: ASL data form.
        rpts: Number of repeats at each TI as comma separated list, not\
            required if the number of repeats is same for all TIs (only for use\
            with --ibf=tis).
        pairs: Data contains adjacent pairs of measurements (e.g. Tag, Control)\
            DEPRECATED use --iaf instead.
        spairs: Split the pairs within the data, e.g. to separate tag and\
            control images in output.
        diff: Take the difference between the pairs, i.e., Tag-control\
            difference.
        surrdiff: Do surround subtraction on the pairs.
        extrapolate: Option to extrapolate the edge of the brain to fix the\
            artefact on the edge of the brain.
        neighbour: Neighbour size for extrapolation, must be an odd number\
            between 3 and 9. Default: 5.
        pvgm: GM partial volume map.
        pvwm: WM partial volume map.
        kernel: Kernel size (in voxels) of partial volume correction, must be\
            an odd number between 3 and 9. Default: 5.
        outblockform: Output block format.
        mean: Output ASL data having taken mean at each TI to file.
        split: Split data into separate files for each TI, specify filename\
            root.
        epoch: Output epochs of ASL data (takes mean at each TI within the\
            epoch).
        epoch_length: Length of epochs in number of repeats.
        epoch_overlap: Amount of overlap between epochs in number of repeats.
        epoch_unit: Epochs to be determined over.
        deconv: Deconvolution of data with arterial input functions.
        aif: Arterial input functions for deconvolution (4D volume, one aif for\
            each voxel within mask).
        help_: Display the help message.
        version: Display version identification.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `AslFileOutputs`).
    """
    runner = runner or get_global_runner()
    if neighbour is not None and not (3 <= neighbour <= 9): 
        raise ValueError(f"'neighbour' must be between 3 <= x <= 9 but was {neighbour}")
    if kernel is not None and not (3 <= kernel <= 9): 
        raise ValueError(f"'kernel' must be between 3 <= x <= 9 but was {kernel}")
    execution = runner.start_execution(ASL_FILE_METADATA)
    cargs = []
    cargs.append("asl_file")
    cargs.extend(["--data", execution.input_file(datafile)])
    cargs.extend(["--ntis", str(ntis)])
    if mask is not None:
        cargs.extend(["--mask", execution.input_file(mask)])
    if inblockform is not None:
        cargs.extend(["--ibf", inblockform])
    if inaslform is not None:
        cargs.extend(["--iaf", inaslform])
    if rpts is not None:
        cargs.extend(["--rpts", rpts])
    if pairs:
        cargs.append("--pairs")
    if spairs:
        cargs.append("--spairs")
    if diff:
        cargs.append("--diff")
    if surrdiff:
        cargs.append("--surrdiff")
    if extrapolate:
        cargs.append("--extrapolate")
    if neighbour is not None:
        cargs.extend(["--neighbour", str(neighbour)])
    if pvgm is not None:
        cargs.extend(["--pvgm", execution.input_file(pvgm)])
    if pvwm is not None:
        cargs.extend(["--pvwm", execution.input_file(pvwm)])
    if kernel is not None:
        cargs.extend(["--kernel", str(kernel)])
    cargs.extend(["--out", outfile])
    if outblockform is not None:
        cargs.extend(["--obf", outblockform])
    if mean:
        cargs.append("--mean")
    if split is not None:
        cargs.extend(["--split", split])
    if epoch:
        cargs.append("--epoch")
    if epoch_length is not None:
        cargs.extend(["--elen", str(epoch_length)])
    if epoch_overlap is not None:
        cargs.extend(["--eol", str(epoch_overlap)])
    if epoch_unit is not None:
        cargs.extend(["--eunit", epoch_unit])
    if deconv:
        cargs.append("--deconv")
    if aif is not None:
        cargs.extend(["--aif", execution.input_file(aif)])
    ret = AslFileOutputs(
        root=execution.output_file("."),
        output_data=execution.output_file(f"{outfile}.nii.gz"),
        output_mean=execution.output_file(f"{outfile}_mean.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ASL_FILE_METADATA",
    "AslFileOutputs",
    "asl_file",
]
