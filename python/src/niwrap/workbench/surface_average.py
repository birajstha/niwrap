# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

SURFACE_AVERAGE_METADATA = Metadata(
    id="0b0af137beb4ea2cc6bc28495313dc2db434da59.boutiques",
    name="surface-average",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class SurfaceAverageSurf:
    """
    specify a surface to include in the average.
    """
    surface: InputPathType
    """a surface file to average"""
    opt_weight_weight: float | None = None
    """specify a weighted average: the weight to use (default 1)"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-surf")
        cargs.append(execution.input_file(self.surface))
        if self.opt_weight_weight is not None:
            cargs.extend([
                "-weight",
                str(self.opt_weight_weight)
            ])
        return cargs


class SurfaceAverageOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_average(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    surface_out: OutputPathType
    """the output averaged surface"""
    opt_stddev_stddev_metric_out: OutputPathType | None
    """compute 3D sample standard deviation: the output metric for 3D sample
    standard deviation"""
    opt_uncertainty_uncert_metric_out: OutputPathType | None
    """compute caret5 'uncertainty': the output metric for uncertainty"""


def surface_average(
    surface_out: str,
    opt_stddev_stddev_metric_out: str | None = None,
    opt_uncertainty_uncert_metric_out: str | None = None,
    surf: list[SurfaceAverageSurf] | None = None,
    runner: Runner | None = None,
) -> SurfaceAverageOutputs:
    """
    Average surface files together.
    
    The 3D sample standard deviation is computed as 'sqrt(sum(squaredlength(xyz
    - mean(xyz)))/(n - 1))'.
    
    Uncertainty is a legacy measure used in caret5, and is computed as
    'sum(length(xyz - mean(xyz)))/n'.
    
    When weights are used, the 3D sample standard deviation treats them as
    reliability weights.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        surface_out: the output averaged surface.
        opt_stddev_stddev_metric_out: compute 3D sample standard deviation: the\
            output metric for 3D sample standard deviation.
        opt_uncertainty_uncert_metric_out: compute caret5 'uncertainty': the\
            output metric for uncertainty.
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
    cargs.append(surface_out)
    if opt_stddev_stddev_metric_out is not None:
        cargs.extend([
            "-stddev",
            opt_stddev_stddev_metric_out
        ])
    if opt_uncertainty_uncert_metric_out is not None:
        cargs.extend([
            "-uncertainty",
            opt_uncertainty_uncert_metric_out
        ])
    if surf is not None:
        cargs.extend([a for c in [s.run(execution) for s in surf] for a in c])
    ret = SurfaceAverageOutputs(
        root=execution.output_file("."),
        surface_out=execution.output_file(surface_out),
        opt_stddev_stddev_metric_out=execution.output_file(opt_stddev_stddev_metric_out) if (opt_stddev_stddev_metric_out is not None) else None,
        opt_uncertainty_uncert_metric_out=execution.output_file(opt_uncertainty_uncert_metric_out) if (opt_uncertainty_uncert_metric_out is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_AVERAGE_METADATA",
    "SurfaceAverageOutputs",
    "SurfaceAverageSurf",
    "surface_average",
]
