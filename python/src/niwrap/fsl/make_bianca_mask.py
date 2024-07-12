# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

MAKE_BIANCA_MASK_METADATA = Metadata(
    id="60db3fe7fc0be5506fcb5e6d6ae8d7066ddd76ec",
    name="make_bianca_mask",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl-make-bianca-mask:latest",
)


class MakeBiancaMaskOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_bianca_mask(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_image: OutputPathType
    """Output image"""


def make_bianca_mask(
    input_image: InputPathType,
    output_image: InputPathType,
    overlay_flag: bool = False,
    binary_mask_flag: bool = False,
    approx_skull_flag: bool = False,
    no_seg_output_flag: bool = False,
    fractional_intensity: float | int | None = None,
    vg_fractional_intensity: float | int | None = None,
    head_radius: float | int | None = None,
    center_of_gravity: str | None = None,
    thresholding_flag: bool = False,
    vtk_mesh: bool = False,
    robust_iters_flag: bool = False,
    residual_optic_cleanup_flag: bool = False,
    reduce_bias_flag: bool = False,
    slice_padding_flag: bool = False,
    whole_set_mask_flag: bool = False,
    additional_surfaces_flag: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose_flag: bool = False,
    debug_flag: bool = False,
    runner: Runner | None = None,
) -> MakeBiancaMaskOutputs:
    """
    make_bianca_mask.
    
    A script for generating BIANCA masks.
    
    Args:
        input_image: Input image.
        output_image: Output image.
        overlay_flag: Generate brain surface outline overlaid onto original\
            image.
        binary_mask_flag: Generate binary brain mask.
        approx_skull_flag: Generate approximate skull image.
        no_seg_output_flag: Don't generate segmented brain image output.
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        head_radius: Head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        center_of_gravity: Centre-of-gravity (voxels not mm) of initial mesh\
            surface.
        thresholding_flag: Apply thresholding to segmented brain image and mask.
        vtk_mesh: Generates brain surface as mesh in .vtk format.
        robust_iters_flag: Robust brain center estimation (iterates BET several\
            times).
        residual_optic_cleanup_flag: Eye & optic nerve cleanup (can be useful\
            in SIENA - disables -o option).
        reduce_bias_flag: Bias field & neck cleanup (can be useful in SIENA).
        slice_padding_flag: Improve BET if FOV is very small in Z (by\
            temporarily padding end slices).
        whole_set_mask_flag: Apply to 4D FMRI data (uses -f 0.3 and dilates\
            brain mask slightly).
        additional_surfaces_flag: Run bet2 and then betsurf to get additional\
            skull and scalp surfaces (includes registrations).
        additional_surfaces_t2: As with -A, when also feeding in\
            non-brain-extracted T2 (includes registrations).
        verbose_flag: Verbose (switch on diagnostic messages).
        debug_flag: Debug (don't delete temporary intermediate images).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeBiancaMaskOutputs`).
    """
    runner = runner or get_global_runner()
    if fractional_intensity is not None and not (0 <= fractional_intensity <= 1): 
        raise ValueError(f"'fractional_intensity' must be between 0 <= x <= 1 but was {fractional_intensity}")
    if vg_fractional_intensity is not None and not (-1 <= vg_fractional_intensity <= 1): 
        raise ValueError(f"'vg_fractional_intensity' must be between -1 <= x <= 1 but was {vg_fractional_intensity}")
    if (
        robust_iters_flag +
        residual_optic_cleanup_flag +
        reduce_bias_flag +
        slice_padding_flag +
        whole_set_mask_flag +
        additional_surfaces_flag +
        (additional_surfaces_t2 is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "robust_iters_flag,\n"
            "residual_optic_cleanup_flag,\n"
            "reduce_bias_flag,\n"
            "slice_padding_flag,\n"
            "whole_set_mask_flag,\n"
            "additional_surfaces_flag,\n"
            "additional_surfaces_t2"
        )
    execution = runner.start_execution(MAKE_BIANCA_MASK_METADATA)
    cargs = []
    cargs.append("/usr/local/fsl/bin/make_bianca_mask")
    cargs.append("<Usage:>")
    cargs.append("<Main")
    cargs.append("bet2")
    cargs.append("options>")
    cargs.append("<Variations")
    cargs.append("on")
    cargs.append("default")
    cargs.append("bet2")
    cargs.append("functionality")
    cargs.append("(mutually")
    cargs.append("exclusive")
    cargs.append("options):>")
    cargs.append("<Miscellaneous")
    cargs.append("options:>")
    ret = MakeBiancaMaskOutputs(
        root=execution.output_file("."),
        output_image=execution.output_file(f"{pathlib.Path(output_image).name}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_BIANCA_MASK_METADATA",
    "MakeBiancaMaskOutputs",
    "make_bianca_mask",
]
