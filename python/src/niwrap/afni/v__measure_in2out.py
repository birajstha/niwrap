# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__MEASURE_IN2OUT_METADATA = Metadata(
    id="4a0fafb32ed5b72823a2f2c3620ce2533eb5d2af.boutiques",
    name="@measure_in2out",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VMeasureIn2outOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__measure_in2out(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    inout_dist: OutputPathType
    """Volumetric thickness/distance from in to out"""
    in_and_out: OutputPathType
    """Volumetric distance to inside and outside in 2 volumes"""
    inout_thick: OutputPathType
    """Unsmoothed thickness mapped to surface nodes"""
    inout_thick_smooth: OutputPathType
    """Smoothed thickness mapped to surface nodes"""
    maskset_output: OutputPathType
    """Mask file"""
    maskset_rs: OutputPathType
    """Resampled mask file"""
    anat_gii: OutputPathType
    """Surface representation of mask volume"""
    quick_spec: OutputPathType
    """Simple specification file for surface to use with suma commands"""


def v__measure_in2out(
    maskset: InputPathType,
    surfset: InputPathType,
    outdir: str,
    resample: str | None = None,
    increment: float | None = None,
    surfsmooth: float | None = None,
    maxthick: float | None = None,
    depthsearch: float | None = None,
    maskinoutvals: list[float] | None = None,
    keep_temp_files: bool = False,
    surfsmooth_method: str | None = None,
    fs_cort_dir: str | None = None,
    runner: Runner | None = None,
) -> VMeasureIn2outOutputs:
    """
    Compute thickness of mask using in2out method.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        maskset: Mask dataset for input.
        surfset: Surface dataset onto which to map thickness (probably a\
            pial/gray matter surface).
        outdir: Output directory. If not specified, in2out_thickdir is used.
        resample: Resample input to mm in millimeters (put a number here). Set\
            this to half a voxel or "auto". No resampling is done by default.\
            Resampling is highly recommended for most 1mm data.
        increment: Test thickness at increments of sub-voxel distance. Default\
            is 1/4 voxel minimum distance (in-plane).
        surfsmooth: Smooth surface map of thickness by mm millimeters. Default\
            is 6 mm.
        maxthick: Search for maximum thickness value of mm millimeters. Default\
            is 6 mm.
        depthsearch: Map to surface by looking for max along mm millimeter\
            normal vectors. Default is 3 mm.
        maskinoutvals: Use v1 for value of mask, v2 and v3 for inside and\
            outside mask values (e.g., '1 -2 -1').
        keep_temp_files: Do not delete the intermediate files (for testing).
        surfsmooth_method: Heat method used for smoothing surfaces. Default is\
            HEAT_07 but HEAT_05 is also useful for some models.
        fs_cort_dir: Use FreeSurfer SUMA directory from @SUMA_Make_Spec_FS for\
            processing.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMeasureIn2outOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MEASURE_IN2OUT_METADATA)
    cargs = []
    cargs.append("@measure_in2out")
    cargs.append("-maskset")
    cargs.append(execution.input_file(maskset))
    cargs.append("-surfset")
    cargs.append(execution.input_file(surfset))
    cargs.append("-outdir")
    cargs.append(outdir)
    if resample is not None:
        cargs.extend([
            "-resample",
            resample
        ])
    if increment is not None:
        cargs.extend([
            "-increment",
            str(increment)
        ])
    if surfsmooth is not None:
        cargs.extend([
            "-surfsmooth",
            str(surfsmooth)
        ])
    if maxthick is not None:
        cargs.extend([
            "-maxthick",
            str(maxthick)
        ])
    if depthsearch is not None:
        cargs.extend([
            "-depthsearch",
            str(depthsearch)
        ])
    if maskinoutvals is not None:
        cargs.extend([
            "-maskinoutvals",
            *map(str, maskinoutvals)
        ])
    if keep_temp_files:
        cargs.append("-keep_temp_files")
    if surfsmooth_method is not None:
        cargs.extend([
            "-surfsmooth_method",
            surfsmooth_method
        ])
    if fs_cort_dir is not None:
        cargs.extend([
            "-fs_cort_dir",
            fs_cort_dir
        ])
    ret = VMeasureIn2outOutputs(
        root=execution.output_file("."),
        inout_dist=execution.output_file("inout_dist.nii.gz"),
        in_and_out=execution.output_file("in_and_out.nii.gz"),
        inout_thick=execution.output_file("inout_thick.niml.dset"),
        inout_thick_smooth=execution.output_file("inout_thick_smooth.niml.dset"),
        maskset_output=execution.output_file("maskset.nii.gz"),
        maskset_rs=execution.output_file("maskset_rs.nii.gz"),
        anat_gii=execution.output_file("anat.gii"),
        quick_spec=execution.output_file("quick.spec"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VMeasureIn2outOutputs",
    "V__MEASURE_IN2OUT_METADATA",
    "v__measure_in2out",
]
