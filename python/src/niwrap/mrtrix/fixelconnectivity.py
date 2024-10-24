# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIXELCONNECTIVITY_METADATA = Metadata(
    id="811fe5b2580b330dbeded0c16e56819fd86331a7.boutiques",
    name="fixelconnectivity",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelconnectivityConfig:
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
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class FixelconnectivityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelconnectivity(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    matrix: OutputPathType
    """the output fixel-fixel connectivity matrix directory path"""


def fixelconnectivity(
    fixel_directory: InputPathType,
    tracks: InputPathType,
    matrix: str,
    threshold: float | None = None,
    angle: float | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelconnectivityConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> FixelconnectivityOutputs:
    """
    Generate a fixel-fixel connectivity matrix.
    
    This command will generate a directory containing three images, which
    encodes the fixel-fixel connectivity matrix. Documentation regarding this
    format and how to use it will come in the future.
    
    References:
    
    .
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        fixel_directory: the directory containing the fixels between which\
            connectivity will be quantified.
        tracks: the tracks used to determine fixel-fixel connectivity.
        matrix: the output fixel-fixel connectivity matrix directory path.
        threshold: a threshold to define the required fraction of shared\
            connections to be included in the neighbourhood (default: 0.01).
        angle: the max angle threshold for assigning streamline tangents to\
            fixels (Default: 45 degrees).
        mask: provide a fixel data file containing a mask of those fixels to be\
            computed; fixels outside the mask will be empty in the output matrix.
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
        NamedTuple of outputs (described in `FixelconnectivityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCONNECTIVITY_METADATA)
    cargs = []
    cargs.append("fixelconnectivity")
    if threshold is not None:
        cargs.extend([
            "-threshold",
            str(threshold)
        ])
    if angle is not None:
        cargs.extend([
            "-angle",
            str(angle)
        ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(fixel_directory))
    cargs.append(execution.input_file(tracks))
    cargs.append(matrix)
    ret = FixelconnectivityOutputs(
        root=execution.output_file("."),
        matrix=execution.output_file(matrix),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELCONNECTIVITY_METADATA",
    "FixelconnectivityConfig",
    "FixelconnectivityOutputs",
    "fixelconnectivity",
]
