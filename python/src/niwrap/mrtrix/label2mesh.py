# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

LABEL2MESH_METADATA = Metadata(
    id="383b8c89a18899ad420ff854cb634178fcf55571",
    name="label2mesh",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Label2meshConfig:
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


class Label2meshOutputs(typing.NamedTuple):
    """
    Output object returned when calling `label2mesh(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mesh_out: OutputPathType
    """the output mesh file"""


def label2mesh(
    nodes_in: InputPathType,
    mesh_out: InputPathType,
    blocky: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Label2meshConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Label2meshOutputs:
    """
    label2mesh by Robert E. Smith (robert.smith@florey.edu.au).
    
    Generate meshes from a label image.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/label2mesh.html
    
    Args:
        nodes_in: the input node parcellation image.
        mesh_out: the output mesh file.
        blocky: generate 'blocky' meshes with precise delineation of voxel\
            edges, rather than the default Marching Cubes approach.
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
        NamedTuple of outputs (described in `Label2meshOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(LABEL2MESH_METADATA)
    cargs = []
    cargs.append("label2mesh")
    if blocky:
        cargs.append("-blocky")
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
    cargs.append(execution.input_file(nodes_in))
    cargs.append(execution.input_file(mesh_out))
    ret = Label2meshOutputs(
        root=execution.output_file("."),
        mesh_out=execution.output_file(f"{pathlib.Path(mesh_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "LABEL2MESH_METADATA",
    "Label2meshConfig",
    "Label2meshOutputs",
    "label2mesh",
]
