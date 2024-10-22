# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FIDUCIALS_CALIBRATION_METADATA = Metadata(
    id="445a4b2fe29e36b5286fe1c80268453941ab7144.boutiques",
    name="fiducials_calibration",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class FiducialsCalibrationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fiducials_calibration(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fiducials_calibration(
    runner: Runner | None = None,
) -> FiducialsCalibrationOutputs:
    """
    A tool used for calibrating fiducials.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FiducialsCalibrationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FIDUCIALS_CALIBRATION_METADATA)
    cargs = []
    cargs.append("fiducials_calibration")
    ret = FiducialsCalibrationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FIDUCIALS_CALIBRATION_METADATA",
    "FiducialsCalibrationOutputs",
    "fiducials_calibration",
]