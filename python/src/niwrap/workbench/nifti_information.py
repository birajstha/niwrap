# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


NIFTI_INFORMATION_METADATA = Metadata(
    id="1983c034cd57becf410baf69211fa8dc122217c3",
    name="nifti-information",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class NiftiInformationOutputs(typing.NamedTuple):
    """
    Output object returned when calling `nifti_information(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def nifti_information(
    nifti_file: str,
    opt_print_header: bool = False,
    opt_allow_truncated: bool = False,
    opt_print_matrix: bool = False,
    opt_print_xml: bool = False,
    opt_version_version: str | None = None,
    runner: Runner = None,
) -> NiftiInformationOutputs:
    """
    nifti-information by Washington University School of Medicin.
    
    Display information about a nifti/cifti file.
    
    You must specify at least one -print-* option.
    
    Args:
        nifti_file: the nifti/cifti file to examine
        opt_print_header: display the header contents
        opt_allow_truncated: print the header even if the data is truncated
        opt_print_matrix: output the values in the matrix (cifti only)
        opt_print_xml: print the cifti XML (cifti only)
        opt_version_version: convert the XML to a specific CIFTI version
            (default is the file's cifti version): the CIFTI version to use
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `NiftiInformationOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(NIFTI_INFORMATION_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-nifti-information")
    cargs.append(nifti_file)
    if opt_print_header:
        cargs.append("-print-header")
    if opt_allow_truncated:
        cargs.append("-allow-truncated")
    if opt_print_matrix:
        cargs.append("-print-matrix")
    if opt_print_xml:
        cargs.append("-print-xml")
    if opt_version_version is not None:
        cargs.extend(["-version", opt_version_version])
    ret = NiftiInformationOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "NIFTI_INFORMATION_METADATA",
    "NiftiInformationOutputs",
    "nifti_information",
]
