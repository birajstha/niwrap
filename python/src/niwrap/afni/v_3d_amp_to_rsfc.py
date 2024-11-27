# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_AMP_TO_RSFC_METADATA = Metadata(
    id="27e3a8435ad8a4458d62e5fc746c88a2665d19fa.boutiques",
    name="3dAmpToRSFC",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dAmpToRsfcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_amp_to_rsfc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_alff: OutputPathType
    """Amplitude of low frequency fluctuations (L1 sum)."""
    output_malff: OutputPathType
    """ALFF divided by the mean value within the input/estimated whole brain
    mask (mean-scaled ALFF)."""
    output_falff: OutputPathType
    """ALFF divided by sum of full amplitude spectrum (fractional ALFF)."""
    output_rsfa: OutputPathType
    """Square-root of summed square of low frequency fluctuations (L2 sum)."""
    output_mrsfa: OutputPathType
    """RSFA divided by the mean value within the input/estimated whole brain
    mask (mean-scaled RSFA)."""
    output_frsfa: OutputPathType
    """ALFF divided by sum of full amplitude spectrum (fractional RSFA)."""


def v_3d_amp_to_rsfc(
    prefix: str,
    band: list[float],
    in_amp: InputPathType | None = None,
    in_pow: InputPathType | None = None,
    mask: InputPathType | None = None,
    runner: Runner | None = None,
) -> V3dAmpToRsfcOutputs:
    """
    Convert spectral amplitudes into standard RSFC parameters.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        prefix: Output file prefix; file names will be: PREFIX_ALFF,\
            PREFIX_FALFF, etc.
        band: Lower and upper boundaries of the low frequency fluctuations\
            (LFFs), within the interval [FBOT, FTOP].
        in_amp: Input file of one-sided spectral amplitudes, such as output by\
            3dLombScargle.
        in_pow: Input file of a one-sided power spectrum, such as output by\
            3dLombScargle.
        mask: Volume mask of voxels to include for calculations.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAmpToRsfcOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AMP_TO_RSFC_METADATA)
    cargs = []
    cargs.append("3dAmpToRSFC")
    cargs.append("{")
    if in_amp is not None:
        cargs.extend([
            "-in_amp",
            execution.input_file(in_amp)
        ])
    cargs.append("|")
    if in_pow is not None:
        cargs.extend([
            "-in_pow",
            execution.input_file(in_pow)
        ])
    cargs.append("}")
    cargs.extend([
        "-prefix",
        prefix
    ])
    cargs.extend([
        "-band",
        *map(str, band)
    ])
    cargs.append("{")
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    cargs.append("}")
    cargs.append("{")
    cargs.append("-nifti")
    cargs.append("}")
    ret = V3dAmpToRsfcOutputs(
        root=execution.output_file("."),
        output_alff=execution.output_file(prefix + "_ALFF*"),
        output_malff=execution.output_file(prefix + "_MALFF*"),
        output_falff=execution.output_file(prefix + "_FALFF*"),
        output_rsfa=execution.output_file(prefix + "_RSFA*"),
        output_mrsfa=execution.output_file(prefix + "_MRSFA*"),
        output_frsfa=execution.output_file(prefix + "_FRSFA*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAmpToRsfcOutputs",
    "V_3D_AMP_TO_RSFC_METADATA",
    "v_3d_amp_to_rsfc",
]
