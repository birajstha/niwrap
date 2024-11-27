# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_CLUST_SIM_METADATA = Metadata(
    id="493de4c7d1501714af71d386a011e1fe097ca5fb.boutiques",
    name="3dClustSim",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dClustSimOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_clust_sim(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_nn1_1sided: OutputPathType
    """Output file for NN1 with 1-sided thresholding"""
    output_nn1_2sided: OutputPathType
    """Output file for NN1 with 2-sided thresholding"""
    output_nn1_bisided: OutputPathType
    """Output file for NN1 with bi-sided thresholding"""
    output_nn2_1sided: OutputPathType
    """Output file for NN2 with 1-sided thresholding"""
    output_nn2_2sided: OutputPathType
    """Output file for NN2 with 2-sided thresholding"""
    output_nn2_bisided: OutputPathType
    """Output file for NN2 with bi-sided thresholding"""
    output_nn3_1sided: OutputPathType
    """Output file for NN3 with 1-sided thresholding"""
    output_nn3_2sided: OutputPathType
    """Output file for NN3 with 2-sided thresholding"""
    output_nn3_bisided: OutputPathType
    """Output file for NN3 with bi-sided thresholding"""
    mask_compressed: OutputPathType
    """Compressed ASCII encoding of the mask volume"""


def v_3d_clust_sim(
    runner: Runner | None = None,
) -> V3dClustSimOutputs:
    """
    Program to estimate the probability of false positive (noise-only) clusters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dClustSimOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_CLUST_SIM_METADATA)
    cargs = []
    cargs.append("3dClustSim")
    cargs.append("[OPTIONS]")
    ret = V3dClustSimOutputs(
        root=execution.output_file("."),
        output_nn1_1sided=execution.output_file("[PREFIX].NN1_1sided.1D"),
        output_nn1_2sided=execution.output_file("[PREFIX].NN1_2sided.1D"),
        output_nn1_bisided=execution.output_file("[PREFIX].NN1_bisided.1D"),
        output_nn2_1sided=execution.output_file("[PREFIX].NN2_1sided.1D"),
        output_nn2_2sided=execution.output_file("[PREFIX].NN2_2sided.1D"),
        output_nn2_bisided=execution.output_file("[PREFIX].NN2_bisided.1D"),
        output_nn3_1sided=execution.output_file("[PREFIX].NN3_1sided.1D"),
        output_nn3_2sided=execution.output_file("[PREFIX].NN3_2sided.1D"),
        output_nn3_bisided=execution.output_file("[PREFIX].NN3_bisided.1D"),
        mask_compressed=execution.output_file("[PREFIX].mask"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dClustSimOutputs",
    "V_3D_CLUST_SIM_METADATA",
    "v_3d_clust_sim",
]
