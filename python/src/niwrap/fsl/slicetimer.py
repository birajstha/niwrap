# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SLICETIMER_METADATA = Metadata(
    id="2b409c00e1e7f61468553b21bd3524a5aed51472",
    name="slicetimer",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class SlicetimerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `slicetimer(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_timeseries: OutputPathType | None
    """Output timeseries"""


def slicetimer(
    infile: InputPathType,
    outfile: InputPathType | None = None,
    verbose_flag: bool = False,
    down_flag: bool = False,
    tr_value: float | int | None = None,
    direction: str | None = None,
    odd_flag: bool = False,
    tcustom_file: InputPathType | None = None,
    tglobal_value: float | int | None = None,
    ocustom_file: InputPathType | None = None,
    runner: Runner = None,
) -> SlicetimerOutputs:
    """
    slicetimer by University of Oxford, FMRIB.
    
    FMRIB's Interpolation for Slice Timing.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Slicetimer
    
    Args:
        infile: Filename of input timeseries
        outfile: Filename of output timeseries
        verbose_flag: Switch on diagnostic messages
        down_flag: Reverse slice indexing (default is: slices were acquired
            bottom-up)
        tr_value: Specify TR of data - default is 3s
        direction: Direction of slice acquisition (x=1,y=2,z=3) - default is z
        odd_flag: Use interleaved acquisition
        tcustom_file: Filename of single-column slice timings, in fractions of
            TR, +ve values shift slices forward in time
        tglobal_value: Global shift in fraction of TR, (default is 0)
        ocustom_file: Filename of single-column custom interleave order file
            (first slice is referred to as 1 not 0)
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `SlicetimerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SLICETIMER_METADATA)
    cargs = []
    cargs.append("slicetimer")
    cargs.append("-i")
    cargs.extend(["-i", execution.input_file(infile)])
    cargs.append("[-o")
    cargs.append("OUTPUT_FILE]")
    cargs.append("[--down]")
    cargs.append("[-r")
    cargs.append("TR_VALUE]")
    cargs.append("[-d")
    cargs.append("DIRECTION]")
    cargs.append("[--odd]")
    cargs.append("[--tcustom")
    cargs.append("TCUSTOM_FILE]")
    cargs.append("[--tglobal")
    cargs.append("TGLOBAL_VALUE]")
    cargs.append("[--ocustom")
    cargs.append("OCUSTOM_FILE]")
    cargs.append("[-v]")
    ret = SlicetimerOutputs(
        root=execution.output_file("."),
        output_timeseries=execution.output_file(f"{pathlib.Path(outfile).name}", optional=True) if outfile is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SLICETIMER_METADATA",
    "SlicetimerOutputs",
    "slicetimer",
]
