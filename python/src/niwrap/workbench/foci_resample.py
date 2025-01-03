# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FOCI_RESAMPLE_METADATA = Metadata(
    id="d25e8eee3893055f474c3819282ad3f943c97a1d.boutiques",
    name="foci-resample",
    package="workbench",
    container_image_tag="brainlife/connectome_workbench:1.5.0-freesurfer-update",
)


@dataclasses.dataclass
class FociResampleLeftSurfaces:
    """
    the left surfaces for resampling.
    """
    current_surf: InputPathType
    """the surface the foci are currently projected on"""
    new_surf: InputPathType
    """the surface to project the foci onto"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-left-surfaces")
        cargs.append(execution.input_file(self.current_surf))
        cargs.append(execution.input_file(self.new_surf))
        return cargs


@dataclasses.dataclass
class FociResampleRightSurfaces:
    """
    the right surfaces for resampling.
    """
    current_surf: InputPathType
    """the surface the foci are currently projected on"""
    new_surf: InputPathType
    """the surface to project the foci onto"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-right-surfaces")
        cargs.append(execution.input_file(self.current_surf))
        cargs.append(execution.input_file(self.new_surf))
        return cargs


@dataclasses.dataclass
class FociResampleCerebellumSurfaces:
    """
    the cerebellum surfaces for resampling.
    """
    current_surf: InputPathType
    """the surface the foci are currently projected on"""
    new_surf: InputPathType
    """the surface to project the foci onto"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            execution: The execution object.
        Returns:
            Command line arguments
        """
        cargs = []
        cargs.append("-cerebellum-surfaces")
        cargs.append(execution.input_file(self.current_surf))
        cargs.append(execution.input_file(self.new_surf))
        return cargs


class FociResampleOutputs(typing.NamedTuple):
    """
    Output object returned when calling `foci_resample(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    foci_out: OutputPathType
    """the output foci file"""


def foci_resample(
    foci_in: InputPathType,
    foci_out: str,
    left_surfaces: FociResampleLeftSurfaces | None = None,
    right_surfaces: FociResampleRightSurfaces | None = None,
    cerebellum_surfaces: FociResampleCerebellumSurfaces | None = None,
    opt_discard_distance_from_surface: bool = False,
    opt_restore_xyz: bool = False,
    runner: Runner | None = None,
) -> FociResampleOutputs:
    """
    Project foci to a different surface.
    
    Unprojects foci from the <current-surf> for the structure, then projects
    them to <new-surf>. If the foci have meaningful distances above or below the
    surface, use anatomical surfaces. If the foci should be on the surface, use
    registered spheres and the options -discard-distance-from-surface and
    -restore-xyz.
    
    Author: Connectome Workbench Developers
    
    URL: https://github.com/Washington-University/workbench
    
    Args:
        foci_in: the input foci file.
        foci_out: the output foci file.
        left_surfaces: the left surfaces for resampling.
        right_surfaces: the right surfaces for resampling.
        cerebellum_surfaces: the cerebellum surfaces for resampling.
        opt_discard_distance_from_surface: ignore the distance the foci are\
            above or below the current surface.
        opt_restore_xyz: put the original xyz coordinates into the foci, rather\
            than the coordinates obtained from unprojection.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FociResampleOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOCI_RESAMPLE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-foci-resample")
    cargs.append(execution.input_file(foci_in))
    cargs.append(foci_out)
    if left_surfaces is not None:
        cargs.extend(left_surfaces.run(execution))
    if right_surfaces is not None:
        cargs.extend(right_surfaces.run(execution))
    if cerebellum_surfaces is not None:
        cargs.extend(cerebellum_surfaces.run(execution))
    if opt_discard_distance_from_surface:
        cargs.append("-discard-distance-from-surface")
    if opt_restore_xyz:
        cargs.append("-restore-xyz")
    ret = FociResampleOutputs(
        root=execution.output_file("."),
        foci_out=execution.output_file(foci_out),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOCI_RESAMPLE_METADATA",
    "FociResampleCerebellumSurfaces",
    "FociResampleLeftSurfaces",
    "FociResampleOutputs",
    "FociResampleRightSurfaces",
    "foci_resample",
]
