# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FIXELCORRESPONDENCE_METADATA = Metadata(
    id="e504e8529648fd4befb8831d2415e0de7107e1d1",
    name="fixelcorrespondence",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelcorrespondenceConfig:
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


class FixelcorrespondenceOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelcorrespondence(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fixelcorrespondence(
    subject_data: InputPathType,
    template_directory: InputPathType,
    output_directory: str,
    output_data: str,
    angle: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelcorrespondenceConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> FixelcorrespondenceOutputs:
    """
    fixelcorrespondence by David Raffelt (david.raffelt@florey.edu.au).
    
    Obtain fixel-fixel correpondence between a subject fixel image and a
    template fixel mask.
    
    It is assumed that the subject image has already been spatially normalised
    and is aligned with the template. The output fixel image will have the same
    fixels (and directions) of the template.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixelcorrespondence.html
    
    Args:
        subject_data: the input subject fixel data file. This should be a file\
            inside the fixel directory.
        template_directory: the input template fixel directory.
        output_directory: the fixel directory where the output file will be\
            written.
        output_data: the name of the output fixel data file. This will be\
            placed in the output fixel directory.
        angle: the max angle threshold for computing inter-subject fixel\
            correspondence (Default: 45 degrees).
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
        NamedTuple of outputs (described in `FixelcorrespondenceOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELCORRESPONDENCE_METADATA)
    cargs = []
    cargs.append("fixelcorrespondence")
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
    cargs.append(execution.input_file(subject_data))
    cargs.append(execution.input_file(template_directory))
    cargs.append(output_directory)
    cargs.append(output_data)
    ret = FixelcorrespondenceOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELCORRESPONDENCE_METADATA",
    "FixelcorrespondenceConfig",
    "FixelcorrespondenceOutputs",
    "fixelcorrespondence",
]
