# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

XFIBRES_METADATA = Metadata(
    id="8f84a39481bb32bd2ebffc5c546042b3ecb3b3a7",
    name="xfibres",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class XfibresOutputs(typing.NamedTuple):
    """
    Output object returned when calling `xfibres(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_logdir: OutputPathType
    """Log directory where output files are saved"""


def xfibres(
    datafile: InputPathType,
    maskfile: InputPathType,
    bvecs: InputPathType,
    bvals: InputPathType,
    logdir: str | None = None,
    forcedir: bool = False,
    max_fibres: float | int | None = None,
    model: float | int | None = None,
    fudge: str | None = None,
    num_jumps: float | int | None = None,
    num_burnin: float | int | None = None,
    burnin_noard: float | int | None = None,
    sampleevery: float | int | None = None,
    updateproposal: float | int | None = None,
    seed: str | None = None,
    noard: bool = False,
    allard: bool = False,
    nospat: bool = False,
    nonlinear: bool = False,
    cnonlinear: bool = False,
    rician: bool = False,
    add_f0: bool = False,
    ard_f0: bool = False,
    rmean: float | int | None = None,
    rstd: float | int | None = None,
    verbose_flag: bool = False,
    help_flag: bool = False,
    runner: Runner = None,
) -> XfibresOutputs:
    """
    xfibres by FMRIB Centre, University of Oxford.
    
    Part of FSL - estimates diffusion parameters for multiple fibres per voxel.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT/UserGuide
    
    Args:
        datafile: Data file (e.g., diffusion data)
        maskfile: Mask file defining brain voxels
        bvecs: B vectors file
        bvals: B values file
        logdir: Log directory (default is logdir)
        forcedir: Use the actual directory name given - i.e., don't add + to
            make a new directory
        max_fibres: Maximum number of fibres to fit in each voxel (default 1)
        model: Model to use: 1=deconv. with sticks (default), 2=deconv. with
            sticks and a range of diffusivities, 3=deconv. with zeppelins
        fudge: ARD fudge factor
        num_jumps: Number of jumps to be made by MCMC (default 1250)
        num_burnin: Total number of jumps at start of MCMC to be discarded
            (default 1000)
        burnin_noard: Number of burnin jumps before ARD is imposed (default 0)
        sampleevery: Number of jumps for each sample (MCMC) (default 25)
        updateproposal: Number of jumps for each update to the proposal density
            std (MCMC) (default 40)
        seed: Seed for pseudo-random number generator
        noard: Turn ARD off on all fibres
        allard: Turn ARD on all fibres
        nospat: Initialize with tensor, not spatially
        nonlinear: Initialize with nonlinear fitting
        cnonlinear: Initialize with constrained nonlinear fitting
        rician: Use Rician noise modelling
        add_f0: Add to the model an unattenuated signal compartment
        ard_f0: Use ARD on F0
        rmean: Set the prior mean for R of model 3 (default: 0.13 - must be
            <0.5)
        rstd: Set the prior standard deviation for R of model 3 (default: 0.03)
        verbose_flag: Switch on diagnostic messages
        help_flag: Display help message
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `XfibresOutputs`).
    """
    runner = runner or get_global_runner()
    if rmean is not None and not (rmean <= 0.5): 
        raise ValueError(f"'rmean' must be less than x <= 0.5 but was {rmean}")
    execution = runner.start_execution(XFIBRES_METADATA)
    cargs = []
    cargs.append("xfibres")
    cargs.extend(["-k", execution.input_file(datafile)])
    cargs.extend(["-m", execution.input_file(maskfile)])
    cargs.extend(["-r", execution.input_file(bvecs)])
    cargs.extend(["-b", execution.input_file(bvals)])
    if logdir is not None:
        cargs.extend(["--ld", logdir])
    if forcedir:
        cargs.append("--forcedir")
    if max_fibres is not None:
        cargs.extend(["--nf", str(max_fibres)])
    if model is not None:
        cargs.extend(["--model", str(model)])
    if fudge is not None:
        cargs.extend(["--fudge", fudge])
    if num_jumps is not None:
        cargs.extend(["--nj", str(num_jumps)])
    if num_burnin is not None:
        cargs.extend(["--bi", str(num_burnin)])
    if burnin_noard is not None:
        cargs.extend(["--bn", str(burnin_noard)])
    if sampleevery is not None:
        cargs.extend(["--se", str(sampleevery)])
    if updateproposal is not None:
        cargs.extend(["--upe", str(updateproposal)])
    if seed is not None:
        cargs.extend(["--seed", seed])
    if noard:
        cargs.append("--noard")
    if allard:
        cargs.append("--allard")
    if nospat:
        cargs.append("--nospat")
    if nonlinear:
        cargs.append("--nonlinear")
    if cnonlinear:
        cargs.append("--cnonlinear")
    if rician:
        cargs.append("--rician")
    if add_f0:
        cargs.append("--f0")
    if ard_f0:
        cargs.append("--ardf0")
    if rmean is not None:
        cargs.extend(["--Rmean", str(rmean)])
    if rstd is not None:
        cargs.extend(["--Rstd", str(rstd)])
    if verbose_flag:
        cargs.append("-V")
    if help_flag:
        cargs.append("-h")
    ret = XfibresOutputs(
        root=execution.output_file("."),
        output_logdir=execution.output_file(f"logdir", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "XFIBRES_METADATA",
    "XfibresOutputs",
    "xfibres",
]