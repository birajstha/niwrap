# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

XHEMIREG_METADATA = Metadata(
    id="f01b4255c8c371fe9d8cf7dac45f58046ba01896.boutiques",
    name="xhemireg",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class XhemiregOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xhemireg(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def xhemireg(
    subject: str,
    output_dir: str | None = None,
    map_lh: bool = False,
    map_rh: bool = False,
    perform_reg: bool = False,
    tal_compute: bool = False,
    no_tal_compute: bool = False,
    tal_estimate: bool = False,
    no_tal_estimate: bool = False,
    gcaprep: str | None = None,
    threads: float | None = None,
    version: bool = False,
    help_: bool = False,
    runner: Runner | None = None,
) -> XhemiregOutputs:
    """
    Tool for hemisphere registration in neuroimaging.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: Subject ID for the hemisphere registration process.
        output_dir: Output directory for the hemisphere registration.
        map_lh: Map from left hemisphere to right hemisphere.
        map_rh: Map from right hemisphere to left hemisphere.
        perform_reg: Perform registration to create sphere.reg.
        tal_compute: Recompute Talairach registration.
        no_tal_compute: Do not perform Talairach registration.
        tal_estimate: Compute estimate of Talairach registration from unflipped\
            registration.
        no_tal_estimate: Do not perform estimation of Talairach registration.
        gcaprep: Prepare GCA for training symmetrical GCA atlases.
        threads: Number of threads used, applicable with --gcaprep option.
        version: Print version and exit.
        help_: Print help and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `XhemiregOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(XHEMIREG_METADATA)
    cargs = []
    cargs.append("xhemireg")
    cargs.extend([
        "--s",
        subject
    ])
    if output_dir is not None:
        cargs.extend([
            "--o",
            output_dir
        ])
    if map_lh:
        cargs.append("--lh")
    if map_rh:
        cargs.append("--rh")
    if perform_reg:
        cargs.append("--reg")
    if tal_compute:
        cargs.append("--tal-compute")
    if no_tal_compute:
        cargs.append("--no-tal-compute")
    if tal_estimate:
        cargs.append("--tal-estimate")
    if no_tal_estimate:
        cargs.append("--no-tal-estimate")
    if gcaprep is not None:
        cargs.extend([
            "--gcaprep",
            gcaprep
        ])
    if threads is not None:
        cargs.extend([
            "--threads",
            str(threads)
        ])
    if version:
        cargs.append("--version")
    if help_:
        cargs.append("--help")
    ret = XhemiregOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XHEMIREG_METADATA",
    "XhemiregOutputs",
    "xhemireg",
]
