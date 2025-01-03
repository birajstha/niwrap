# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_PROC_DECMAP_METADATA = Metadata(
    id="a736dc72fa9ccb8800e84305855b09096c833b1d.boutiques",
    name="fat_proc_decmap",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatProcDecmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_proc_decmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile_dec_rgb: OutputPathType
    """Single file of type 'rgb' for RGB coloration display."""
    outfile_dec_unwt_thr: OutputPathType
    """Single file of type 'rgb' without FA weighting but using FA to threshold
    where DEC values are calculated."""
    outfile_dec_sca: OutputPathType
    """DEC file additionally scaled by a value (such as 0.7)."""
    qc_dec_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC data."""
    qc_dec_unwt_thrx_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC
    unweighted thresholded data."""
    qc_dec_sca_images: OutputPathType
    """Set of cor, axi, and sag images (each a 5x3 montage) of the DEC scaled
    data."""


def fat_proc_decmap(
    in_fa: InputPathType,
    in_v1: InputPathType,
    prefix: str,
    mask: InputPathType | None = None,
    fa_thr: float | None = None,
    fa_sca: float | None = None,
    workdir: str | None = None,
    no_clean: bool = False,
    qc_prefix: str | None = None,
    no_cmd_out: bool = False,
    no_qc_view: bool = False,
    runner: Runner | None = None,
) -> FatProcDecmapOutputs:
    """
    This program makes a directionally encoded color (DEC) map for DTI results.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        in_fa: Input FA (scalar) map.
        in_v1: Input first eigenvector (3-vector) map.
        prefix: Set prefix (and path) for output DWI data.
        mask: Optional mask for picking out a region. Otherwise, only places\
            with FA>0 are given coloration.
        fa_thr: For QC1 type of DEC images, use FFF to threshold where DEC\
            values are calculated (default: 0.2).
        fa_sca: For QC2 type of DEC images, use SSS to scale the FA weighting\
            of what would otherwise be a 'classical' DEC map (default: 0.7).
        workdir: Specify a working directory, which can be removed (default:\
            '__WORKING_decmap').
        no_clean: Do not delete temporary files when finishing.
        qc_prefix: Set the prefix of the QC image files (default: 'PREFIX').
        no_cmd_out: Do not save the command line call of this program and\
            location where it was run.
        no_qc_view: Turn off generating QC image files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatProcDecmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_PROC_DECMAP_METADATA)
    cargs = []
    cargs.append("fat_proc_decmap")
    cargs.extend([
        "-in_fa",
        execution.input_file(in_fa)
    ])
    cargs.extend([
        "-in_v1",
        execution.input_file(in_v1)
    ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if fa_thr is not None:
        cargs.extend([
            "-fa_thr",
            str(fa_thr)
        ])
    if fa_sca is not None:
        cargs.extend([
            "-fa_sca",
            str(fa_sca)
        ])
    if workdir is not None:
        cargs.extend([
            "-workdir",
            workdir
        ])
    if no_clean:
        cargs.append("-no_clean")
    if qc_prefix is not None:
        cargs.extend([
            "-qc_prefix",
            qc_prefix
        ])
    if no_cmd_out:
        cargs.append("-no_cmd_out")
    if no_qc_view:
        cargs.append("-no_qc_view")
    ret = FatProcDecmapOutputs(
        root=execution.output_file("."),
        outfile_dec_rgb=execution.output_file(prefix + "_dec.nii.gz"),
        outfile_dec_unwt_thr=execution.output_file(prefix + "_dec_unwt_thr.nii.gz"),
        outfile_dec_sca=execution.output_file(prefix + "_dec_sca*.nii.gz"),
        qc_dec_images=execution.output_file(prefix + "_qc_dec*.png"),
        qc_dec_unwt_thrx_images=execution.output_file(prefix + "_qc_dec_unwt_thrx*.png"),
        qc_dec_sca_images=execution.output_file(prefix + "_qc_dec_sca*.png"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_PROC_DECMAP_METADATA",
    "FatProcDecmapOutputs",
    "fat_proc_decmap",
]
