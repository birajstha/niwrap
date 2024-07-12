# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

TSFTHRESHOLD_METADATA = Metadata(
    id="9f2b6d460e04e0cdb680c50341661efb12b982f3",
    name="tsfthreshold",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TsfthresholdConfig:
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


class TsfthresholdOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tsfthreshold(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the binary output track scalar file"""


def tsfthreshold(
    input_: InputPathType,
    t: float | int,
    output: str,
    invert: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TsfthresholdConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TsfthresholdOutputs:
    """
    tsfthreshold by David Raffelt (david.raffelt@florey.edu.au).
    
    Threshold and invert track scalar files.
    
    
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tsfthreshold.html
    
    Args:
        input_: the input track scalar file.
        t: the desired threshold.
        output: the binary output track scalar file.
        invert: invert the output mask.
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
        NamedTuple of outputs (described in `TsfthresholdOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TSFTHRESHOLD_METADATA)
    cargs = []
    cargs.append("tsfthreshold")
    if invert:
        cargs.append("-invert")
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
    cargs.append(str(t))
    cargs.append(output)
    ret = TsfthresholdOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TSFTHRESHOLD_METADATA",
    "TsfthresholdConfig",
    "TsfthresholdOutputs",
    "tsfthreshold",
]
