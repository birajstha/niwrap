# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

VOXEL2MESH_METADATA = Metadata(
    id="9bf6ef38f2f75e5b53e06330bf429ad908be414a",
    name="voxel2mesh",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Voxel2meshConfig:
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


class Voxel2meshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `voxel2mesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output mesh file."""


def voxel2mesh(
    input_: InputPathType,
    output: str,
    blocky: bool = False,
    threshold: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Voxel2meshConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Voxel2meshOutputs:
    """
    voxel2mesh by Robert E. Smith (robert.smith@florey.edu.au).
    
    Generate a surface mesh representation from a voxel image.
    
    This command utilises the Marching Cubes algorithm to generate a polygonal
    surface that represents the isocontour(s) of the input image at a particular
    intensity. By default, an appropriate threshold will be determined
    automatically from the input image, however the intensity value of the
    isocontour(s) can instead be set manually using the -threhsold option.
    
    If the -blocky option is used, then the Marching Cubes algorithm will not be
    used. Instead, the input image will be interpreted as a binary mask image,
    and polygonal surfaces will be generated at the outer faces of the voxel
    clusters within the mask.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/voxel2mesh.html
    
    Args:
        input_: the input image.
        output: the output mesh file.
        blocky: generate a 'blocky' mesh that precisely represents the voxel\
            edges.
        threshold: manually set the intensity threshold for the Marching Cubes\
            algorithm.
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
        NamedTuple of outputs (described in `Voxel2meshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOXEL2MESH_METADATA)
    cargs = []
    cargs.append("voxel2mesh")
    if blocky:
        cargs.append("-blocky")
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
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
    cargs.append(output)
    ret = Voxel2meshOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOXEL2MESH_METADATA",
    "Voxel2meshConfig",
    "Voxel2meshOutputs",
    "voxel2mesh",
]
