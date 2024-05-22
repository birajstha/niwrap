# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


CIFTI_CONVERT_METADATA = Metadata(
    id="7140cdb626ccae532981dca12f8238644ca3e1a1",
    name="cifti-convert",
    container_image_type="docker",
    container_image_tag="mcin/docker-fsl:latest",
)


class CiftiConvertOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_convert(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def cifti_convert(
    opt_from_gifti_ext_gifti_in: str | None = None,
    opt_to_nifti_cifti_in: InputPathType | None = None,
    runner: Runner = None,
) -> CiftiConvertOutputs:
    """
    cifti-convert by Washington University School of Medicin.
    
    DUMP CIFTI MATRIX INTO OTHER FORMATS.
    
    This command is used to convert a full CIFTI matrix to/from formats that can
    be used by programs that don't understand CIFTI. You must specify exactly
    one of -to-gifti-ext, -from-gifti-ext, -to-nifti, -from-nifti, -to-text, or
    -from-text.
    
    If you want to write an existing CIFTI file with a different CIFTI version,
    see -file-convert, and its -cifti-version-convert option.
    
    If you want part of the CIFTI file as a metric, label, or volume file, see
    -cifti-separate. If you want to create a CIFTI file from metric and/or
    volume files, see the -cifti-create-* commands.
    
    If you want to import a matrix that is restricted to an ROI, first create a
    template CIFTI file matching that ROI using a -cifti-create-* command. After
    importing to CIFTI, you can then expand the file into a standard
    brainordinates space with -cifti-create-dense-from-template. If you want to
    export only part of a CIFTI file, first create an roi-restricted CIFTI file
    with -cifti-restrict-dense-mapping.
    
    The -transpose option to -from-gifti-ext is needed if the replacement binary
    file is in column-major order.
    
    The -unit options accept these values:
    
    SECOND
    HERTZ
    METER
    RADIAN.
    
    Args:
        opt_from_gifti_ext_gifti_in: convert a GIFTI made with this command back
            into a CIFTI: the input gifti file
        opt_to_nifti_cifti_in: convert to NIFTI1: the input cifti file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `CiftiConvertOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CONVERT_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-convert")
    if opt_from_gifti_ext_gifti_in is not None:
        cargs.extend(["-from-gifti-ext", opt_from_gifti_ext_gifti_in])
    if opt_to_nifti_cifti_in is not None:
        cargs.extend(["-to-nifti", execution.input_file(opt_to_nifti_cifti_in)])
    ret = CiftiConvertOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CONVERT_METADATA",
    "CiftiConvertOutputs",
    "cifti_convert",
]
