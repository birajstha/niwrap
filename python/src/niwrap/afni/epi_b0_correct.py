# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

EPI_B0_CORRECT_METADATA = Metadata(
    id="690e7b1a6986e67ced0f065ca6d025cd2006e8eb.boutiques",
    name="epi_b0_correct",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class EpiB0CorrectOutputs(typing.NamedTuple):
    """
    Output object returned when calling `epi_b0_correct(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    warp_dset: OutputPathType
    """Warp dataset containing the warp along the phase encode axis."""
    cmds_script: OutputPathType
    """Script of the commands used to generate the warp and process the EPI."""
    params_txt: OutputPathType
    """Text file of parameters input or derived from datasets."""
    unwarped_epi: OutputPathType
    """EPI dataset with estimated distortion correction applied."""
    qc_image_dir: OutputPathType
    """Directory containing QC images."""


def epi_b0_correct(
    prefix: str,
    input_freq: InputPathType,
    input_epi: InputPathType,
    epi_pe_dir: str,
    input_mask: InputPathType | None = None,
    input_magn: InputPathType | None = None,
    input_anat: InputPathType | None = None,
    input_json: InputPathType | None = None,
    epi_pe_bwpp: float | None = None,
    epi_pe_echo_sp: float | None = None,
    epi_pe_vox_dim: float | None = None,
    scale_freq: float | None = None,
    out_cmds: str | None = None,
    out_pars: str | None = None,
    wdir_name: str | None = None,
    blur_sigma: float | None = None,
    do_recenter_freq: str | None = None,
    mask_dilate: list[float] | None = None,
    no_clean: bool = False,
    qc_box_focus_ulay: bool = False,
    no_qc_image: bool = False,
    help_: bool = False,
    ver: bool = False,
    date: bool = False,
    runner: Runner | None = None,
) -> EpiB0CorrectOutputs:
    """
    B0 distortion correction tool using an acquired frequency (phase) image.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Prefix of output files; can include path.
        input_freq: Phase dataset (frequency volume); should be at similar\
            resolution and FOV as the EPI dataset; must be scaled appropriately.
        input_epi: EPI dataset to which B0 distortion correction will be\
            applied.
        epi_pe_dir: Direction (axis) of phase encoding, e.g., AP, PA, RL, ...
        input_mask: Mask of brain volume.
        input_magn: Magnitude dataset from which to estimate brain mask; can be\
            used for QC imaging.
        input_anat: Anatomical dataset to be used as underlay for QC images\
            (optional).
        input_json: JSON file containing parameters about the EPI dataset.
        epi_pe_bwpp: Bandwidth per pixel (in Hz) in the EPI dataset along the\
            phase encode direction.
        epi_pe_echo_sp: Effective TE spacing of the phase encoded volume, in\
            seconds.
        epi_pe_vox_dim: Voxel size along the EPI dataset's phase encode axis,\
            in mm.
        scale_freq: Scale to apply to frequency volume to match units (def:\
            SF=1.0).
        out_cmds: Name for output script recording commands (def:\
            PREFIX_cmds.tcsh).
        out_pars: Name for output text file recording relevant parameters (def:\
            PREFIX_pars.txt).
        wdir_name: Working directory name (def: automatic name).
        blur_sigma: Amount of blurring to apply to masked phase encode dataset\
            (def: BS=9).
        do_recenter_freq: Method to recenter the phase volume within the brain\
            mask (def: MC=mode).
        mask_dilate: Erosion and dilation parameters for automask (when using\
            magnitude image).
        no_clean: Don't remove the temporary directory of intermediate files.
        qc_box_focus_ulay: Focus the QC images on an automask region of the\
            underlay dataset.
        no_qc_image: Don't generate QC images.
        help_: Display program help in terminal.
        ver: Display program version number in terminal.
        date: Display date of program's last update in terminal.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `EpiB0CorrectOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(EPI_B0_CORRECT_METADATA)
    cargs = []
    cargs.append("epi_b0_correct.py")
    cargs.append(prefix)
    cargs.extend([
        "-in_freq",
        execution.input_file(input_freq)
    ])
    cargs.extend([
        "-in_epi",
        execution.input_file(input_epi)
    ])
    if input_mask is not None:
        cargs.extend([
            "-in_mask",
            execution.input_file(input_mask)
        ])
    if input_magn is not None:
        cargs.extend([
            "-in_magn",
            execution.input_file(input_magn)
        ])
    if input_anat is not None:
        cargs.extend([
            "-in_anat",
            execution.input_file(input_anat)
        ])
    if input_json is not None:
        cargs.extend([
            "-in_epi_json",
            execution.input_file(input_json)
        ])
    cargs.extend([
        "-epi_pe_dir",
        epi_pe_dir
    ])
    if epi_pe_bwpp is not None:
        cargs.extend([
            "-epi_pe_bwpp",
            str(epi_pe_bwpp)
        ])
    if epi_pe_echo_sp is not None:
        cargs.extend([
            "-epi_pe_echo_sp",
            str(epi_pe_echo_sp)
        ])
    if epi_pe_vox_dim is not None:
        cargs.extend([
            "-epi_pe_voxdim",
            str(epi_pe_vox_dim)
        ])
    if scale_freq is not None:
        cargs.extend([
            "-scale_freq",
            str(scale_freq)
        ])
    if out_cmds is not None:
        cargs.extend([
            "-out_cmds",
            out_cmds
        ])
    if out_pars is not None:
        cargs.extend([
            "-out_pars",
            out_pars
        ])
    if wdir_name is not None:
        cargs.extend([
            "-wdir_name",
            wdir_name
        ])
    if blur_sigma is not None:
        cargs.extend([
            "-blur_sigma",
            str(blur_sigma)
        ])
    if do_recenter_freq is not None:
        cargs.extend([
            "-do_recenter_freq",
            do_recenter_freq
        ])
    if mask_dilate is not None:
        cargs.extend([
            "-mask_dilate",
            *map(str, mask_dilate)
        ])
    if no_clean:
        cargs.append("-no_clean")
    if qc_box_focus_ulay:
        cargs.append("-qc_box_focus_ulay")
    if no_qc_image:
        cargs.append("-no_qc_image")
    if help_:
        cargs.append("-help")
    if ver:
        cargs.append("-ver")
    if date:
        cargs.append("-date")
    ret = EpiB0CorrectOutputs(
        root=execution.output_file("."),
        warp_dset=execution.output_file(prefix + "_WARP.nii.gz"),
        cmds_script=execution.output_file(prefix + "_cmds.tcsh"),
        params_txt=execution.output_file(prefix + "_pars.txt"),
        unwarped_epi=execution.output_file(prefix + "_unwarped.nii.gz"),
        qc_image_dir=execution.output_file(prefix + "_QC/"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "EPI_B0_CORRECT_METADATA",
    "EpiB0CorrectOutputs",
    "epi_b0_correct",
]
