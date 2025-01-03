# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SCENE_FILE_RELOCATE_METADATA = Metadata(
    id="4d5785c213ba8c43cc0d1cb433a896970dc23e80.boutiques",
    name="scene-file-relocate",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


class SceneFileRelocateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `scene_file_relocate(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def scene_file_relocate(
    input_scene: str,
    output_scene: str,
    runner: Runner | None = None,
) -> SceneFileRelocateOutputs:
    """
    Recreate scene file in new location.
    
    Scene files contain internal relative paths, such that moving or copying a
    scene file will cause it to lose track of the files it refers to. This
    command makes a modified copy of the scene file, changing the relative paths
    to refer to the new relative locations of the files.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        input_scene: the scene file to use.
        output_scene: output - the new scene file to create.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SceneFileRelocateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SCENE_FILE_RELOCATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-scene-file-relocate")
    cargs.append(input_scene)
    cargs.append(output_scene)
    ret = SceneFileRelocateOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SCENE_FILE_RELOCATE_METADATA",
    "SceneFileRelocateOutputs",
    "scene_file_relocate",
]
