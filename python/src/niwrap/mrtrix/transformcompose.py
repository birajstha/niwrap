# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

TRANSFORMCOMPOSE_METADATA = Metadata(
    id="4a1fa00a64521e89c78077507af058c9f9ff7feb",
    name="transformcompose",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TransformcomposeConfig:
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


class TransformcomposeOutputs(typing.NamedTuple):
    """
    Output object returned when calling `transformcompose(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def transformcompose(
    input_: list[InputPathType],
    output: str,
    template: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TransformcomposeConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> TransformcomposeOutputs:
    """
    transformcompose by David Raffelt (david.raffelt@florey.edu.au).
    
    Compose any number of linear transformations and/or warps into a single
    transformation.
    
    Any linear transforms must be supplied as a 4x4 matrix in a text file (e.g.
    as per the output of mrregister). Any warp fields must be supplied as a 4D
    image representing a deformation field (e.g. as output from mrrregister
    -nl_warp).
    
    Input transformations should be provided to the command in the order in
    which they would be applied to an image if they were to be applied
    individually.
    
    If all input transformations are linear, and the -template option is not
    provided, then the file output by the command will also be a linear
    transformation saved as a 4x4 matrix in a text file. If a template image is
    supplied, then the output will always be a deformation field. If at least
    one of the inputs is a warp field, then the output will be a deformation
    field, which will be defined on the grid of the last input warp image
    supplied if the -template option is not used.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/transformcompose.html
    
    Args:
        input_: the input transforms (either linear or non-linear warps).
        output: the output file (may be a linear transformation text file, or a\
            deformation warp field image, depending on usage).
        template: define the output grid defined by a template image.
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
        NamedTuple of outputs (described in `TransformcomposeOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TRANSFORMCOMPOSE_METADATA)
    cargs = []
    cargs.append("transformcompose")
    if template is not None:
        cargs.extend(["-template", execution.input_file(template)])
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
    cargs.extend([execution.input_file(f) for f in input_])
    cargs.append(output)
    ret = TransformcomposeOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TRANSFORMCOMPOSE_METADATA",
    "TransformcomposeConfig",
    "TransformcomposeOutputs",
    "transformcompose",
]
