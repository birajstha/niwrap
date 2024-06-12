# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

ROBUST_FOV_METADATA = Metadata(
    id="0169c09dbf20519f4ff464e2364a2ba28e878213",
    name="RobustFOV",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class RobustFovOutputs(typing.NamedTuple):
    """
    Output object returned when calling `robust_fov(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_roi: OutputPathType
    """Roi volume output name."""
    out_transform: OutputPathType
    """Transformation matrix in_file to out_roi output name."""
    out_roi_: OutputPathType
    """Roi volume output name."""
    out_transform_: OutputPathType
    """Transformation matrix in_file to out_roi output name."""


def robust_fov(
    in_file: InputPathType,
    brainsize: int | None = None,
    output_type: typing.Literal["NIFTI", "NIFTI_PAIR", "NIFTI_GZ", "NIFTI_PAIR_GZ"] | None = None,
    runner: Runner = None,
) -> RobustFovOutputs:
    """
    RobustFOV by Nipype (interface).
    
    Automatically crops an image removing lower head and neck.
    Interface is stable 5.0.0 to 5.0.9, but default brainsize changed from 150mm
    to 170mm.
    
    Args:
        in_file: Input filename.
        brainsize: Size of brain in z-dimension (default 170mm/150mm).
        output_type: 'nifti' or 'nifti_pair' or 'nifti_gz' or 'nifti_pair_gz'.\
            Fsl output type.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RobustFovOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ROBUST_FOV_METADATA)
    cargs = []
    cargs.append("RobustFOV")
    cargs.extend(["-i", execution.input_file(in_file)])
    if brainsize is not None:
        cargs.extend(["-b", str(brainsize)])
    cargs.append("[OUT_ROI]")
    cargs.append("[OUT_TRANSFORM]")
    if output_type is not None:
        cargs.append(output_type)
    ret = RobustFovOutputs(
        root=execution.output_file("."),
        out_roi=execution.output_file(f"{pathlib.Path(in_file).name}_ROI", optional=True),
        out_transform=execution.output_file(f"{pathlib.Path(in_file).name}_to_ROI", optional=True),
        out_roi_=execution.output_file(f"out_roi", optional=True),
        out_transform_=execution.output_file(f"out_transform", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ROBUST_FOV_METADATA",
    "RobustFovOutputs",
    "robust_fov",
]
