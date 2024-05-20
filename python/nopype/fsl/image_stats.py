# This file was auto generated by styx
# Do not edit this file directly

import typing

from ..styxdefs import *


IMAGE_STATS_METADATA = Metadata(
    id="b420aa3204337c516b306b71a494d7783ea7ad5b",
    name="ImageStats",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ImageStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `image_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_stat: OutputPathType
    """Any value. Stats output."""


def image_stats(
    runner: Runner,
    in_file: InputPathType,
    op_string: str,
    index_mask_file: InputPathType | None = None,
    mask_file: InputPathType | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    split_4d: bool = False,
) -> ImageStatsOutputs:
    """
    ImageStats, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    ImageStats).
    Use FSL fslstats command to calculate stats from images `FSL info
    <http://www.fmrib.ox.ac.uk/fslcourse/lectures/practicals/intro/index.htm#fslutils>`_
    
    Args:
        runner: Command runner
        in_file: Input file to generate stats of.
        op_string: String defining the operation, options are applied in order,
            e.g. -m -l 10 -m will report the non-zero mean, apply a threshold and
            then report the new nonzero mean.
        index_mask_file: Generate separate n submasks from indexmask, for
            indexvalues 1..n where n is the maximum index value in indexmask, and
            generate statistics for each submask.
        mask_file: Mask file used for option -k %s.
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.
            Fsl output type.
        split_4d: Give a separate output line for each 3d volume of a 4d
            timeseries.
    Returns:
        NamedTuple of outputs (described in `ImageStatsOutputs`).
    """
    execution = runner.start_execution(IMAGE_STATS_METADATA)
    cargs = []
    cargs.append("ImageStats")
    if split_4d:
        cargs.append("-t")
    if index_mask_file is not None:
        cargs.extend(["-K", execution.input_file(index_mask_file)])
    cargs.append(execution.input_file(in_file))
    cargs.append(op_string)
    cargs.append("[ARGS]")
    cargs.append("[ENVIRON]")
    if mask_file is not None:
        cargs.append(execution.input_file(mask_file))
    if output_type is not None:
        cargs.append(output_type)
    ret = ImageStatsOutputs(
        root=execution.output_file("."),
        out_stat=execution.output_file(f"out_stat", optional=True),
    )
    execution.run(cargs)
    return ret
