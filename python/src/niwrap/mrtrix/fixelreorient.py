# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FIXELREORIENT_METADATA = Metadata(
    id="7be2d5220e46f4ccbe84989d75dbfad0138a3943",
    name="fixelreorient",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class FixelreorientConfig:
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


class FixelreorientOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fixelreorient(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fixel_out: OutputPathType
    """the output fixel directory. If the the input and output directories are the same, the existing directions file will be replaced (providing the -force option is supplied). If a new directory is supplied then the fixel directions and all other fixel data will be copied to the new directory."""


def fixelreorient(
    fixel_in: InputPathType,
    warp: InputPathType,
    fixel_out: str,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[FixelreorientConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> FixelreorientOutputs:
    """
    fixelreorient by David Raffelt (david.raffelt@florey.edu.au).
    
    Reorient fixel directions.
    
    Reorientation is performed by transforming the vector representing the fixel
    direction with the Jacobian (local affine transform) computed at each voxel
    in the warp, then re-normalising the vector.
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fixelreorient.html
    
    Args:
        fixel_in: the input fixel directory.
        warp: a 4D deformation field used to perform reorientation.\
            Reorientation is performed by applying the Jacobian affine transform in\
            each voxel in the warp, then re-normalising the vector representing the\
            fixel direction.
        fixel_out: the output fixel directory. If the the input and output\
            directories are the same, the existing directions file will be replaced\
            (providing the -force option is supplied). If a new directory is\
            supplied then the fixel directions and all other fixel data will be\
            copied to the new directory.
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
        NamedTuple of outputs (described in `FixelreorientOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIXELREORIENT_METADATA)
    cargs = []
    cargs.append("fixelreorient")
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
    cargs.append(execution.input_file(fixel_in))
    cargs.append(execution.input_file(warp))
    cargs.append(fixel_out)
    ret = FixelreorientOutputs(
        root=execution.output_file("."),
        fixel_out=execution.output_file(f"{fixel_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIXELREORIENT_METADATA",
    "FixelreorientConfig",
    "FixelreorientOutputs",
    "fixelreorient",
]
