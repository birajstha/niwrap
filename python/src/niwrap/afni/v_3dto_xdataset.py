# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DTO_XDATASET_METADATA = Metadata(
    id="70a5468c88f08d3cefa21702fad29ffcbc95ec9a",
    name="3dtoXdataset",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dtoXdatasetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dto_xdataset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_sdat: OutputPathType
    """Output file in .sdat format"""


def v_3dto_xdataset(
    prefix: str,
    mask: InputPathType,
    input_files: list[InputPathType],
    runner: Runner | None = None,
) -> V3dtoXdatasetOutputs:
    """
    3dtoXdataset by AFNI Team.
    
    Convert input datasets to the format needed for 3dClustSimX.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dtoXdataset.html
    
    Args:
        prefix: Prefix for the output file.
        mask: Mask dataset file.
        input_files: Input datasets to be converted.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dtoXdatasetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3DTO_XDATASET_METADATA)
    cargs = []
    cargs.append("3dtoXdataset")
    cargs.append("-prefix")
    cargs.append(prefix)
    cargs.append(execution.input_file(mask))
    cargs.extend([execution.input_file(f) for f in input_files])
    ret = V3dtoXdatasetOutputs(
        root=execution.output_file("."),
        output_sdat=execution.output_file(f"{prefix}.sdat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dtoXdatasetOutputs",
    "V_3DTO_XDATASET_METADATA",
    "v_3dto_xdataset",
]