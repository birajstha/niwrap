# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


ADD_TO_SPEC_FILE_METADATA = Metadata(
    id="fba7b8da42e9d7aa382689587036d60e92241cb4",
    name="add-to-spec-file",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class AddToSpecFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `add_to_spec_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def add_to_spec_file(
    specfile: str,
    structure: str,
    filename: str,
    runner: Runner = None,
) -> AddToSpecFileOutputs:
    """
    add-to-spec-file by Washington University School of Medicin.
    
    Add a file to a specification file.
    
    The resulting spec file overwrites the existing spec file. If the spec file
    doesn't exist, it is created with default metadata. The structure argument
    must be one of the following:
    
    CORTEX_LEFT
    CORTEX_RIGHT
    CEREBELLUM
    ACCUMBENS_LEFT
    ACCUMBENS_RIGHT
    ALL_GREY_MATTER
    ALL_WHITE_MATTER
    AMYGDALA_LEFT
    AMYGDALA_RIGHT
    BRAIN_STEM
    CAUDATE_LEFT
    CAUDATE_RIGHT
    CEREBELLAR_WHITE_MATTER_LEFT
    CEREBELLAR_WHITE_MATTER_RIGHT
    CEREBELLUM_LEFT
    CEREBELLUM_RIGHT
    CEREBRAL_WHITE_MATTER_LEFT
    CEREBRAL_WHITE_MATTER_RIGHT
    CORTEX
    DIENCEPHALON_VENTRAL_LEFT
    DIENCEPHALON_VENTRAL_RIGHT
    HIPPOCAMPUS_LEFT
    HIPPOCAMPUS_RIGHT
    INVALID
    OTHER
    OTHER_GREY_MATTER
    OTHER_WHITE_MATTER
    PALLIDUM_LEFT
    PALLIDUM_RIGHT
    PUTAMEN_LEFT
    PUTAMEN_RIGHT
    THALAMUS_LEFT
    THALAMUS_RIGHT
    .
    
    Args:
        specfile: the specification file to add to
        structure: the structure of the data file
        filename: the path to the file
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `AddToSpecFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ADD_TO_SPEC_FILE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-add-to-spec-file")
    cargs.append(specfile)
    cargs.append(structure)
    cargs.append(filename)
    ret = AddToSpecFileOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ADD_TO_SPEC_FILE_METADATA",
    "AddToSpecFileOutputs",
    "add_to_spec_file",
]
