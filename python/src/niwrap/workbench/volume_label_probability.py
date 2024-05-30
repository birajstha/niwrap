# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


VOLUME_LABEL_PROBABILITY_METADATA = Metadata(
    id="87d1563a8c992e3b4e82b3c5ba411e45fb0c806a",
    name="volume-label-probability",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class VolumeLabelProbabilityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_label_probability(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    probability_out: OutputPathType
    """the relative frequencies of each label at each voxel"""


def volume_label_probability(
    label_maps: InputPathType,
    probability_out: InputPathType,
    opt_exclude_unlabeled: bool = False,
    runner: Runner = None,
) -> VolumeLabelProbabilityOutputs:
    """
    volume-label-probability by Washington University School of Medicin.
    
    Find frequency of volume labels.
    
    This command outputs a set of soft ROIs, one for each label in the input,
    where the value is how many of the input maps had that label at that voxel,
    divided by the number of input maps.
    
    Args:
        label_maps: volume label file containing individual label maps from many
            subjects
        probability_out: the relative frequencies of each label at each voxel
        opt_exclude_unlabeled: don't make a probability map of the unlabeled key
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeLabelProbabilityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_LABEL_PROBABILITY_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-label-probability")
    cargs.append(execution.input_file(label_maps))
    cargs.append(execution.input_file(probability_out))
    if opt_exclude_unlabeled:
        cargs.append("-exclude-unlabeled")
    ret = VolumeLabelProbabilityOutputs(
        root=execution.output_file("."),
        probability_out=execution.output_file(f"{pathlib.Path(probability_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_LABEL_PROBABILITY_METADATA",
    "VolumeLabelProbabilityOutputs",
    "volume_label_probability",
]
