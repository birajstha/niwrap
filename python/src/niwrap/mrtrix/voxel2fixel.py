# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOXEL2FIXEL_METADATA = Metadata(
    id="3ee38fc4c944bbf53830a1ae211114adba9f0623",
    name="voxel2fixel",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Voxel2fixelConfig:
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


class Voxel2fixelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `voxel2fixel(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def voxel2fixel(
    image_in: InputPathType,
    fixel_directory_in: InputPathType,
    fixel_directory_out: str,
    fixel_data_out: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2fixelConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Voxel2fixelOutputs:
    """
    voxel2fixel by David Raffelt (david.raffelt@florey.edu.au).
    
    Map the scalar value in each voxel to all fixels within that voxel.
    
    This command is designed to enable CFE-based statistical analysis to be
    performed on voxel-wise measures.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/voxel2fixel.html
    
    Args:
        image_in: the input image.
        fixel_directory_in: the input fixel directory. Used to define the\
            fixels and their directions.
        fixel_directory_out: the fixel directory where the output will be\
            written. This can be the same as the input directory if desired.
        fixel_data_out: the name of the fixel data image.
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Voxel2fixelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOXEL2FIXEL_METADATA)
    cargs = []
    cargs.append("voxel2fixel")
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
    cargs.append(execution.input_file(image_in))
    cargs.append(execution.input_file(fixel_directory_in))
    cargs.append(fixel_directory_out)
    cargs.append(fixel_data_out)
    ret = Voxel2fixelOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOXEL2FIXEL_METADATA",
    "Voxel2fixelConfig",
    "Voxel2fixelOutputs",
    "voxel2fixel",
]
