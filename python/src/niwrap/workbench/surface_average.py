# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

SURFACE_AVERAGE_METADATA = Metadata(
    id="98f438cc476f86c25766a0eba51a0fc2105a5bcf",
    name="surface-average",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class SurfaceAverageSurf:
    """
    specify a surface to include in the average
    """
    opt_weight_weight: float | int | None = None
    """specify a weighted average: the weight to use (default 1)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_weight_weight is not None:
            cargs.extend(["-weight", str(self.opt_weight_weight)])
        return cargs


class SurfaceAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output averaged surface"""
    stddev_metric_out: OutputPathType
    """the output metric for 3D sample standard deviation"""
    uncert_metric_out: OutputPathType
    """the output metric for uncertainty"""


def surface_average(
    surface_out: InputPathType,
    stddev_metric_out: InputPathType,
    uncert_metric_out: InputPathType,
    opt_stddev: bool = False,
    opt_uncertainty: bool = False,
    surf: list[SurfaceAverageSurf] = None,
    runner: Runner = None,
) -> SurfaceAverageOutputs:
    """
    surface-average by Washington University School of Medicin.
    
    Average surface files together.
    
    The 3D sample standard deviation is computed as 'sqrt(sum(squaredlength(xyz
    - mean(xyz)))/(n - 1))'.
    
    Uncertainty is a legacy measure used in caret5, and is computed as
    'sum(length(xyz - mean(xyz)))/n'.
    
    When weights are used, the 3D sample standard deviation treats them as
    reliability weights.
    
    Args:
        surface_out: the output averaged surface.
        stddev_metric_out: the output metric for 3D sample standard deviation.
        uncert_metric_out: the output metric for uncertainty.
        opt_stddev: compute 3D sample standard deviation.
        opt_uncertainty: compute caret5 'uncertainty'.
        surf: specify a surface to include in the average.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceAverageOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_AVERAGE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-surface-average")
    cargs.append(execution.input_file(surface_out))
    if opt_stddev:
        cargs.append("-stddev")
    cargs.append(execution.input_file(stddev_metric_out))
    if opt_uncertainty:
        cargs.append("-uncertainty")
    cargs.append(execution.input_file(uncert_metric_out))
    if surf is not None:
        cargs.extend(["-surf", *[a for c in [s.run(execution) for s in surf] for a in c]])
    ret = SurfaceAverageOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(f"{pathlib.Path(surface_out).name}"),
        stddev_metric_out=execution.output_file(f"{pathlib.Path(stddev_metric_out).name}"),
        uncert_metric_out=execution.output_file(f"{pathlib.Path(uncert_metric_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_AVERAGE_METADATA",
    "SurfaceAverageOutputs",
    "SurfaceAverageSurf",
    "surface_average",
]
