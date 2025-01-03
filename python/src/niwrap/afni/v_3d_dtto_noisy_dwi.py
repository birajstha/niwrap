# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V_3D_DTTO_NOISY_DWI_METADATA = Metadata(
    id="0ef5fe03a8b952b27e737adb59a395ac94790601.boutiques",
    name="3dDTtoNoisyDWI",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class V3dDttoNoisyDwiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_dtto_noisy_dwi(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_dwi: OutputPathType
    """Synthetic set of DWI measures with noise. Contains N+1 bricks mimicking
    B0+DWI data."""


def v_3d_dtto_noisy_dwi(
    dt_file: InputPathType,
    grad_file: InputPathType,
    noise_dwi: float,
    prefix: str,
    noise_b0: float | None = None,
    mask: InputPathType | None = None,
    bval: float | None = None,
    s0: float | None = None,
    runner: Runner | None = None,
) -> V3dDttoNoisyDwiOutputs:
    """
    Generate a synthetic set of DWI measures with a given SNR from an AFNI-style DT
    file and a set of gradients. This can be useful for simulations and testing.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        dt_file: Diffusion tensor file with six bricks of DT components ordered\
            in the AFNI manner: Dxx,Dxy,Dyy,Dxz,Dyz,Dzz.
        grad_file: Text file of gradients arranged in three columns. There\
            should be no row of all zeros representing the b=0 line.
        noise_dwi: Fractional value of noise in DWIs. FF = sigma/S0 = 1/SNR0.\
            For example, FF=0.05 corresponds to SNR0=20.
        prefix: Output file name prefix. Will have N+1 bricks when GRADFILE has\
            N rows of gradients.
        noise_b0: Optional fraction of Rician noise in the b=0 reference image.\
            If not provided, FF2=FF.
        mask: Optional mask within which to calculate uncertainty. Data should\
            be masked already otherwise.
        bval: Optional DW factor to use if DT values are scaled to something\
            physical. Default is BB=1.
        s0: Optional reference b=0 signal strength. Default value is SS=1000.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dDttoNoisyDwiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_DTTO_NOISY_DWI_METADATA)
    cargs = []
    cargs.append("3dDTtoNoisyDWI")
    cargs.append(execution.input_file(dt_file))
    cargs.append(execution.input_file(grad_file))
    cargs.extend([
        "-noise_DWI",
        str(noise_dwi)
    ])
    if noise_b0 is not None:
        cargs.extend([
            "-noise_B0",
            str(noise_b0)
        ])
    cargs.extend([
        "-prefix",
        prefix
    ])
    if mask is not None:
        cargs.extend([
            "-mask",
            execution.input_file(mask)
        ])
    if bval is not None:
        cargs.extend([
            "-bval",
            str(bval)
        ])
    if s0 is not None:
        cargs.extend([
            "-S0",
            str(s0)
        ])
    ret = V3dDttoNoisyDwiOutputs(
        root=execution.output_file("."),
        output_dwi=execution.output_file(prefix + "+orig"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dDttoNoisyDwiOutputs",
    "V_3D_DTTO_NOISY_DWI_METADATA",
    "v_3d_dtto_noisy_dwi",
]
