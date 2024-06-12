# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SYSTEMNOISE_METADATA = Metadata(
    id="912d0213fe2927098265fb0d8c25a1bae5ff42df",
    name="systemnoise",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class SystemnoiseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `systemnoise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_signal_file: OutputPathType
    """Output signal with added system noise"""


def systemnoise(
    input_signal: InputPathType,
    output_signal: InputPathType,
    noise_standard_deviation: float | int,
    seed: float | int | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner = None,
) -> SystemnoiseOutputs:
    """
    systemnoise by University of Oxford (Mark Jenkinson).
    
    Tool for adding system noise to a given signal using FSL's utilities.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/SystemNoise
    
    Args:
        input_signal: Input signal (possum output matrix).
        output_signal: Output signal (possum matrix form).
        noise_standard_deviation: Set noise standard deviation (units of\
            intensity).
        seed: Input seed value for the sequence.
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display help message.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SystemnoiseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SYSTEMNOISE_METADATA)
    cargs = []
    cargs.append("systemnoise")
    cargs.append("[OPTIONS]")
    ret = SystemnoiseOutputs(
        root=execution.output_file("."),
        output_signal_file=execution.output_file(f"{pathlib.Path(output_signal).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SYSTEMNOISE_METADATA",
    "SystemnoiseOutputs",
    "systemnoise",
]
