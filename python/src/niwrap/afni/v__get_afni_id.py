# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

GET_AFNI_ID_METADATA = Metadata(
    id="6b658fe42ff0526b16617838d33ca9be119eab76",
    name="GetAfniID",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class GetAfniIdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `get_afni_id(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    unique_id: OutputPathType
    """Unique identifier of the dataset"""


def get_afni_id(
    dset: InputPathType,
    runner: Runner | None = None,
) -> GetAfniIdOutputs:
    """
    GetAfniID by AFNI Team.
    
    Returns the unique identifier of a dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@GetAfniID.html
    
    Args:
        dset: Dataset for which the unique identifier is to be returned.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `GetAfniIdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(GET_AFNI_ID_METADATA)
    cargs = []
    cargs.append("GetAfniID")
    cargs.append(execution.input_file(dset))
    ret = GetAfniIdOutputs(
        root=execution.output_file("."),
        unique_id=execution.output_file(f"stdout"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "GET_AFNI_ID_METADATA",
    "GetAfniIdOutputs",
    "get_afni_id",
]