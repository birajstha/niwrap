# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FAT_PROC_CONVERT_DCM_ANAT_METADATA = Metadata(
    id="7951b73888f19470fef8855e904dbbbc4d0d9690",
    name="fat_proc_convert_dcm_anat",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FatProcConvertDcmAnatOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_convert_dcm_anat(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_volume: OutputPathType
    """Converted anatomical volume output."""


def fat_proc_convert_dcm_anat(
    prefix: str,
    dicom_directory: str | None = None,
    nifti_input: InputPathType | None = None,
    workdir: str | None = None,
    orient: str | None = None,
    no_clean: bool = False,
    reorig_reorient_off: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    runner: Runner | None = None,
) -> FatProcConvertDcmAnatOutputs:
    """
    fat_proc_convert_dcm_anat by AFNI Team.
    
    Converts an anatomical dataset from DICOM files into a volume, specifically
    designed to fit in line with other processing such as DTI analysis.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/fat_proc_convert_dcm_anat.html
    
    Args:
        prefix: Set prefix (and path) for output data.
        dicom_directory: Input as DICOM directory; DIR_IN should contain only\
            DICOM files; all will be selected.
        nifti_input: Input as NIFTI file (zipped or unzipped fine). Alternative\
            to '-indir ..'.
        workdir: Specify a working directory, which can be removed (default\
            name = '__WORKING_convert_dcm_anat').
        orient: Optional chance to reset orientation of the volume files\
            (default is currently 'RAI').
        no_clean: Prevents removal of working directory.
        reorig_reorient_off: Turns off the nicety of putting (0, 0, 0) at\
            brain's center of mass (-> 'reorigin' calc) and reorienting data (->\
            'reorient' calc).
        qc_prefix: Set the prefix of the QC image files separately (default is\
            '').
        no_cmd_out: Don't save the command line call and the location where it\
            was run.
        no_qc_view: Turn off generating QC image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcConvertDcmAnatOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_CONVERT_DCM_ANAT_METADATA)
    cargs = []
    cargs.append("fat_proc_convert_dcm_anat")
    if nifti_input is not None:
        cargs.extend(["-innii", execution.input_file(nifti_input)])
    cargs.append("-prefix")
    cargs.extend(["-prefix", prefix])
    if workdir is not None:
        cargs.extend(["-workdir", workdir])
    if orient is not None:
        cargs.extend(["-orient", orient])
    if no_clean:
        cargs.append("-no_clean")
    if reorig_reorient_off:
        cargs.append("-reorig_reorient_off")
    if qc_prefix is not None:
        cargs.extend(["-qc_prefix", qc_prefix])
    if no_cmd_out:
        cargs.append("-no_cmd_out")
    if no_qc_view:
        cargs.append("-no_qc_view")
    ret = FatProcConvertDcmAnatOutputs(
        root=execution.output_file("."),
        output_volume=execution.output_file(f"{prefix}.nii.gz"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_CONVERT_DCM_ANAT_METADATA",
    "FatProcConvertDcmAnatOutputs",
    "fat_proc_convert_dcm_anat",
]
