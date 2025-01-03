# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKSIFT2_METADATA = Metadata(
    id="399c2a04022ba3cedcda7e35cf69c1dae578656c.boutiques",
    name="tcksift2",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Tcksift2Config:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value: str
    """temporarily set the value of an MRtrix config file entry."""
    
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
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class Tcksift2Outputs(typing.NamedTuple):
    """
    Output object returned when calling `tcksift2(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    out_weights: OutputPathType
    """output text file containing the weighting factor for each streamline"""
    csv_: OutputPathType | None
    """output statistics of execution per iteration to a .csv file """
    out_mu: OutputPathType | None
    """output the final value of SIFT proportionality coefficient mu to a text
    file """
    out_coeffs: OutputPathType | None
    """output text file containing the weighting coefficient for each streamline
    """


def tcksift2(
    in_tracks: InputPathType,
    in_fod: InputPathType,
    out_weights: str,
    proc_mask: InputPathType | None = None,
    act: InputPathType | None = None,
    fd_scale_gm: bool = False,
    no_dilate_lut: bool = False,
    make_null_lobes: bool = False,
    remove_untracked: bool = False,
    fd_thresh: float | None = None,
    csv_: str | None = None,
    out_mu: str | None = None,
    output_debug: bool = False,
    out_coeffs: str | None = None,
    reg_tikhonov: float | None = None,
    reg_tv: float | None = None,
    min_td_frac: float | None = None,
    min_iters: int | None = None,
    max_iters: int | None = None,
    min_factor: float | None = None,
    min_coeff: float | None = None,
    max_factor: float | None = None,
    max_coeff: float | None = None,
    max_coeff_step: float | None = None,
    min_cf_decrease: float | None = None,
    linear: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tcksift2Config] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Tcksift2Outputs:
    """
    Optimise per-streamline cross-section multipliers to match a whole-brain
    tractogram to fixel-wise fibre densities.
    
    
    
    References:
    
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT2: Enabling
    dense quantitative assessment of brain white matter connectivity using
    streamlines tractography. NeuroImage, 2015, 119, 338-351
    
    * If using the -linear option:
    Smith, RE; Raffelt, D; Tournier, J-D; Connelly, A. Quantitative Streamlines
    Tractography: Methods and Inter-Subject Normalisation. Open Science
    Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        in_tracks: the input track file.
        in_fod: input image containing the spherical harmonics of the fibre\
            orientation distributions.
        out_weights: output text file containing the weighting factor for each\
            streamline.
        proc_mask: provide an image containing the processing mask weights for\
            the model; image spatial dimensions must match the fixel image.
        act: use an ACT five-tissue-type segmented anatomical image to derive\
            the processing mask.
        fd_scale_gm: provide this option (in conjunction with -act) to\
            heuristically downsize the fibre density estimates based on the\
            presence of GM in the voxel. This can assist in reducing tissue\
            interface effects when using a single-tissue deconvolution algorithm.
        no_dilate_lut: do NOT dilate FOD lobe lookup tables; only map\
            streamlines to FOD lobes if the precise tangent lies within the angular\
            spread of that lobe.
        make_null_lobes: add an additional FOD lobe to each voxel, with zero\
            integral, that covers all directions with zero / negative FOD\
            amplitudes.
        remove_untracked: remove FOD lobes that do not have any streamline\
            density attributed to them; this improves filtering slightly, at the\
            expense of longer computation time (and you can no longer do\
            quantitative comparisons between reconstructions if this is enabled).
        fd_thresh: fibre density threshold; exclude an FOD lobe from filtering\
            processing if its integral is less than this amount (streamlines will\
            still be mapped to it, but it will not contribute to the cost function\
            or the filtering).
        csv_: output statistics of execution per iteration to a .csv file.
        out_mu: output the final value of SIFT proportionality coefficient mu\
            to a text file.
        output_debug: provide various output images for assessing & debugging\
            performance etc.
        out_coeffs: output text file containing the weighting coefficient for\
            each streamline.
        reg_tikhonov: provide coefficient for regularising streamline weighting\
            coefficients (Tikhonov regularisation) (default: 0).
        reg_tv: provide coefficient for regularising variance of streamline\
            weighting coefficient to fixels along its length (Total Variation\
            regularisation) (default: 0.1).
        min_td_frac: minimum fraction of the FOD integral reconstructed by\
            streamlines; if the reconstructed streamline density is below this\
            fraction, the fixel is excluded from optimisation (default: 0.1).
        min_iters: minimum number of iterations to run before testing for\
            convergence; this can prevent premature termination at early iterations\
            if the cost function increases slightly (default: 10).
        max_iters: maximum number of iterations to run before terminating\
            program.
        min_factor: minimum weighting factor for an individual streamline; if\
            the factor falls below this number the streamline will be rejected\
            entirely (factor set to zero) (default: 0).
        min_coeff: minimum weighting coefficient for an individual streamline;\
            similar to the '-min_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -min_factor and -min_coeff options\
            are mutually exclusive - you can only provide one. (default: -inf).
        max_factor: maximum weighting factor that can be assigned to any one\
            streamline (default: inf).
        max_coeff: maximum weighting coefficient for an individual streamline;\
            similar to the '-max_factor' option, but using the exponential\
            coefficient basis of the SIFT2 model; these parameters are related as:\
            factor = e^(coeff). Note that the -max_factor and -max_coeff options\
            are mutually exclusive - you can only provide one. (default: inf).
        max_coeff_step: maximum change to a streamline's weighting coefficient\
            in a single iteration (default: 1).
        min_cf_decrease: minimum decrease in the cost function (as a fraction\
            of the initial value) that must occur each iteration for the algorithm\
            to continue (default: 2.5e-05).
        linear: perform a linear estimation of streamline weights, rather than\
            the standard non-linear optimisation (typically does not provide as\
            accurate a model fit; but only requires a single pass).
        info: display information messages.
        quiet: do not display information messages or progress status;\
            alternatively, this can be achieved by setting the MRTRIX_QUIET\
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as\
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications\
            (set to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `Tcksift2Outputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKSIFT2_METADATA)
    cargs = []
    cargs.append("tcksift2")
    if proc_mask is not None:
        cargs.extend([
            "-proc_mask",
            execution.input_file(proc_mask)
        ])
    if act is not None:
        cargs.extend([
            "-act",
            execution.input_file(act)
        ])
    if fd_scale_gm:
        cargs.append("-fd_scale_gm")
    if no_dilate_lut:
        cargs.append("-no_dilate_lut")
    if make_null_lobes:
        cargs.append("-make_null_lobes")
    if remove_untracked:
        cargs.append("-remove_untracked")
    if fd_thresh is not None:
        cargs.extend([
            "-fd_thresh",
            str(fd_thresh)
        ])
    if csv_ is not None:
        cargs.extend([
            "-csv",
            csv_
        ])
    if out_mu is not None:
        cargs.extend([
            "-out_mu",
            out_mu
        ])
    if output_debug:
        cargs.append("-output_debug")
    if out_coeffs is not None:
        cargs.extend([
            "-out_coeffs",
            out_coeffs
        ])
    if reg_tikhonov is not None:
        cargs.extend([
            "-reg_tikhonov",
            str(reg_tikhonov)
        ])
    if reg_tv is not None:
        cargs.extend([
            "-reg_tv",
            str(reg_tv)
        ])
    if min_td_frac is not None:
        cargs.extend([
            "-min_td_frac",
            str(min_td_frac)
        ])
    if min_iters is not None:
        cargs.extend([
            "-min_iters",
            str(min_iters)
        ])
    if max_iters is not None:
        cargs.extend([
            "-max_iters",
            str(max_iters)
        ])
    if min_factor is not None:
        cargs.extend([
            "-min_factor",
            str(min_factor)
        ])
    if min_coeff is not None:
        cargs.extend([
            "-min_coeff",
            str(min_coeff)
        ])
    if max_factor is not None:
        cargs.extend([
            "-max_factor",
            str(max_factor)
        ])
    if max_coeff is not None:
        cargs.extend([
            "-max_coeff",
            str(max_coeff)
        ])
    if max_coeff_step is not None:
        cargs.extend([
            "-max_coeff_step",
            str(max_coeff_step)
        ])
    if min_cf_decrease is not None:
        cargs.extend([
            "-min_cf_decrease",
            str(min_cf_decrease)
        ])
    if linear:
        cargs.append("-linear")
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend([
            "-nthreads",
            str(nthreads)
        ])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.append(execution.input_file(in_tracks))
    cargs.append(execution.input_file(in_fod))
    cargs.append(out_weights)
    ret = Tcksift2Outputs(
        root=execution.output_file("."),
        out_weights=execution.output_file(out_weights),
        csv_=execution.output_file(csv_) if (csv_ is not None) else None,
        out_mu=execution.output_file(out_mu) if (out_mu is not None) else None,
        out_coeffs=execution.output_file(out_coeffs) if (out_coeffs is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKSIFT2_METADATA",
    "Tcksift2Config",
    "Tcksift2Outputs",
    "tcksift2",
]
