# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

CONVERT_FIBER_ORIENTATIONS_METADATA = Metadata(
    id="b03dad0ae50bf132140bf9a79b3f9433dc9bcfe1",
    name="convert-fiber-orientations",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class ConvertFiberOrientationsFiber:
    """
    specify the parameter volumes for a fiber
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


class ConvertFiberOrientationsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `convert_fiber_orientations(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    fiber_out: OutputPathType
    """the output fiber orientation file"""


def convert_fiber_orientations(
    label_volume: InputPathType,
    fiber_out: InputPathType,
    fiber: list[ConvertFiberOrientationsFiber] = None,
    runner: Runner = None,
) -> ConvertFiberOrientationsOutputs:
    """
    convert-fiber-orientations by Washington University School of Medicin.
    
    Convert bingham parameter volumes to fiber orientation file.
    
    Takes precomputed bingham parameters from volume files and converts them to
    the format workbench uses for display. The <label-volume> argument must be a
    label volume, where the labels use these strings:
    
    
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
    THALAMUS_RIGHT.
    
    Args:
        label_volume: volume of cifti structure labels.
        fiber_out: the output fiber orientation file.
        fiber: specify the parameter volumes for a fiber.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ConvertFiberOrientationsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONVERT_FIBER_ORIENTATIONS_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-convert-fiber-orientations")
    cargs.append(execution.input_file(label_volume))
    cargs.append(execution.input_file(fiber_out))
    if fiber is not None:
        cargs.extend(["-fiber", *[a for c in [s.run(execution) for s in fiber] for a in c]])
    ret = ConvertFiberOrientationsOutputs(
        root=execution.output_file("."),
        fiber_out=execution.output_file(f"{pathlib.Path(fiber_out).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONVERT_FIBER_ORIENTATIONS_METADATA",
    "ConvertFiberOrientationsFiber",
    "ConvertFiberOrientationsOutputs",
    "convert_fiber_orientations",
]
