# This file was auto generated by styx
# Do not edit this file directly

import pathlib
import typing

from styxdefs import *


MCFLIRT_METADATA = Metadata(
    id="c3e4c3ae27d26e48c70cea714c10eac0d4ffbf44",
    name="MCFLIRT",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class McflirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mcflirt(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mat_file: OutputPathType
    """A list of items which are an existing file name. Transformation matrices."""
    mean_img: OutputPathType | None
    """Mean timeseries image (if mean_vol=true)."""
    out_file_outfile: OutputPathType | None
    """Motion-corrected timeseries."""
    par_file: OutputPathType | None
    """Text-file with motion parameters."""
    rms_files: OutputPathType | None
    """A list of items which are an existing file name. Absolute and relative displacement parameters."""
    std_img: OutputPathType | None
    """Standard deviation image."""
    variance_img: OutputPathType | None
    """Variance image."""


def mcflirt(
    in_file: InputPathType,
    bins: int | None = None,
    cost: typing.Literal["mutualinfo", "woods", "corratio", "normcorr", "normmi", "leastsquares"] | None = None,
    dof: int | None = None,
    init: InputPathType | None = None,
    interpolation: typing.Literal["spline_final", "nn_final", "sinc_final"] | None = None,
    mean_vol: bool = False,
    out_file: InputPathType | None = None,
    ref_file: InputPathType | None = None,
    ref_vol: int | None = None,
    rotation: int | None = None,
    save_mats: bool = False,
    save_plots: bool = False,
    save_rms: bool = False,
    scaling: float | int | None = None,
    smooth: float | int | None = None,
    stages: int | None = None,
    stats_imgs: bool = False,
    use_contour: bool = False,
    use_gradient: bool = False,
    runner: Runner = None,
) -> McflirtOutputs:
    """
    MCFLIRT by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    MCFLIRT is an intra-modal motion correction tool designed for use on fMRI
    time series and based on optimization and registration techniques used in
    FLIRT, a fully automated robust and accurate tool for linear (affine) inter-
    and inter-modal brain image registration.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/MCFLIRT
    
    Args:
        in_file: Timeseries to motion-correct.
        bins: Number of histogram bins.
        cost: 'mutualinfo' or 'woods' or 'corratio' or 'normcorr' or 'normmi' or
            'leastsquares'. Cost function to optimize.
        dof: Degrees of freedom for the transformation.
        init: Initial transformation matrix.
        interpolation: 'spline' or 'nn' or 'sinc'. Interpolation method for
            transformation.
        mean_vol: Register to mean volume.
        out_file: File to write.
        ref_file: Target image for motion correction.
        ref_vol: Volume to align frames to.
        rotation: Scaling factor for rotation tolerances.
        save_mats: Save transformation matrices.
        save_plots: Save transformation parameters.
        save_rms: Save rms displacement parameters.
        scaling: Scaling factor to use.
        smooth: Smoothing factor for the cost function.
        stages: Stages (if 4, perform final search with sinc interpolation.
        stats_imgs: Produce variance and std. dev. images.
        use_contour: Run search on contour images.
        use_gradient: Run search on gradient images.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `McflirtOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MCFLIRT_METADATA)
    cargs = []
    cargs.append("mcflirt")
    cargs.extend(["-in", execution.input_file(in_file)])
    if bins is not None:
        cargs.extend(["-bins", str(bins)])
    if cost is not None:
        cargs.extend(["-cost", cost])
    if dof is not None:
        cargs.extend(["-dof", str(dof)])
    if init is not None:
        cargs.extend(["-init", execution.input_file(init)])
    if interpolation is not None:
        cargs.append(("-" + interpolation))
    if mean_vol:
        cargs.append("-meanvol")
    if out_file is not None:
        cargs.extend(["-out", execution.input_file(out_file)])
    if ref_file is not None:
        cargs.extend(["-reffile", execution.input_file(ref_file)])
    if ref_vol is not None:
        cargs.extend(["-refvol", str(ref_vol)])
    if rotation is not None:
        cargs.extend(["-rotation", str(rotation)])
    if save_mats:
        cargs.append("-mats")
    if save_plots:
        cargs.append("-plots")
    if save_rms:
        cargs.append("-rmsabs -rmsrel")
    if scaling is not None:
        cargs.extend(["-scaling", str(scaling)])
    if smooth is not None:
        cargs.extend(["-smooth", str(smooth)])
    if stages is not None:
        cargs.extend(["-stages", str(stages)])
    if stats_imgs:
        cargs.append("-stats")
    if use_contour:
        cargs.append("-edge")
    if use_gradient:
        cargs.append("-gdt")
    ret = McflirtOutputs(
        root=execution.output_file("."),
        mat_file=execution.output_file(f"MAT_*", optional=True),
        mean_img=execution.output_file(f"{pathlib.Path(out_file).stem}_mean_reg.ext", optional=True) if out_file is not None else None,
        out_file_outfile=execution.output_file(f"{pathlib.Path(out_file).stem}", optional=True) if out_file is not None else None,
        par_file=execution.output_file(f"{pathlib.Path(out_file).stem}.par", optional=True) if out_file is not None else None,
        rms_files=execution.output_file(f"{pathlib.Path(out_file).stem}_*.rms", optional=True) if out_file is not None else None,
        std_img=execution.output_file(f"{pathlib.Path(out_file).stem}_sigma.ext", optional=True) if out_file is not None else None,
        variance_img=execution.output_file(f"{pathlib.Path(out_file).stem}_variance.ext", optional=True) if out_file is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MCFLIRT_METADATA",
    "McflirtOutputs",
    "mcflirt",
]
