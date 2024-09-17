# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

BET_METADATA = Metadata(
    id="0a7819f0c98ae5620097d3a5297b51a33edc1d6e.boutiques",
    name="bet",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class BetOutputs(typing.NamedTuple):
    """
    Output object returned when calling `bet(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    outfile: OutputPathType
    """Main default mask output of BET"""
    binary_mask: OutputPathType
    """Binary mask file (from -m option)"""
    overlay_file: OutputPathType
    """Overlaid brain surface onto original image"""
    approx_skull_img: OutputPathType
    """Approximate skull image file"""
    output_vtk_mesh: OutputPathType
    """Mesh in VTK format"""
    skull_mask: OutputPathType
    """Output mask for skull image"""
    out_inskull_mask: OutputPathType
    """The in-skull mask file from betsurf (from -A or -A2)"""
    out_inskull_mesh: OutputPathType
    """The in-skull mesh file from betsurf (from -A or -A2)"""
    out_inskull_off: OutputPathType
    """The in-skull mesh .off file from betsurf (from -A or -A2)"""
    out_outskin_mask: OutputPathType
    """The out-skin mask file from betsurf (from -A or -A2)"""
    out_outskin_mesh: OutputPathType
    """The out-skin mesh file from betsurf (from -A or -A2)"""
    out_outskin_off: OutputPathType
    """The out-skin mesh .off file from betsurf (from -A or -A2)"""
    out_outskull_mask: OutputPathType
    """The out-skull mask file from betsurf (from -A or -A2)"""
    out_outskull_mesh: OutputPathType
    """The out-skull mesh file from betsurf (from -A or -A2)"""
    out_outskull_off: OutputPathType
    """The out-skull mesh .off file from betsurf (from -A or -A2)"""


def bet(
    infile: InputPathType,
    maskfile: str = "img_bet",
    fractional_intensity: float | None = None,
    vg_fractional_intensity: float | None = None,
    center_of_gravity: list[float] | None = None,
    overlay: bool = False,
    binary_mask: bool = False,
    approx_skull: bool = False,
    no_seg_output: bool = False,
    vtk_mesh: bool = False,
    head_radius: float | None = None,
    thresholding: bool = False,
    robust_iters: bool = False,
    residual_optic_cleanup: bool = False,
    reduce_bias: bool = False,
    slice_padding: bool = False,
    whole_set_mask: bool = False,
    additional_surfaces: bool = False,
    additional_surfaces_t2: InputPathType | None = None,
    verbose: bool = False,
    debug: bool = False,
    runner: Runner | None = None,
) -> BetOutputs:
    """
    Automated brain extraction tool for FSL.
    
    Author: Oxford Centre for Functional MRI of the Brain (FMRIB)
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/BET
    
    Args:
        infile: Input image (e.g. img.nii.gz).
        maskfile: Output brain mask (e.g. img_bet.nii.gz).
        fractional_intensity: Fractional intensity threshold (0->1);\
            default=0.5; smaller values give larger brain outline estimates.
        vg_fractional_intensity: Vertical gradient in fractional intensity\
            threshold (-1->1); default=0; positive values give larger brain outline\
            at bottom, smaller at top.
        center_of_gravity: The xyz coordinates of the center of gravity\
            (voxels, not mm) of initial mesh surface. Must have exactly three\
            numerical entries in the list (3-vector).
        overlay: Generate brain surface outline overlaid onto original image.
        binary_mask: Generate binary brain mask.
        approx_skull: Generate rough skull image (not as clean as betsurf).
        no_seg_output: Don't generate segmented brain image output.
        vtk_mesh: Generate brain surface as mesh in .vtk format.
        head_radius: head radius (mm not voxels); initial surface sphere is set\
            to half of this.
        thresholding: Apply thresholding to segmented brain image and mask.
        robust_iters: More robust brain center estimation, by iterating BET\
            with a changing center-of-gravity.
        residual_optic_cleanup: This attempts to cleanup residual eye and optic\
            nerve voxels which bet2 can sometimes leave behind. This can be useful\
            when running SIENA or SIENAX, for example. Various stages involving\
            standard-space masking, morphpological operations and thresholdings are\
            combined to produce a result which can often give better results than\
            just running bet2.
        reduce_bias: This attempts to reduce image bias, and residual neck\
            voxels. This can be useful when running SIENA or SIENAX, for example.\
            Various stages involving FAST segmentation-based bias field removal and\
            standard-space masking are combined to produce a result which can often\
            give better results than just running bet2.
        slice_padding: This can improve the brain extraction if only a few\
            slices are present in the data (i.e., a small field of view in the Z\
            direction). This is achieved by padding the end slices in both\
            directions, copying the end slices several times, running bet2 and then\
            removing the added slices.
        whole_set_mask: This option uses bet2 to determine a brain mask on the\
            basis of the first volume in a 4D data set, and applies this to the\
            whole data set. This is principally intended for use on FMRI data, for\
            example to remove eyeballs. Because it is normally important (in this\
            application) that masking be liberal (ie that there be little risk of\
            cutting out valid brain voxels) the -f threshold is reduced to 0.3, and\
            also the brain mask is "dilated" slightly before being used.
        additional_surfaces: This runs both bet2 and betsurf programs in order\
            to get the additional skull and scalp surfaces created by betsurf. This\
            involves registering to standard space in order to allow betsurf to\
            find the standard space masks it needs.
        additional_surfaces_t2: This is the same as -A except that a T2 image\
            is also input, to further improve the estimated skull and scalp\
            surfaces. As well as carrying out the standard space registration this\
            also registers the T2 to the T1 input image.
        verbose: Switch on diagnostic messages.
        debug: Don't delete temporary intermediate images.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `BetOutputs`).
    """
    if fractional_intensity is not None and not (0 <= fractional_intensity <= 1): 
        raise ValueError(f"'fractional_intensity' must be between 0 <= x <= 1 but was {fractional_intensity}")
    if vg_fractional_intensity is not None and not (-1 <= vg_fractional_intensity <= 1): 
        raise ValueError(f"'vg_fractional_intensity' must be between -1 <= x <= 1 but was {vg_fractional_intensity}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(BET_METADATA)
    cargs = []
    cargs.append("bet")
    cargs.append(execution.input_file(infile))
    cargs.append(maskfile)
    if fractional_intensity is not None:
        cargs.extend([
            "-f",
            str(fractional_intensity)
        ])
    if vg_fractional_intensity is not None:
        cargs.extend([
            "-g",
            str(vg_fractional_intensity)
        ])
    if center_of_gravity is not None:
        cargs.extend([
            "-c",
            *map(str, center_of_gravity)
        ])
    if overlay:
        cargs.append("-o")
    if binary_mask:
        cargs.append("-m")
    if approx_skull:
        cargs.append("-s")
    if no_seg_output:
        cargs.append("-n")
    if vtk_mesh:
        cargs.append("-e")
    if head_radius is not None:
        cargs.extend([
            "-r",
            str(head_radius)
        ])
    if thresholding:
        cargs.append("-t")
    if robust_iters:
        cargs.append("-R")
    if residual_optic_cleanup:
        cargs.append("-S")
    if reduce_bias:
        cargs.append("-B")
    if slice_padding:
        cargs.append("-Z")
    if whole_set_mask:
        cargs.append("-F")
    if additional_surfaces:
        cargs.append("-A")
    if additional_surfaces_t2 is not None:
        cargs.extend([
            "-A2",
            execution.input_file(additional_surfaces_t2)
        ])
    if verbose:
        cargs.append("-v")
    if debug:
        cargs.append("-d")
    ret = BetOutputs(
        root=execution.output_file("."),
        outfile=execution.output_file(maskfile + ".nii.gz"),
        binary_mask=execution.output_file(maskfile + "_mask.nii.gz"),
        overlay_file=execution.output_file(maskfile + "_overlay.nii.gz"),
        approx_skull_img=execution.output_file(maskfile + "_skull.nii.gz"),
        output_vtk_mesh=execution.output_file(maskfile + "_mesh.vtk"),
        skull_mask=execution.output_file(maskfile + "_skull_mask.nii.gz"),
        out_inskull_mask=execution.output_file(maskfile + "_inskull_mask.nii.gz"),
        out_inskull_mesh=execution.output_file(maskfile + "_inskull_mesh.nii.gz"),
        out_inskull_off=execution.output_file(maskfile + "_inskull_mesh.off"),
        out_outskin_mask=execution.output_file(maskfile + "_outskin_mask.nii.gz"),
        out_outskin_mesh=execution.output_file(maskfile + "_outskin_mesh.nii.gz"),
        out_outskin_off=execution.output_file(maskfile + "_outskin_mesh.off"),
        out_outskull_mask=execution.output_file(maskfile + "_outskull_mask.nii.gz"),
        out_outskull_mesh=execution.output_file(maskfile + "_outskull_mesh.nii.gz"),
        out_outskull_off=execution.output_file(maskfile + "_outskull_mesh.off"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "BET_METADATA",
    "BetOutputs",
    "bet",
]
