# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA = Metadata(
    id="754f3aa0c946c5cfbe25ac3e564e2cd8edaa60c6",
    name="cifti-create-parcellated-from-template",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class CiftiCreateParcellatedFromTemplateCifti:
    """
    specify an input cifti file
    """
    cifti_in: InputPathType
    """the input parcellated cifti file"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-cifti")
        cargs.append(execution.input_file(self.cifti_in))
        return cargs


class CiftiCreateParcellatedFromTemplateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `cifti_create_parcellated_from_template(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    cifti_out: OutputPathType
    """the output cifti file"""


def cifti_create_parcellated_from_template(
    cifti_template: InputPathType,
    modify_direction: str,
    cifti_out: str,
    opt_fill_value_value: float | int | None = None,
    cifti: list[CiftiCreateParcellatedFromTemplateCifti] | None = None,
    runner: Runner | None = None,
) -> CiftiCreateParcellatedFromTemplateOutputs:
    """
    cifti-create-parcellated-from-template by Washington University School of
    Medicin.
    
    Match parcels to template by name.
    
    For each parcel name in the template mapping, find that name in an input
    cifti file and use its data in the output file. All input cifti files must
    have a parcels mapping along <modify-direction> and matching mappings along
    other dimensions. The direction can be either an integer starting from 1, or
    the strings 'ROW' or 'COLUMN'.
    
    Args:
        cifti_template: a cifti file with the template parcel mapping along\
            column.
        modify_direction: which dimension of the output file should match the\
            template (integer, 'ROW', or 'COLUMN').
        cifti_out: the output cifti file.
        opt_fill_value_value: specify value to be used in parcels that don't\
            match: value to use (default 0).
        cifti: specify an input cifti file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `CiftiCreateParcellatedFromTemplateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-cifti-create-parcellated-from-template")
    cargs.append(execution.input_file(cifti_template))
    cargs.append(modify_direction)
    cargs.append(cifti_out)
    if opt_fill_value_value is not None:
        cargs.extend(["-fill-value", str(opt_fill_value_value)])
    if cifti is not None:
        cargs.extend([a for c in [s.run(execution) for s in cifti] for a in c])
    ret = CiftiCreateParcellatedFromTemplateOutputs(
        root=execution.output_file("."),
        cifti_out=execution.output_file(f"{cifti_out}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CIFTI_CREATE_PARCELLATED_FROM_TEMPLATE_METADATA",
    "CiftiCreateParcellatedFromTemplateCifti",
    "CiftiCreateParcellatedFromTemplateOutputs",
    "cifti_create_parcellated_from_template",
]
