# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_RSFC_METADATA = Metadata(
    id="f1d35055279f0d50637821729455f8aecddf55a2",
    name="3dRSFC",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dRsfcOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_rsfc(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    filtered_time_series: OutputPathType | None
    """Filtered time series output"""
    un_bandpassed_series: OutputPathType | None
    """Un-bandpassed series output"""


def v_3d_rsfc(
    input_dataset: InputPathType,
    fbot: float | int,
    ftop: float | int,
    despike: bool = False,
    ort_file: InputPathType | None = None,
    dsort_file: InputPathType | None = None,
    nodetrend: bool = False,
    time_step: float | int | None = None,
    nfft: int | None = None,
    norm: bool = False,
    mask: InputPathType | None = None,
    automask: bool = False,
    blur: float | int | None = None,
    localpv: float | int | None = None,
    input_alt: InputPathType | None = None,
    band: list[float | int] | None = None,
    prefix: str | None = None,
    quiet: bool = False,
    no_rs_out: bool = False,
    un_bandpass_out: bool = False,
    no_rsfa: bool = False,
    bp_at_end: bool = False,
    notrans: bool = False,
    nosat: bool = False,
    runner: Runner | None = None,
) -> V3dRsfcOutputs:
    """
    3dRSFC by AFNI Team.
    
    Program to calculate common resting state functional connectivity (RSFC)
    parameters.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dRSFC.html
    
    Args:
        input_dataset: Input dataset (3D+time sequence of volumes).
        fbot: Lowest frequency in the passband, in Hz.
        ftop: Highest frequency in the passband (must be > fbot).
        despike: Despike each time series before other processing.
        ort_file: Also orthogonalize input to columns in specified file.
        dsort_file: Orthogonalize each voxel to the corresponding voxel time\
            series in specified dataset.
        nodetrend: Skip the quadratic detrending of input before FFT-based\
            bandpassing.
        time_step: Set time step to specified value in seconds.
        nfft: Set the FFT length to specified value.
        norm: Make all output time series have L2 norm = 1.
        mask: Specify mask dataset.
        automask: Create a mask from the input dataset.
        blur: Blur inside the mask only with specified FWHM in mm.
        localpv: Replace each vector by the local Principal Vector from a\
            neighborhood radius.
        input_alt: Alternative way to specify input dataset.
        band: Alternative way to specify passband frequencies.
        prefix: Set prefix name of the output dataset.
        quiet: Turn off the fun and informative messages.
        no_rs_out: Don't output processed time series, just output parameters.
        un_bandpass_out: Output the un-bandpassed series as well.
        no_rsfa: Exclude RSFA output (default is to include).
        bp_at_end: Bandpassing as the last step in the processing sequence.
        notrans: Don't check for initial positive transients in the data.
        nosat: Equivalent to -notrans, skips checking for initial transients.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dRsfcOutputs`).
    """
    runner = runner or get_global_runner()
    if band is not None and (len(band) != 2): 
        raise ValueError(f"Length of 'band' must be 2 but was {len(band)}")
    execution = runner.start_execution(V_3D_RSFC_METADATA)
    cargs = []
    cargs.append("3dRSFC")
    cargs.append("[OPTIONS]")
    cargs.append(str(fbot))
    cargs.append(str(ftop))
    cargs.append(execution.input_file(input_dataset))
    ret = V3dRsfcOutputs(
        root=execution.output_file("."),
        filtered_time_series=execution.output_file(f"{prefix}_LFF+orig.*", optional=True) if prefix is not None else None,
        un_bandpassed_series=execution.output_file(f"{prefix}_unBP+orig.*", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dRsfcOutputs",
    "V_3D_RSFC_METADATA",
    "v_3d_rsfc",
]
