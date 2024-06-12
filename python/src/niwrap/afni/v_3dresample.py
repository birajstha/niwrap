# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3DRESAMPLE_METADATA = Metadata(
    id="71d456ed68fb0fccec030d2d1bb82c4cfdb4af62",
    name="3dresample",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dresampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3dresample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_file: OutputPathType
    """Output image file name."""


def v_3dresample(
    in_file: InputPathType,
    prefix: str = "out.nii.gz",
    master: InputPathType | None = None,
    orientation: typing.Literal["AIL", "AIR", "ASL", "ASR", "PIL", "PIR", "PSL", "PSR", "ALI", "ALS", "ARI", "ARS", "PLI", "PLS", "PRI", "PRS", "IAL", "IAR", "IPL", "IPR", "SAL", "SAR", "SPL", "SPR", "ILA", "ILP", "IRA", "IRP", "SLA", "SLP", "SRA", "SRP", "LAI", "LAS", "LPI", "LPS", "RAI", "RAS", "RPI", "RPS", "LIA", "LIP", "LSA", "LSP", "RIA", "RIP", "RSA", "RSP"] | None = None,
    outputtype: typing.Literal["NIFTI", "AFNI", "NIFTI_GZ"] | None = None,
    resample_mode: typing.Literal["NN", "Li", "Cu", "Bk"] | None = None,
    voxel_size: list[float | int] = None,
    runner: Runner = None,
) -> V3dresampleOutputs:
    """
    3dresample by Nipype (interface).
    
    Resample or reorient an image using AFNI 3dresample command.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dresample.html
    
    Args:
        in_file: Input file to 3dresample.
        prefix: required prefix for output dataset.
        master: Align dataset grid to a reference file.
        orientation: New orientation code.
        outputtype: 'nifti' or 'afni' or 'nifti_gz'. Afni output filetype.
        resample_mode: 'nn' or 'li' or 'cu' or 'bk'. Resampling method from set\
            {"nn", "li", "cu", "bk"}. these are for "nearest neighbor", "linear",\
            "cubic" and "blocky"interpolation, respectively. default is nn.
        voxel_size: (a float, a float, a float). Resample to new dx, dy and dz.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dresampleOutputs`).
    """
    runner = runner or get_global_runner()
    if voxel_size is not None and (len(voxel_size) != 3): 
        raise ValueError(f"Length of 'voxel_size' must be 3 but was {len(voxel_size)}")
    execution = runner.start_execution(V_3DRESAMPLE_METADATA)
    cargs = []
    cargs.append("3dresample")
    cargs.extend(["-inset", execution.input_file(in_file)])
    if master is not None:
        cargs.extend(["-master", execution.input_file(master)])
    if orientation is not None:
        cargs.extend(["-orient", orientation])
    cargs.extend(["-prefix", prefix])
    if outputtype is not None:
        cargs.append(outputtype)
    if resample_mode is not None:
        cargs.extend(["-rmode", resample_mode])
    if voxel_size is not None:
        cargs.extend(["-dxyz", *map(str, voxel_size)])
    ret = V3dresampleOutputs(
        root=execution.output_file("."),
        out_file=execution.output_file(f"{prefix}", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dresampleOutputs",
    "V_3DRESAMPLE_METADATA",
    "v_3dresample",
]
