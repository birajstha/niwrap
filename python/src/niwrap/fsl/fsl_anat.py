# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_ANAT_METADATA = Metadata(
    id="0da53b490ed48b917206d952e52a45d300617d44.boutiques",
    name="fsl_anat",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_anat_dir: OutputPathType | None
    """Output anatomical directory"""


def fsl_anat(
    structural_image: InputPathType | None = None,
    existing_anat_dir: str | None = None,
    output_dir: str | None = None,
    clobber_flag: bool = False,
    strongbias_flag: bool = False,
    weakbias_flag: bool = False,
    noreorient_flag: bool = False,
    nocrop_flag: bool = False,
    nobias_flag: bool = False,
    noreg_flag: bool = False,
    nononlinreg_flag: bool = False,
    noseg_flag: bool = False,
    nosubcortseg_flag: bool = False,
    bias_smoothing: float | None = None,
    image_type: str | None = None,
    nosearch_flag: bool = False,
    bet_f_param: float | None = None,
    nocleanup_flag: bool = False,
    runner: Runner | None = None,
) -> FslAnatOutputs:
    """
    A wrapper for FSL tools to process anatomical scans.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        structural_image: Filename of input image (for one image only).
        existing_anat_dir: Directory name for existing .anat directory where\
            this script will be run in place.
        output_dir: Basename of directory for output (default is input image\
            basename followed by .anat).
        clobber_flag: If .anat directory exists (as specified by -o or default\
            from -i) then delete it and make a new one.
        strongbias_flag: Used for images with very strong bias fields.
        weakbias_flag: Used for images with smoother, more typical, bias fields\
            (default setting).
        noreorient_flag: Turn off step that does reorientation to standard\
            (fslreorient2std).
        nocrop_flag: Turn off step that does automated cropping (robustfov).
        nobias_flag: Turn off steps that do bias field correction (via FAST).
        noreg_flag: Turn off steps that do registration to standard (FLIRT and\
            FNIRT).
        nononlinreg_flag: Turn off step that does non-linear registration\
            (FNIRT).
        noseg_flag: Turn off step that does tissue-type segmentation (FAST).
        nosubcortseg_flag: Turn off step that does sub-cortical segmentation\
            (FIRST).
        bias_smoothing: Specify the value for bias field smoothing (the -l\
            option in FAST).
        image_type: Specify the type of image (choose one of T1 T2 PD - default\
            is T1).
        nosearch_flag: Specify that linear registration uses the -nosearch\
            option (FLIRT).
        bet_f_param: Specify f parameter for BET (only used if not running\
            non-linear reg and also wanting brain extraction done).
        nocleanup_flag: Do not remove intermediate files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_ANAT_METADATA)
    cargs = []
    cargs.append("fsl_anat")
    if structural_image is not None:
        cargs.extend([
            "-i",
            execution.input_file(structural_image)
        ])
    if existing_anat_dir is not None:
        cargs.extend([
            "-d",
            existing_anat_dir
        ])
    if output_dir is not None:
        cargs.extend([
            "-o",
            output_dir
        ])
    if clobber_flag:
        cargs.append("--clobber")
    if strongbias_flag:
        cargs.append("--strongbias")
    if weakbias_flag:
        cargs.append("--weakbias")
    if noreorient_flag:
        cargs.append("--noreorient")
    if nocrop_flag:
        cargs.append("--nocrop")
    if nobias_flag:
        cargs.append("--nobias")
    if noreg_flag:
        cargs.append("--noreg")
    if nononlinreg_flag:
        cargs.append("--nononlinreg")
    if noseg_flag:
        cargs.append("--noseg")
    if nosubcortseg_flag:
        cargs.append("--nosubcortseg")
    if bias_smoothing is not None:
        cargs.extend([
            "-s",
            str(bias_smoothing)
        ])
    if image_type is not None:
        cargs.extend([
            "-t",
            image_type
        ])
    if nosearch_flag:
        cargs.append("--nosearch")
    if bet_f_param is not None:
        cargs.extend([
            "--betfparam",
            str(bet_f_param)
        ])
    if nocleanup_flag:
        cargs.append("--nocleanup")
    ret = FslAnatOutputs(
        root=execution.output_file("."),
        output_anat_dir=execution.output_file(output_dir + ".anat") if (output_dir is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_ANAT_METADATA",
    "FslAnatOutputs",
    "fsl_anat",
]
