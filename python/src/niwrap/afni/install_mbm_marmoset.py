# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INSTALL_MBM_MARMOSET_METADATA = Metadata(
    id="eddeae997cf598c4fa8e72be036616de792633f0.boutiques",
    name="Install_MBM_Marmoset",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class InstallMbmMarmosetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_mbm_marmoset(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def install_mbm_marmoset(
    wget: bool = False,
    curl: bool = False,
    runner: Runner | None = None,
) -> InstallMbmMarmosetOutputs:
    """
    Installs the NIH marmoset template and atlases.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_MBM_Marmoset.html
    
    Args:
        wget: Use wget to download archive. Script chooses by default with\
            preference for curl.
        curl: Use curl to download archive. Script chooses by default with\
            preference for curl.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallMbmMarmosetOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_MBM_MARMOSET_METADATA)
    cargs = []
    cargs.append("@Install_MBM_Marmoset")
    if wget:
        cargs.append("-wget")
    if curl:
        cargs.append("-curl")
    ret = InstallMbmMarmosetOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_MBM_MARMOSET_METADATA",
    "InstallMbmMarmosetOutputs",
    "install_mbm_marmoset",
]