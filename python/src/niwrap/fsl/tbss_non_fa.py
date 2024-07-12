# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

TBSS_NON_FA_METADATA = Metadata(
    id="a0088890dcf1b6d2d1266176267e880674efa875",
    name="tbss_non_FA",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class TbssNonFaOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tbss_non_fa(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    merged_output: OutputPathType
    """Merged output file"""


def tbss_non_fa(
    input_files: list[InputPathType],
    output_file: str,
    concat_x: bool = False,
    concat_y: bool = False,
    concat_z: bool = False,
    concat_t: bool = False,
    concat_auto: bool = False,
    concat_tr: float | int | None = 0,
    volume_number: float | int | None = None,
    runner: Runner | None = None,
) -> TbssNonFaOutputs:
    """
    tbss_non_FA by FMRIB, Oxford Centre for Functional MRI of the Brain.
    
    TBSS processing for non-FA images.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/TBSS/UserGuide
    
    Args:
        input_files: Images to concatenate.
        output_file: Output file for merged images.
        concat_x: Concatenate images in the x direction.
        concat_y: Concatenate images in the y direction.
        concat_z: Concatenate images in the z direction.
        concat_t: Concatenate images in time.
        concat_auto: Auto-choose: single slices -> volume, volumes -> 4D (time\
            series).
        concat_tr: Concatenate images in time and set the output image TR\
            (repetition time) to the final option value.
        volume_number: Only use volume <N> from each input file (first volume\
            is 0 not 1).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `TbssNonFaOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TBSS_NON_FA_METADATA)
    cargs = []
    cargs.append("fslmerge")
    if concat_auto:
        cargs.append("-a")
    cargs.append(output_file)
    cargs.extend([execution.input_file(f) for f in input_files])
    if concat_tr is not None:
        cargs.extend(["-tr", str(concat_tr)])
    if volume_number is not None:
        cargs.extend(["-n", str(volume_number)])
    ret = TbssNonFaOutputs(
        root=execution.output_file("."),
        merged_output=execution.output_file(f"{output_file}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TBSS_NON_FA_METADATA",
    "TbssNonFaOutputs",
    "tbss_non_fa",
]
