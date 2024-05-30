# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


TCK2FIXEL_METADATA = Metadata(
    id="eb214376a576e7c83be8a1981030f92f0a68cd9f",
    name="tck2fixel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class ConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Config.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Config:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConfigOutputs`).
        """
        ret = ConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class Tck2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tck2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    config: ConfigOutputs
    """Subcommand outputs"""


def tck2fixel(
    tracks: InputPathType,
    fixel_folder_in: InputPathType,
    fixel_folder_out: str,
    fixel_data_out: str,
    angle: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Tck2fixelOutputs:
    """
    tck2fixel by David Raffelt (david.raffelt@florey.edu.au).
    
    Compute a fixel TDI map from a tractogram.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tck2fixel.html
    
    Args:
        tracks: the input tracks.
        fixel_folder_in: the input fixel folder. Used to define the fixels and
            their directions
        fixel_folder_out: the fixel folder to which the output will be written.
            This can be the same as the input folder if desired
        fixel_data_out: the name of the fixel data image.
        angle: the max angle threshold for assigning streamline tangents to
            fixels (Default: 45 degrees)
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `Tck2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCK2FIXEL_METADATA)
    cargs = []
    cargs.append("tck2fixel")
    if angle is not None:
        cargs.extend(["-angle", str(angle)])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(tracks))
    cargs.append(execution.input_file(fixel_folder_in))
    cargs.append(fixel_folder_out)
    cargs.append(fixel_data_out)
    ret = Tck2fixelOutputs(
        root=execution.output_file("."),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Config",
    "ConfigOutputs",
    "TCK2FIXEL_METADATA",
    "Tck2fixelOutputs",
    "tck2fixel",
]
