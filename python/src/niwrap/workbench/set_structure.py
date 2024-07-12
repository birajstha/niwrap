# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SET_STRUCTURE_METADATA = Metadata(
    id="7380330fce6ee441336abb558cb65e66f59c6bcf",
    name="set-structure",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SetStructureOutputs(typing.NamedTuple):
    """
    Output object returned when calling `set_structure(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def set_structure(
    data_file: str,
    structure: str,
    opt_surface_type_type: str | None = None,
    opt_surface_secondary_type_secondary_type: str | None = None,
    runner: Runner | None = None,
) -> SetStructureOutputs:
    """
    set-structure by Washington University School of Medicin.
    
    Set structure of a data file.
    
    The existing file is modified and rewritten to the same filename. Valid
    values for the structure name are:
    
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
    
    Valid names for the surface type are:
    
    UNKNOWN
    RECONSTRUCTION
    ANATOMICAL
    INFLATED
    VERY_INFLATED
    SPHERICAL
    SEMI_SPHERICAL
    ELLIPSOID
    FLAT
    HULL
    
    Valid names for the surface secondary type are:
    
    INVALID
    GRAY_WHITE
    MIDTHICKNESS
    PIAL
    .
    
    Args:
        data_file: the file to set the structure of.
        structure: the structure to set the file to.
        opt_surface_type_type: set the type of a surface (only used if file is\
            a surface file): name of surface type.
        opt_surface_secondary_type_secondary_type: set the secondary type of a\
            surface (only used if file is a surface file): name of surface\
            secondary type.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SetStructureOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SET_STRUCTURE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-set-structure")
    cargs.append(data_file)
    cargs.append(structure)
    if opt_surface_type_type is not None:
        cargs.extend(["-surface-type", opt_surface_type_type])
    if opt_surface_secondary_type_secondary_type is not None:
        cargs.extend(["-surface-secondary-type", opt_surface_secondary_type_secondary_type])
    ret = SetStructureOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SET_STRUCTURE_METADATA",
    "SetStructureOutputs",
    "set_structure",
]
