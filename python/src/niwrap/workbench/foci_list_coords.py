# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

FOCI_LIST_COORDS_METADATA = Metadata(
    id="db5c91253f13371240846253e87cfab661e3cefc",
    name="foci-list-coords",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FociListCoordsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_list_coords(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def foci_list_coords(
    foci_file: InputPathType,
    coord_file_out: str,
    opt_names_out_names_file_out: str | None = None,
    runner: Runner = None,
) -> FociListCoordsOutputs:
    """
    foci-list-coords by Washington University School of Medicin.
    
    Output foci coordinates in a text file.
    
    Output the coordinates for every focus in the foci file, and optionally the
    focus names in a second text file.
    
    Args:
        foci_file: input foci file.
        coord_file_out: output - the output coordinate text file.
        opt_names_out_names_file_out: output the foci names: output - text file\
            to put foci names in.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociListCoordsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_LIST_COORDS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-list-coords")
    cargs.append(execution.input_file(foci_file))
    cargs.append(coord_file_out)
    if opt_names_out_names_file_out is not None:
        cargs.extend(["-names-out", opt_names_out_names_file_out])
    ret = FociListCoordsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOCI_LIST_COORDS_METADATA",
    "FociListCoordsOutputs",
    "foci_list_coords",
]
