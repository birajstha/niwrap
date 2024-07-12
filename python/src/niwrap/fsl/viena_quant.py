# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

VIENA_QUANT_METADATA = Metadata(
    id="b972f833d89f8dcbaabd9d992553bdd05813b35a",
    name="viena_quant",
)


class VienaQuantOutputs(typing.NamedTuple):
    """
    Output object returned when calling `viena_quant(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_quantification: OutputPathType
    """Output quantification result"""


def viena_quant(
    input1: InputPathType,
    input2: InputPathType,
    ventricle_mask: InputPathType,
    runner: Runner | None = None,
) -> VienaQuantOutputs:
    """
    viena_quant by Unknown.
    
    Automated brain ventricle quantification tool.
    
    Args:
        input1: Input image 1 (e.g. img1.nii.gz).
        input2: Input image 2 (e.g. img2.nii.gz).
        ventricle_mask: Ventricle mask (e.g. mask.nii.gz).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VienaQuantOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VIENA_QUANT_METADATA)
    cargs = []
    cargs.append("viena_quant")
    cargs.append(execution.input_file(input1))
    cargs.append(execution.input_file(input2))
    cargs.append(execution.input_file(ventricle_mask))
    ret = VienaQuantOutputs(
        root=execution.output_file("."),
        output_quantification=execution.output_file(f"output_quantification.nii.gz", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VIENA_QUANT_METADATA",
    "VienaQuantOutputs",
    "viena_quant",
]
