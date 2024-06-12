# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

SET_MAP_NAMES_METADATA = Metadata(
    id="564bae9e86701df79e5834a7280f70b167c46077",
    name="set-map-names",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class SetMapNamesMap:
    """
    specify a map to set the name of
    """
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        return cargs


class SetMapNamesOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_map_names(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def set_map_names(
    data_file: str,
    opt_name_file_file: str | None = None,
    opt_from_data_file_file: str | None = None,
    map_: list[SetMapNamesMap] = None,
    runner: Runner = None,
) -> SetMapNamesOutputs:
    """
    set-map-names by Washington University School of Medicin.
    
    Set the name of one or more maps in a file.
    
    Sets the name of one or more maps for metric, shape, label, volume, cifti
    scalar or cifti label files. You must specify either -name-file, or
    -from-data-file, or at least one -map option. The three option types are
    mutually exclusive.
    
    Args:
        data_file: the file to set the map names of.
        opt_name_file_file: use a text file to replace all map names: text file\
            containing map names, one per line.
        opt_from_data_file_file: use the map names from another data file: a\
            data file with the same number of maps.
        map_: specify a map to set the name of.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SetMapNamesOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SET_MAP_NAMES_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-set-map-names")
    cargs.append(data_file)
    if opt_name_file_file is not None:
        cargs.extend(["-name-file", opt_name_file_file])
    if opt_from_data_file_file is not None:
        cargs.extend(["-from-data-file", opt_from_data_file_file])
    if map_ is not None:
        cargs.extend(["-map", *[a for c in [s.run(execution) for s in map_] for a in c]])
    ret = SetMapNamesOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SET_MAP_NAMES_METADATA",
    "SetMapNamesMap",
    "SetMapNamesOutputs",
    "set_map_names",
]
