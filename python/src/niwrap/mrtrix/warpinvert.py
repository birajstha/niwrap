# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


WARPINVERT_METADATA = Metadata(
    id="1c17a942ecf4a167fa5592c9d400d5c806e42c99",
    name="warpinvert",
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


class WarpinvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warpinvert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out: OutputPathType
    """the output warp image."""
    config: ConfigOutputs
    """Subcommand outputs"""


def warpinvert(
    in_: InputPathType,
    out: InputPathType,
    template: InputPathType | None = None,
    displacement: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> WarpinvertOutputs:
    """
    warpinvert by Robert E. Smith (robert.smith@florey.edu.au) and David Raffelt
    (david.raffelt@florey.edu.au).
    
    Invert a non-linear warp field.
    
    By default, this command assumes that the input warp field is a deformation
    field, i.e. each voxel stores the corresponding position in the other image
    (in scanner space), and the calculated output warp image will also be a
    deformation field. If the input warp field is instead a displacment field,
    i.e. where each voxel stores an offset from which to sample the other image
    (but still in scanner space), then the -displacement option should be used;
    the output warp field will additionally be calculated as a displacement
    field in this case.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/warpinvert.html
    
    Args:
        in_: the input warp image.
        out: the output warp image.
        template: define a template image grid for the output warp
        displacement: indicates that the input warp field is a displacement
            field; the output will also be a displacement field
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
        NamedTuple of outputs (described in `WarpinvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARPINVERT_METADATA)
    cargs = []
    cargs.append("warpinvert")
    if template is not None:
        cargs.extend(["-template", execution.input_file(template)])
    if displacement:
        cargs.append("-displacement")
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
    cargs.append(execution.input_file(in_))
    cargs.append(execution.input_file(out))
    ret = WarpinvertOutputs(
        root=execution.output_file("."),
        out=execution.output_file(f"{pathlib.Path(out).name}"),
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "Config",
    "ConfigOutputs",
    "WARPINVERT_METADATA",
    "WarpinvertOutputs",
    "warpinvert",
]
