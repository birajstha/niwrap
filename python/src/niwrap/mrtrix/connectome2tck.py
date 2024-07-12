# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CONNECTOME2TCK_METADATA = Metadata(
    id="9b8f76e3780a04a62382dbfad738ea0d57198eda",
    name="connectome2tck",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Connectome2tckConfig:
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


class Connectome2tckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `connectome2tck(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def connectome2tck(
    tracks_in: InputPathType,
    assignments_in: InputPathType,
    prefix_out: str,
    nodes: list[int] | None = None,
    exclusive: bool = False,
    files: str | None = None,
    exemplars: InputPathType | None = None,
    keep_unassigned: bool = False,
    keep_self: bool = False,
    tck_weights_in: InputPathType | None = None,
    prefix_tck_weights_out: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Connectome2tckConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Connectome2tckOutputs:
    """
    connectome2tck by Robert E. Smith (robert.smith@florey.edu.au).
    
    Extract streamlines from a tractogram based on their assignment to
    parcellated nodes.
    
    The compulsory input file "assignments_in" should contain a text file where
    there is one row for each streamline, and each row contains a list of
    numbers corresponding to the parcels to which that streamline was assigned
    (most typically there will be two entries per streamline, one for each
    endpoint; but this is not strictly a requirement). This file will most
    typically be generated using the tck2connectome command with the
    -out_assignments option.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/connectome2tck.html
    
    Args:
        tracks_in: the input track file.
        assignments_in: input text file containing the node assignments for\
            each streamline.
        prefix_out: the output file / prefix.
        nodes: only select tracks that involve a set of nodes of interest\
            (provide as a comma-separated list of integers).
        exclusive: only select tracks that exclusively connect nodes from\
            within the list of nodes of interest.
        files: select how the resulting streamlines will be grouped in output\
            files. Options are: per_edge, per_node, single (default: per_edge).
        exemplars: generate a mean connection exemplar per edge, rather than\
            keeping all streamlines (the parcellation node image must be provided\
            in order to constrain the exemplar endpoints).
        keep_unassigned: by default, the program discards those streamlines\
            that are not successfully assigned to a node. Set this option to\
            generate corresponding outputs containing these streamlines (labelled\
            as node index 0).
        keep_self: by default, the program will not output streamlines that\
            connect to the same node at both ends. Set this option to instead keep\
            these self-connections.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
        prefix_tck_weights_out: provide a prefix for outputting a text file\
            corresponding to each output file, each containing only the streamline\
            weights relevant for that track file.
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
        NamedTuple of outputs (described in `Connectome2tckOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONNECTOME2TCK_METADATA)
    cargs = []
    cargs.append("connectome2tck")
    if nodes is not None:
        cargs.extend(["-nodes", ",".join(map(str, nodes))])
    if exclusive:
        cargs.append("-exclusive")
    if files is not None:
        cargs.extend(["-files", files])
    if exemplars is not None:
        cargs.extend(["-exemplars", execution.input_file(exemplars)])
    if keep_unassigned:
        cargs.append("-keep_unassigned")
    if keep_self:
        cargs.append("-keep_self")
    if tck_weights_in is not None:
        cargs.extend(["-tck_weights_in", execution.input_file(tck_weights_in)])
    if prefix_tck_weights_out is not None:
        cargs.extend(["-prefix_tck_weights_out", prefix_tck_weights_out])
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
    cargs.append(execution.input_file(tracks_in))
    cargs.append(execution.input_file(assignments_in))
    cargs.append(prefix_out)
    ret = Connectome2tckOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONNECTOME2TCK_METADATA",
    "Connectome2tckConfig",
    "Connectome2tckOutputs",
    "connectome2tck",
]
