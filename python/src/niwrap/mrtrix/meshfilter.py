# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

MESHFILTER_METADATA = Metadata(
    id="ec71318141eed6fc264716fddad90a1fa6d802cf",
    name="meshfilter",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MeshfilterConfig:
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


class MeshfilterOutputs(typing.NamedTuple):
    """
    Output object returned when calling `meshfilter(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file"""


def meshfilter(
    input_: InputPathType,
    filter_: str,
    output: str,
    smooth_spatial: float | int | None = None,
    smooth_influence: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MeshfilterConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MeshfilterOutputs:
    """
    meshfilter by Robert E. Smith (robert.smith@florey.edu.au).
    
    Apply filter operations to meshes.
    
    While this command has only one filter operation currently available, it
    nevertheless presents with a comparable interface to the MRtrix3 commands
    maskfilter and mrfilter commands.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/meshfilter.html
    
    Args:
        input_: the input mesh file.
        filter_: the filter to apply.Options are: smooth.
        output: the output mesh file.
        smooth_spatial: spatial extent of smoothing (default: 10mm).
        smooth_influence: influence factor for smoothing (default: 10).
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
        NamedTuple of outputs (described in `MeshfilterOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MESHFILTER_METADATA)
    cargs = []
    cargs.append("meshfilter")
    if smooth_spatial is not None:
        cargs.extend(["-smooth_spatial", str(smooth_spatial)])
    if smooth_influence is not None:
        cargs.extend(["-smooth_influence", str(smooth_influence)])
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
    cargs.append(execution.input_file(input_))
    cargs.append(filter_)
    cargs.append(output)
    ret = MeshfilterOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MESHFILTER_METADATA",
    "MeshfilterConfig",
    "MeshfilterOutputs",
    "meshfilter",
]
