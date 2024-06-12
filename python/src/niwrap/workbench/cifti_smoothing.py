# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_SMOOTHING_METADATA = Metadata(
    id="e9c0a2ff8012537c4f49bb87706f90fd9c99c586",
    name="cifti-smoothing",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiSmoothingLeftSurface:
    """
    specify the left surface to use
    """
    opt_left_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the left surface: the
    corrected vertex areas, as a metric"""
    
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
        if self.opt_left_corrected_areas_area_metric is not None:
            cargs.extend(["-left-corrected-areas", execution.input_file(self.opt_left_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiSmoothingRightSurface:
    """
    specify the right surface to use
    """
    opt_right_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the right surface: the
    corrected vertex areas, as a metric"""
    
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
        if self.opt_right_corrected_areas_area_metric is not None:
            cargs.extend(["-right-corrected-areas", execution.input_file(self.opt_right_corrected_areas_area_metric)])
        return cargs


@dataclasses.dataclass
class CiftiSmoothingCerebellumSurface:
    """
    specify the cerebellum surface to use
    """
    opt_cerebellum_corrected_areas_area_metric: InputPathType | None = None
    """vertex areas to use instead of computing them from the cerebellum
    surface: the corrected vertex areas, as a metric"""
    
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
        if self.opt_cerebellum_corrected_areas_area_metric is not None:
            cargs.extend(["-cerebellum-corrected-areas", execution.input_file(self.opt_cerebellum_corrected_areas_area_metric)])
        return cargs


class CiftiSmoothingOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_smoothing(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti"""


def cifti_smoothing(
    cifti: InputPathType,
    surface_kernel: float | int,
    volume_kernel: float | int,
    direction: str,
    cifti_out: InputPathType,
    opt_fwhm: bool = False,
    left_surface: CiftiSmoothingLeftSurface | None = None,
    right_surface: CiftiSmoothingRightSurface | None = None,
    cerebellum_surface: CiftiSmoothingCerebellumSurface | None = None,
    opt_cifti_roi_roi_cifti: InputPathType | None = None,
    opt_fix_zeros_volume: bool = False,
    opt_fix_zeros_surface: bool = False,
    opt_merged_volume: bool = False,
    runner: Runner = None,
) -> CiftiSmoothingOutputs:
    """
    cifti-smoothing by Washington University School of Medicin.
    
    Smooth a cifti file.
    
    The input cifti file must have a brain models mapping on the chosen
    dimension, columns for .dtseries, and either for .dconn. By default, data in
    different structures is smoothed independently (i.e., "parcel constrained"
    smoothing), so volume structures that touch do not smooth across this
    boundary. Specify -merged-volume to ignore these boundaries. Surface
    smoothing uses the GEO_GAUSS_AREA smoothing method.
    
    The -*-corrected-areas options are intended for when it is unavoidable to
    smooth on group average surfaces, it is only an approximate correction for
    the reduction of structure in a group average surface. It is better to
    smooth the data on individuals before averaging, when feasible.
    
    The -fix-zeros-* options will treat values of zero as lack of data, and not
    use that value when generating the smoothed values, but will fill zeros with
    extrapolated values. The ROI should have a brain models mapping along
    columns, exactly matching the mapping of the chosen direction in the input
    file. Data outside the ROI is ignored.
    
    Args:
        cifti: the input cifti.
        surface_kernel: the size of the gaussian surface smoothing kernel in\
            mm, as sigma by default.
        volume_kernel: the size of the gaussian volume smoothing kernel in mm,\
            as sigma by default.
        direction: which dimension to smooth along, ROW or COLUMN.
        cifti_out: the output cifti.
        opt_fwhm: kernel sizes are FWHM, not sigma.
        left_surface: specify the left surface to use.
        right_surface: specify the right surface to use.
        cerebellum_surface: specify the cerebellum surface to use.
        opt_cifti_roi_roi_cifti: smooth only within regions of interest: the\
            regions to smooth within, as a cifti file.
        opt_fix_zeros_volume: treat values of zero in the volume as missing\
            data.
        opt_fix_zeros_surface: treat values of zero on the surface as missing\
            data.
        opt_merged_volume: smooth across subcortical structure boundaries.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiSmoothingOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_SMOOTHING_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-smoothing")
    cargs.append(execution.input_file(cifti))
    cargs.append(str(surface_kernel))
    cargs.append(str(volume_kernel))
    cargs.append(direction)
    cargs.append(execution.input_file(cifti_out))
    if opt_fwhm:
        cargs.append("-fwhm")
    if left_surface is not None:
        cargs.extend(["-left-surface", *left_surface.run(execution)])
    if right_surface is not None:
        cargs.extend(["-right-surface", *right_surface.run(execution)])
    if cerebellum_surface is not None:
        cargs.extend(["-cerebellum-surface", *cerebellum_surface.run(execution)])
    if opt_cifti_roi_roi_cifti is not None:
        cargs.extend(["-cifti-roi", execution.input_file(opt_cifti_roi_roi_cifti)])
    if opt_fix_zeros_volume:
        cargs.append("-fix-zeros-volume")
    if opt_fix_zeros_surface:
        cargs.append("-fix-zeros-surface")
    if opt_merged_volume:
        cargs.append("-merged-volume")
    ret = CiftiSmoothingOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{pathlib.Path(cifti_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_SMOOTHING_METADATA",
    "CiftiSmoothingCerebellumSurface",
    "CiftiSmoothingLeftSurface",
    "CiftiSmoothingOutputs",
    "CiftiSmoothingRightSurface",
    "cifti_smoothing",
]
