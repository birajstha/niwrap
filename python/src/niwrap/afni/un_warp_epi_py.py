# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

UN_WARP_EPI_PY_METADATA = Metadata(
    id="e4fd23a18bcd39d85c3ce820bf2ec1cc6ba41ead",
    name="unWarpEPI.py",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class UnWarpEpiPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `un_warp_epi_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def un_warp_epi_py(
    forward: InputPathType,
    reverse: InputPathType,
    anat4warp: InputPathType,
    data: str,
    subj_id: str,
    giant_move: bool = False,
    runner: Runner | None = None,
) -> UnWarpEpiPyOutputs:
    """
    unWarpEPI.py by AFNI Team.
    
    Routine to unwarp EPI data set using another data set with opposite
    polarity.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/unWarpEPI.py.html
    
    Args:
        forward: Calibration matching data to be corrected.
        reverse: Calibration with opposing polarity to data to be corrected.
        anat4warp: Reference anatomical dataset.
        data: Data to be corrected (same polarity as forward calibration data).\
            Separate with commas if specifying multiple datasets.
        subj_id: ID of subject to be corrected.
        giant_move: Set giant_move option for align_epi_anat if final align of\
            anatomy to corrected EPI fails if datasets are far apart in space.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `UnWarpEpiPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(UN_WARP_EPI_PY_METADATA)
    cargs = []
    cargs.append("unWarpEPI.py")
    cargs.append("-f")
    cargs.extend(["-f", execution.input_file(forward)])
    cargs.append("-r")
    cargs.extend(["-r", execution.input_file(reverse)])
    cargs.append("-a")
    cargs.extend(["-a", execution.input_file(anat4warp)])
    cargs.append("-d")
    cargs.extend(["-d", data])
    cargs.append("-s")
    cargs.extend(["-s", subj_id])
    if giant_move:
        cargs.append("-g")
    ret = UnWarpEpiPyOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "UN_WARP_EPI_PY_METADATA",
    "UnWarpEpiPyOutputs",
    "un_warp_epi_py",
]
