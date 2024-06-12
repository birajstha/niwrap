# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_WEIGHTED_STATS_METADATA = Metadata(
    id="3d08a8eec40bec1f0dd1101875830affda36510b",
    name="cifti-weighted-stats",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiWeightedStatsSpatialWeights:
    """
    use vertex area and voxel volume as weights
    """
    opt_left_area_surf_left_surf: InputPathType | None = None
    """use a surface for left vertex areas: the left surface to use, areas are
    in mm^2"""
    opt_right_area_surf_right_surf: InputPathType | None = None
    """use a surface for right vertex areas: the right surface to use, areas are
    in mm^2"""
    opt_cerebellum_area_surf_cerebellum_surf: InputPathType | None = None
    """use a surface for cerebellum vertex areas: the cerebellum surface to use,
    areas are in mm^2"""
    opt_left_area_metric_left_metric: InputPathType | None = None
    """use a metric file for left vertex areas: metric file containing left
    vertex areas"""
    opt_right_area_metric_right_metric: InputPathType | None = None
    """use a metric file for right vertex areas: metric file containing right
    vertex areas"""
    opt_cerebellum_area_metric_cerebellum_metric: InputPathType | None = None
    """use a metric file for cerebellum vertex areas: metric file containing
    cerebellum vertex areas"""
    
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
        if self.opt_left_area_surf_left_surf is not None:
            cargs.extend(["-left-area-surf", execution.input_file(self.opt_left_area_surf_left_surf)])
        if self.opt_right_area_surf_right_surf is not None:
            cargs.extend(["-right-area-surf", execution.input_file(self.opt_right_area_surf_right_surf)])
        if self.opt_cerebellum_area_surf_cerebellum_surf is not None:
            cargs.extend(["-cerebellum-area-surf", execution.input_file(self.opt_cerebellum_area_surf_cerebellum_surf)])
        if self.opt_left_area_metric_left_metric is not None:
            cargs.extend(["-left-area-metric", execution.input_file(self.opt_left_area_metric_left_metric)])
        if self.opt_right_area_metric_right_metric is not None:
            cargs.extend(["-right-area-metric", execution.input_file(self.opt_right_area_metric_right_metric)])
        if self.opt_cerebellum_area_metric_cerebellum_metric is not None:
            cargs.extend(["-cerebellum-area-metric", execution.input_file(self.opt_cerebellum_area_metric_cerebellum_metric)])
        return cargs


@dataclasses.dataclass
class CiftiWeightedStatsRoi:
    """
    only consider data inside an roi
    """
    opt_match_maps: bool = False
    """each column of input uses the corresponding column from the roi file"""
    
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
        if self.opt_match_maps:
            cargs.append("-match-maps")
        return cargs


class CiftiWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_weighted_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_weighted_stats(
    cifti_in: InputPathType,
    spatial_weights: CiftiWeightedStatsSpatialWeights | None = None,
    opt_cifti_weights_weight_cifti: InputPathType | None = None,
    opt_column_column: int | None = None,
    roi: CiftiWeightedStatsRoi | None = None,
    opt_mean: bool = False,
    opt_stdev: bool = False,
    opt_sample: bool = False,
    opt_percentile_percent: float | int | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
    runner: Runner = None,
) -> CiftiWeightedStatsOutputs:
    """
    cifti-weighted-stats by Washington University School of Medicin.
    
    Weighted statistics along cifti columns.
    
    If the mapping along column is brain models, for each column of the input,
    the specified operation is done on each surface and across all voxels, and
    the results are printed on separate lines. For other mapping types, the
    operation is done on each column, and one line per map is printed. Exactly
    one of -spatial-weights or -cifti-weights must be specified. Use -column to
    only give output for a single column. If the -roi option is used without
    -match-maps, then each line will contain as many numbers as there are maps
    in the ROI file, separated by tab characters. Exactly one of -mean, -stdev,
    -percentile or -sum must be specified.
    
    Using -sum with -spatial-weights (or with -cifti-weights and a cifti
    containing weights of similar meaning) is equivalent to integrating with
    respect to area and volume. When the input is binary ROIs, this will
    therefore output the area or volume of each ROI.
    
    Args:
        cifti_in: the input cifti.
        spatial_weights: use vertex area and voxel volume as weights.
        opt_cifti_weights_weight_cifti: use a cifti file containing weights:\
            the weights to use, as a cifti file.
        opt_column_column: only display output for one column: the column to\
            use (1-based).
        roi: only consider data inside an roi.
        opt_mean: compute weighted mean.
        opt_stdev: compute weighted standard deviation.
        opt_sample: estimate population stdev from the sample.
        opt_percentile_percent: compute weighted percentile: the percentile to\
            find, must be between 0 and 100.
        opt_sum: compute weighted sum.
        opt_show_map_name: print map index and name before each output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiWeightedStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_WEIGHTED_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-weighted-stats")
    cargs.append(execution.input_file(cifti_in))
    if spatial_weights is not None:
        cargs.extend(["-spatial-weights", *spatial_weights.run(execution)])
    if opt_cifti_weights_weight_cifti is not None:
        cargs.extend(["-cifti-weights", execution.input_file(opt_cifti_weights_weight_cifti)])
    if opt_column_column is not None:
        cargs.extend(["-column", str(opt_column_column)])
    if roi is not None:
        cargs.extend(["-roi", *roi.run(execution)])
    if opt_mean:
        cargs.append("-mean")
    if opt_stdev:
        cargs.append("-stdev")
    if opt_sample:
        cargs.append("-sample")
    if opt_percentile_percent is not None:
        cargs.extend(["-percentile", str(opt_percentile_percent)])
    if opt_sum:
        cargs.append("-sum")
    if opt_show_map_name:
        cargs.append("-show-map-name")
    ret = CiftiWeightedStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_WEIGHTED_STATS_METADATA",
    "CiftiWeightedStatsOutputs",
    "CiftiWeightedStatsRoi",
    "CiftiWeightedStatsSpatialWeights",
    "cifti_weighted_stats",
]
