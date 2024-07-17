# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

SURFACE_FWHM_CALCULATOR_METADATA = Metadata(
    id="bc2f76bd91b66d16734202d1c3680da6ab6d1ca6",
    name="Surface FWHM Calculator",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class SurfaceFwhmCalculatorOutputs(typing.NamedTuple):
    """
    Output object returned when calling `surface_fwhm_calculator(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    detrended_output: OutputPathType | None
    """Detrended dataset."""
    main_output: OutputPathType | None
    """Main output dataset."""
    histogram_output: OutputPathType | None
    """Histogram showing the distribution of local FWHM."""
    mask_output: OutputPathType | None
    """Mask output dataset."""


def surface_fwhm_calculator(
    input_file: InputPathType,
    mask: InputPathType | None = None,
    surf_1: str | None = None,
    surf_sphere: str | None = None,
    clean: bool = False,
    detrend: float | int | None = None,
    detpoly: float | int | None = None,
    detprefix: str | None = None,
    prefix: str | None = None,
    vox_size: float | int | None = None,
    neighborhood: float | int | None = None,
    ok_warn: bool = False,
    examples: bool = False,
    slice_: bool = False,
    runner: Runner | None = None,
) -> SurfaceFwhmCalculatorOutputs:
    """
    Surface FWHM Calculator by AFNI Team.
    
    A program for calculating local and global FWHM.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/SurfFWHM.html
    
    Args:
        input_file: Dataset for which the FWHM is to be calculated.
        mask: Node mask so that only nodes in the mask are used to obtain\
            estimates.
        surf_1: Option for specifying the surface over which the input dataset\
            is defined.
        surf_sphere: Spherical version of -SURF_1 for Local FWHM estimates.
        clean: Strip text from output to simplify parsing.
        detrend: Detrend to order 'q'. If q is not given, the program picks\
            q=NT/30.
        detpoly: Detrend with polynomials of order p.
        detprefix: Save the detrended file into a dataset with prefix 'd'.
        prefix: Prefix of output data set.
        vox_size: Specify the nominal voxel size in mm.
        neighborhood: Neighborhood radius R for local FWHM estimates.
        ok_warn: Flag to set the mode to ok_warn.
        examples: Show command line examples and quit.
        slice_: Use the contours from planar intersections to estimate\
            gradients. For testing and development purposes only.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `SurfaceFwhmCalculatorOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(SURFACE_FWHM_CALCULATOR_METADATA)
    cargs = []
    cargs.append("SurfFWHM")
    cargs.append(execution.input_file(input_file))
    if mask is not None:
        cargs.extend(["-MASK", execution.input_file(mask)])
    if surf_1 is not None:
        cargs.extend(["-SURF_1", surf_1])
    if surf_sphere is not None:
        cargs.extend(["-SURF_SPHERE", surf_sphere])
    if clean:
        cargs.append("-clean")
    if detrend is not None:
        cargs.extend(["-detrend", str(detrend)])
    if detpoly is not None:
        cargs.extend(["-detpoly", str(detpoly)])
    if detprefix is not None:
        cargs.extend(["-detprefix", detprefix])
    if prefix is not None:
        cargs.extend(["-prefix", prefix])
    if vox_size is not None:
        cargs.extend(["-vox_size", str(vox_size)])
    if neighborhood is not None:
        cargs.extend(["-hood", str(neighborhood)])
    if ok_warn:
        cargs.append("-ok_warn")
    if examples:
        cargs.append("-examples")
    if slice_:
        cargs.append("-slice")
    cargs.append("[TALK_SUMA_OPTIONS]")
    cargs.append("[NIML_OPTIONS]")
    cargs.append("[DEBUG_OPTIONS]")
    cargs.append("[HELP_OPTIONS]")
    ret = SurfaceFwhmCalculatorOutputs(
        root=execution.output_file("."),
        detrended_output=execution.output_file(f"{prefix}.1D.dset", optional=True) if prefix is not None else None,
        main_output=execution.output_file(f"{prefix}.nii.gz", optional=True) if prefix is not None else None,
        histogram_output=execution.output_file(f"{prefix}_histog.1D", optional=True) if prefix is not None else None,
        mask_output=execution.output_file(f"{prefix}_mask.nii.gz", optional=True) if prefix is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "SURFACE_FWHM_CALCULATOR_METADATA",
    "SurfaceFwhmCalculatorOutputs",
    "surface_fwhm_calculator",
]
