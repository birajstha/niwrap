# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

INSTALL_MEICA_DEMO_METADATA = Metadata(
    id="6f730f1b23805b68435905ad6cd0b5998f5edd5a.boutiques",
    name="Install_MEICA_Demo",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class InstallMeicaDemoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `install_meica_demo(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    readme_file: OutputPathType
    """Details of the demo archive"""


def install_meica_demo(
    demo_archive: InputPathType,
    runner: Runner | None = None,
) -> InstallMeicaDemoOutputs:
    """
    Installs the demo archive for Prantik Kundu MEICA denoising tools. After the
    archive is downloaded and unpacked, see its README.txt for details.
    
    Author: AFNI Team
    
    URL:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@Install_MEICA_Demo.html
    
    Args:
        demo_archive: Demo archive to install (e.g. meica_demo.zip).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `InstallMeicaDemoOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(INSTALL_MEICA_DEMO_METADATA)
    cargs = []
    cargs.append("Install_MEICA_Demo")
    cargs.append(execution.input_file(demo_archive))
    ret = InstallMeicaDemoOutputs(
        root=execution.output_file("."),
        readme_file=execution.output_file("README.txt"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "INSTALL_MEICA_DEMO_METADATA",
    "InstallMeicaDemoOutputs",
    "install_meica_demo",
]