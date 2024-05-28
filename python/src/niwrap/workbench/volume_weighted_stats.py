# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_WEIGHTED_STATS_METADATA = Metadata(
    id="f04254ac39eb8bffd17a0a1b7a021e67f4680557",
    name="volume-weighted-stats",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeWeightedStatsWeightVolume:
    """
    use weights from a volume file
    """
    opt_match_maps: bool = False
    """each subvolume of input uses the corresponding subvolume from the weights
    file"""
    
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


@dataclasses.dataclass
class VolumeWeightedStatsRoi:
    """
    only consider data inside an roi
    """
    opt_match_maps: bool = False
    """each subvolume of input uses the corresponding subvolume from the roi
    file"""
    
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


class VolumeWeightedStatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_weighted_stats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def volume_weighted_stats(
    volume_in: InputPathType,
    weight_volume: VolumeWeightedStatsWeightVolume | None = None,
    opt_subvolume_subvolume: str | None = None,
    roi: VolumeWeightedStatsRoi | None = None,
    opt_mean: bool = False,
    opt_stdev: bool = False,
    opt_sample: bool = False,
    opt_percentile_percent: float | int | None = None,
    opt_sum: bool = False,
    opt_show_map_name: bool = False,
    runner: Runner = None,
) -> VolumeWeightedStatsOutputs:
    """
    volume-weighted-stats by Washington University School of Medicin.
    
    Weighted spatial statistics on a volume file.
    
    For each subvolume of the input, a line of text is printed, resulting from
    the specified operation. If -weight-volume is not specified, each voxel's
    volume is used. Use -subvolume to only give output for a single subvolume.
    If the -roi option is used without -match-maps, then each line will contain
    as many numbers as there are maps in the ROI file, separated by tab
    characters. Exactly one of -mean, -stdev, -percentile or -sum must be
    specified.
    
    Using -sum without -weight-volume is equivalent to integrating with respect
    to volume.
    
    Args:
        volume_in: the input volume
        weight_volume: use weights from a volume file
        opt_subvolume_subvolume: only display output for one subvolume: the
            subvolume number or name
        roi: only consider data inside an roi
        opt_mean: compute weighted mean
        opt_stdev: compute weighted standard deviation
        opt_sample: estimate population stdev from the sample
        opt_percentile_percent: compute weighted percentile: the percentile to
            find, must be between 0 and 100
        opt_sum: compute weighted sum
        opt_show_map_name: print map index and name before each output
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeWeightedStatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_WEIGHTED_STATS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-weighted-stats")
    cargs.append(execution.input_file(volume_in))
    if weight_volume is not None:
        cargs.extend(["-weight-volume", *weight_volume.run(execution)])
    if opt_subvolume_subvolume is not None:
        cargs.extend(["-subvolume", opt_subvolume_subvolume])
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
    ret = VolumeWeightedStatsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_WEIGHTED_STATS_METADATA",
    "VolumeWeightedStatsOutputs",
    "VolumeWeightedStatsRoi",
    "VolumeWeightedStatsWeightVolume",
    "volume_weighted_stats",
]
