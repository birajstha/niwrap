# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_TSHIFT_METADATA = Metadata(
    id="ae3eac68bd5962b0fe249f42757c87f6a26d57fd",
    name="3dTshift",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dTshiftOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_tshift(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""
    out_file_: OutputPathType
    """Output file."""
    timing_file: OutputPathType
    """Afni formatted timing file, if ``slice_timing`` is a list."""


def v_3d_tshift(
    in_file: InputPathType,
    ignore: int | None = None,
    interp: typing.Literal["Fourier", "linear", "cubic", "quintic", "heptic"] | None = None,
    num_threads: int | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    rlt: bool = False,
    rltplus: bool = False,
    slice_encoding_direction: typing.Literal["k", "k-"] | None = None,
    slice_timing: InputPathType | None = None,
    slice_timing_2: list[float | int] | None = None,
    tpattern: typing.Literal["alt+z", "altplus", "alt+z2", "alt-z", "altminus", "alt-z2", "seq+z", "seqplus", "seq-z", "seqminus"] | None = None,
    tpattern_2: str | None = None,
    tr: str | None = None,
    tslice: int | None = None,
    tzero: float | int | None = None,
    runner: Runner | None = None,
) -> V3dTshiftOutputs:
    """
    3dTshift by AFNI Team.
    
    Shifts voxel time series from input so that separate slices are aligned to
    the same temporal origin.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dTshift.html
    
    Args:
        in_file: Input file to 3dtshift.
        ignore: Ignore the first set of points specified.
        interp: 'fourier' or 'linear' or 'cubic' or 'quintic' or 'heptic'.\
            Different interpolation methods (see 3dtshift for details) default =\
            fourier.
        num_threads: Set number of threads.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        rlt: Before shifting, remove the mean and linear trend.
        rltplus: Before shifting, remove the mean and linear trend and later\
            put back the mean.
        slice_encoding_direction: 'k' or 'k-'. Direction in which slice_timing\
            is specified (default: k). if negative,slice_timing is defined in\
            reverse order, that is, the first entry corresponds to the slice with\
            the largest index, and the final entry corresponds to slice index zero.\
            only in effect when slice_timing is passed as list, not when it is\
            passed as file.
        slice_timing: file or string or a list of items which are a float. Time\
            offsets from the volume acquisition onset for each slice.
        slice_timing_2: file or string or a list of items which are a float.\
            Time offsets from the volume acquisition onset for each slice.
        tpattern: 'alt+z' or 'altplus' or 'alt+z2' or 'alt-z' or 'altminus' or\
            'alt-z2' or 'seq+z' or 'seqplus' or 'seq-z' or 'seqminus' or a string.\
            Use specified slice time pattern rather than one in header.
        tpattern_2: 'alt+z' or 'altplus' or 'alt+z2' or 'alt-z' or 'altminus'\
            or 'alt-z2' or 'seq+z' or 'seqplus' or 'seq-z' or 'seqminus' or a\
            string. Use specified slice time pattern rather than one in header.
        tr: Manually set the tr. you can attach suffix "s" for seconds or "ms"\
            for milliseconds.
        tslice: Align each slice to time offset of given slice.
        tzero: Align each slice to given time offset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dTshiftOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_TSHIFT_METADATA)
    cargs = []
    cargs.append("3dTshift")
    cargs.append(execution.input_file(in_file))
    if ignore is not None:
        cargs.extend(["-ignore", str(ignore)])
    if interp is not None:
        cargs.extend(["-", interp])
    cargs.append("[OUT_FILE]")
    if outputtype is not None:
        cargs.append(outputtype)
    if rlt:
        cargs.append("-rlt")
    if rltplus:
        cargs.append("-rlt+")
    if slice_encoding_direction is not None:
        cargs.append(slice_encoding_direction)
    if slice_timing_2 is not None:
        cargs.extend(["-tpattern @", *map(str, slice_timing_2)])
    if tpattern_2 is not None:
        cargs.extend(["-tpattern", tpattern_2])
    if tr is not None:
        cargs.extend(["-TR", tr])
    if tslice is not None:
        cargs.extend(["-slice", str(tslice)])
    if tzero is not None:
        cargs.extend(["-tzero", str(tzero)])
    ret = V3dTshiftOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{pathlib.Path(in_file).name}_tshift", optional=True),
        out_file_=execution.output_file(f"out_file", optional=True),
        timing_file=execution.output_file(f"timing_file", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dTshiftOutputs",
    "V_3D_TSHIFT_METADATA",
    "v_3d_tshift",
]
