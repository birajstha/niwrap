# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

XTRACT_BLUEPRINT_METADATA = Metadata(
    id="d46ca4a0b7fd5fecfd318331eb681722aa0ef1d3",
    name="xtract_blueprint",
)


class XtractBlueprintOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xtract_blueprint(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated in the specified output folder"""


def xtract_blueprint(
    bpx_folder: str,
    out_folder: str,
    xtract_folder: str,
    seeds_list: str,
    warps: str,
    stage: str | None = None,
    gpu_flag: bool = False,
    save_txt_flag: bool = False,
    prefix: str | None = None,
    rois_list: str | None = None,
    stops_file: InputPathType | None = None,
    wtstops_file: InputPathType | None = None,
    tract_list: str | None = None,
    threshold: float | int | None = 0.001,
    nsamples: float | int | None = 1000,
    res: float | int | None = 3,
    ptx_options: InputPathType | None = None,
    runner: Runner = None,
) -> XtractBlueprintOutputs:
    """
    xtract_blueprint by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Blueprint extraction tool using XTRACT and bedpostx folders.
    
    More information: https://fsl.fmrib.ox.ac.uk
    
    Args:
        bpx_folder: Path to bedpostx folder.
        out_folder: Path to output folder.
        xtract_folder: Path to xtract folder.
        seeds_list: Comma separated list of seeds for which a blueprint is\
            requested.
        warps: Standard space reference image and transforms between xtract\
            space and diffusion space.
        stage: What to run. 1:matrix2, 2:blueprint, all:everything (default).
        gpu_flag: Use GPU version.
        save_txt_flag: Save blueprint as txt file (nseed by ntracts) instead of\
            CIFTI.
        prefix: Specify a prefix for the final blueprint filename.
        rois_list: Comma separated list of ROIs (gifti) to restrict seeding\
            (e.g. medial wall masks).
        stops_file: Text file containing line separated list.
        wtstops_file: Text file containing line separated list.
        tract_list: Comma separated list of tracts to include (default = all\
            found under -xtract <folder>).
        threshold: Threshold applied to XTRACT tracts prior to blueprint\
            calculation (default = 0.001, i.e. 0.1% probability).
        nsamples: Number of samples per seed used in tractography (default =\
            1000).
        res: Resolution of matrix2 output (Default = 3 mm).
        ptx_options: Pass extra probtrackx2 options as a text file to override\
            defaults.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XtractBlueprintOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XTRACT_BLUEPRINT_METADATA)
    cargs = []
    cargs.append("xtract_blueprint")
    cargs.append("-bpx")
    cargs.append(bpx_folder)
    cargs.append("-out")
    cargs.append(out_folder)
    cargs.append("-xtract")
    cargs.append(xtract_folder)
    cargs.append("-seeds")
    cargs.append(seeds_list)
    cargs.append("-warps")
    cargs.append("[REF]")
    cargs.append("[XTRACT2DIFF]")
    cargs.append("[DIFF2XTRACT]")
    if stage is not None:
        cargs.extend(["-stage", stage])
    if gpu_flag:
        cargs.append("-gpu")
    if save_txt_flag:
        cargs.append("-savetxt")
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if rois_list is not None:
        cargs.extend(["-rois", rois_list])
    if stops_file is not None:
        cargs.extend(["-stops", execution.input_file(stops_file)])
    if wtstops_file is not None:
        cargs.extend(["-wtstops", execution.input_file(wtstops_file)])
    if tract_list is not None:
        cargs.extend(["-tract_list", tract_list])
    if threshold is not None:
        cargs.extend(["-thr", str(threshold)])
    if nsamples is not None:
        cargs.extend(["-nsamples", str(nsamples)])
    if res is not None:
        cargs.extend(["-res", str(res)])
    if ptx_options is not None:
        cargs.extend(["-ptx_options", execution.input_file(ptx_options)])
    ret = XtractBlueprintOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(f"{out_folder}/*", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XTRACT_BLUEPRINT_METADATA",
    "XtractBlueprintOutputs",
    "xtract_blueprint",
]
