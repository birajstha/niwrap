# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SIMPLE_SYN_REGISTRATION_METADATA = Metadata(
    id="8bdec8bc3a221887858c098adc61e63838dc3139.boutiques",
    name="simpleSynRegistration",
    package="ants",
    container_image_tag="antsx/ants:v2.5.3",
)


class SimpleSynRegistrationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `simple_syn_registration(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    registered_image: OutputPathType
    """The output registered image."""
    transform_matrix: OutputPathType
    """The output transformation matrix."""


def simple_syn_registration(
    fixed_image: InputPathType,
    moving_image: InputPathType,
    initial_transform: str,
    output_prefix: str,
    runner: Runner | None = None,
) -> SimpleSynRegistrationOutputs:
    """
    A simple SyN registration tool.
    
    Author: ANTs Developers
    
    URL: https://github.com/ANTsX/ANTs
    
    Args:
        fixed_image: The fixed image for registration.
        moving_image: The moving image to be registered.
        initial_transform: The initial transform for registration.
        output_prefix: Prefix for the output file name without any extension.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SimpleSynRegistrationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SIMPLE_SYN_REGISTRATION_METADATA)
    cargs = []
    cargs.append("simpleSynRegistration")
    cargs.append(execution.input_file(fixed_image) + ",")
    cargs.append(execution.input_file(moving_image) + ",")
    cargs.append(initial_transform + ",")
    cargs.append(output_prefix)
    ret = SimpleSynRegistrationOutputs(
        root=execution.output_file("."),
        registered_image=execution.output_file(output_prefix + "Registered.nii.gz"),
        transform_matrix=execution.output_file(output_prefix + "Transform.mat"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SIMPLE_SYN_REGISTRATION_METADATA",
    "SimpleSynRegistrationOutputs",
    "simple_syn_registration",
]
