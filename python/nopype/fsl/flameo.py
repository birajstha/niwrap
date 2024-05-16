# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.015750

import typing

from ..styxdefs import *


FLAMEO_METADATA = Metadata(
    id="429b46b8ae14b00327226a7334c2739f00079390",
    name="FLAMEO",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FlameoOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flameo(...)`.
    """
    dummy_output: OutputPathType
    """Description missing"""


def flameo(
    runner: Runner,
    dummy_input: InputPathType,
) -> FlameoOutputs:
    """
    FLAMEO, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    FLAMEO). Automatic nipype2boutiques conversion failed.
    
    Args:
        runner: Command runner
        dummy_input: Description missing
    Returns:
        NamedTuple of outputs (described in `FlameoOutputs`).
    """
    execution = runner.start_execution(FLAMEO_METADATA)
    cargs = []
    cargs.append("dummy")
    ret = FlameoOutputs(
        dummy_output=execution.output_file(f"dummy_output.txt"),
    )
    execution.run(cargs)
    return ret