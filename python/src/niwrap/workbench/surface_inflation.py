# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_INFLATION_METADATA = Metadata(
    id="9e8a090010468eb1b4a1ab2178e5a3d720f41c8a",
    name="surface-inflation",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceInflationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_inflation(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """output surface file"""


def surface_inflation(
    anatomical_surface_in: InputPathType,
    surface_in: InputPathType,
    number_of_smoothing_cycles: int,
    smoothing_strength: float | int,
    smoothing_iterations: int,
    inflation_factor: float | int,
    surface_out: InputPathType,
    runner: Runner = None,
) -> SurfaceInflationOutputs:
    """
    surface-inflation by Washington University School of Medicin.
    
    Surface inflation.
    
    Inflate a surface by performing cycles that consist of smoothing followed by
    inflation (to correct shrinkage caused by smoothing).
    
    Args:
        anatomical_surface_in: the anatomical surface.
        surface_in: the surface file to inflate.
        number_of_smoothing_cycles: number of smoothing cycles.
        smoothing_strength: smoothing strength (ranges [0.0 - 1.0]).
        smoothing_iterations: smoothing iterations.
        inflation_factor: inflation factor.
        surface_out: output surface file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceInflationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_INFLATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-inflation")
    cargs.append(execution.input_file(anatomical_surface_in))
    cargs.append(execution.input_file(surface_in))
    cargs.append(str(number_of_smoothing_cycles))
    cargs.append(str(smoothing_strength))
    cargs.append(str(smoothing_iterations))
    cargs.append(str(inflation_factor))
    cargs.append(execution.input_file(surface_out))
    ret = SurfaceInflationOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_INFLATION_METADATA",
    "SurfaceInflationOutputs",
    "surface_inflation",
]
