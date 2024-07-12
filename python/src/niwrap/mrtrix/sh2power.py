# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

SH2POWER_METADATA = Metadata(
    id="1ab49e4ed2dfe080fcbd257db71a6d4309225297",
    name="sh2power",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Sh2powerConfig:
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


class Sh2powerOutputs(typing.NamedTuple):
    """
    Output object returned when calling `sh2power(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    power: OutputPathType
    """the output power image."""


def sh2power(
    sh: InputPathType,
    power: str,
    spectrum: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Sh2powerConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Sh2powerOutputs:
    """
    sh2power by J-Donald Tournier (jdtournier@gmail.com).
    
    Compute the total power of a spherical harmonics image.
    
    This command computes the sum of squared SH coefficients, which equals the
    mean-squared amplitude of the spherical function it represents.
    
    The spherical harmonic coefficients are stored according the conventions
    described the main documentation, which can be found at the following link:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/spherical_harmonics.html
    
    References:
    
    .
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/sh2power.html
    
    Args:
        sh: the input spherical harmonics coefficients image.
        power: the output power image.
        spectrum: output the power spectrum, i.e., the power contained within\
            each harmonic degree (l=0, 2, 4, ...) as a 4-D image.
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
        NamedTuple of outputs (described in `Sh2powerOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SH2POWER_METADATA)
    cargs = []
    cargs.append("sh2power")
    if spectrum:
        cargs.append("-spectrum")
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
    cargs.append(execution.input_file(sh))
    cargs.append(power)
    ret = Sh2powerOutputs(
        root=execution.output_file("."),
        power=execution.output_file(f"{power}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SH2POWER_METADATA",
    "Sh2powerConfig",
    "Sh2powerOutputs",
    "sh2power",
]
