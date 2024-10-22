# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_SUB_CONFIG_METADATA = Metadata(
    id="a12a2b0d79584fa9a2530b2e6ee9858bc59cbd7d.boutiques",
    name="fsl_sub_config",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslSubConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_sub_config(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_sub_config(
    cluster_system: typing.Literal["shell", "sge", "slurm"],
    help_flag: bool = False,
    runner: Runner | None = None,
) -> FslSubConfigOutputs:
    """
    FSL cluster submission configuration examples.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        cluster_system: Choice of cluster system configuration example to\
            output. Options are 'shell', 'sge', or 'slurm'.
        help_flag: Show help message and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslSubConfigOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_SUB_CONFIG_METADATA)
    cargs = []
    cargs.append("fsl_sub_config")
    cargs.append(cluster_system)
    if help_flag:
        cargs.append("-h")
    ret = FslSubConfigOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_SUB_CONFIG_METADATA",
    "FslSubConfigOutputs",
    "fsl_sub_config",
]
