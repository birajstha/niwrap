# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_AFNITO_NIFTI_METADATA = Metadata(
    id="3a13b2f4c45a8aa8ca8f5b70399944c96172a06e",
    name="3dAFNItoNIFTI",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="afni/afni_latest",
)


class V3dAfnitoNiftiOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_afnito_nifti(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_nifti: OutputPathType | None
    """Output NIfTI file."""


def v_3d_afnito_nifti(
    input_dataset: InputPathType,
    prefix: str | None = None,
    verbose: bool = False,
    force_float: bool = False,
    pure: bool = False,
    denote: bool = False,
    oldid: bool = False,
    newid: bool = False,
    runner: Runner = None,
) -> V3dAfnitoNiftiOutputs:
    """
    3dAFNItoNIFTI by AFNI Team.
    
    Converts an AFNI dataset to a NIfTI-1.1 file.
    
    More information: https://afni.nimh.nih.gov/
    
    Args:
        input_dataset: Input AFNI dataset.
        prefix: Output NIfTI file prefix.
        verbose: Print progress messages (increases verbosity if repeated).
        force_float: Force the output dataset to be 32-bit floats.
        pure: Do not write an AFNI extension field into the output file.
        denote: Remove text notes from AFNI extension field that might contain\
            identifying information.
        oldid: Retain the input dataset's AFNI ID code.
        newid: Assign a new AFNI ID code to the dataset (default action).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dAfnitoNiftiOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_AFNITO_NIFTI_METADATA)
    cargs = []
    cargs.append("3dAFNItoNIFTI")
    cargs.append(execution.input_file(input_dataset))
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if verbose:
        cargs.append("-verb")
    if force_float:
        cargs.append("-float")
    if pure:
        cargs.append("-pure")
    if denote:
        cargs.append("-denote")
    if oldid:
        cargs.append("-oldid")
    if newid:
        cargs.append("-newid")
    ret = V3dAfnitoNiftiOutputs(
        root=execution.output_file("."),
        output_nifti=execution.output_file(f"{prefix}.nii") if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dAfnitoNiftiOutputs",
    "V_3D_AFNITO_NIFTI_METADATA",
    "v_3d_afnito_nifti",
]
