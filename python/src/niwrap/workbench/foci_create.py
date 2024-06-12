# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FOCI_CREATE_METADATA = Metadata(
    id="ae571d078894a26aee60faeaafa69bdead3b9cde",
    name="foci-create",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class FociCreateClass:
    """
    specify class input data
    """
    
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
        return cargs


class FociCreateOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_create(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output foci file"""


def foci_create(
    output: InputPathType,
    class_: list[FociCreateClass] = None,
    runner: Runner = None,
) -> FociCreateOutputs:
    """
    foci-create by Washington University School of Medicin.
    
    Create a foci file.
    
    Creates a foci file from names, coordinates, and RGB values in a text file.
    The text file must have the following format (2 lines per focus):
    
    <focus-name>
    <red> <green> <blue> <x> <y> <z>
    ...
    
    Foci names are specified on a separate line from their coordinates and
    color, in order to let foci names contain spaces. Whitespace is trimmed from
    both ends of the foci name, but is kept if it is in the middle of a name.
    The values of <red>, <green>, <blue> and must be integers from 0 to 255, and
    will specify the color the foci is drawn as.
    
    Foci are grouped into classes and the name for the class is specified using
    the <class-name> parameter.
    
    All foci within one text file must be associated with the structure
    contained in the <surface> parameter and are projected to that surface.
    
    Args:
        output: the output foci file.
        class_: specify class input data.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociCreateOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_CREATE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-create")
    cargs.append(execution.input_file(output))
    if class_ is not None:
        cargs.extend(["-class", *[a for c in [s.run(execution) for s in class_] for a in c]])
    ret = FociCreateOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{pathlib.Path(output).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOCI_CREATE_METADATA",
    "FociCreateClass",
    "FociCreateOutputs",
    "foci_create",
]
