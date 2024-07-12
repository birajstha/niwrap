# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

IMMV_METADATA = Metadata(
    id="95a9db3e6c7df5852f5123476e267e31308d183b",
    name="immv",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="docker/immv:latest",
)


class ImmvOutputs(typing.NamedTuple):
    """
    Output object returned when calling `immv(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def immv(
    source_files: list[InputPathType],
    destination: str,
    runner: Runner | None = None,
) -> ImmvOutputs:
    """
    immv by Unknown.
    
    Moves images from one file or directory to another.
    
    Args:
        source_files: Source files to be moved. Recognized file extensions:\
            .nii.gz, .nii, .img, .hdr, .img.gz, .hdr.gz.
        destination: Destination file or directory.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ImmvOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(IMMV_METADATA)
    cargs = []
    cargs.append("immv")
    cargs.extend([execution.input_file(f) for f in source_files])
    cargs.append(destination)
    ret = ImmvOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "IMMV_METADATA",
    "ImmvOutputs",
    "immv",
]
