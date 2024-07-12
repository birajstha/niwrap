# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PROBTRACKX_METADATA = Metadata(
    id="837c0df452b7a5504fb600df04336642a9bdf6f2",
    name="probtrackx",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class ProbtrackxOutputs(typing.NamedTuple):
    """
    Output object returned when calling `probtrackx(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def probtrackx(
    samples: InputPathType,
    mask: InputPathType,
    seed: InputPathType,
    out: str = "fdt_paths",
    verbose: int | None = None,
    targetmasks: InputPathType | None = None,
    mask2: InputPathType | None = None,
    waypoints: InputPathType | None = None,
    network: bool = False,
    mesh: InputPathType | None = None,
    seedref: InputPathType | None = None,
    dir_: str | None = "logdir",
    forcedir: bool = False,
    opd: bool = False,
    pd: bool = False,
    os2t: bool = False,
    avoid: InputPathType | None = None,
    stop: InputPathType | None = None,
    xfm: InputPathType | None = None,
    invxfm: InputPathType | None = None,
    nsamples: int | None = 5000,
    nsteps: int | None = 2000,
    distthresh: float | int | None = 0,
    cthr: float | int | None = 0.2,
    fibthresh: float | int | None = 0.01,
    sampvox: bool = False,
    steplength: float | int | None = 0.5,
    loopcheck: bool = False,
    usef: bool = False,
    randfib: int | None = 0,
    fibst: int | None = 1,
    modeuler: bool = False,
    rseed: int | None = None,
    s2tastext: bool = False,
    runner: Runner | None = None,
) -> ProbtrackxOutputs:
    """
    probtrackx by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    Streamlines tracking algorithm for probabilistic tractography.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FDT
    
    Args:
        samples: Basename for samples files.
        mask: Bet binary mask file in diffusion space.
        seed: Seed volume, or voxel, or ascii file with multiple volumes, or\
            freesurfer label file.
        out: Output file (default='fdt_paths').
        verbose: Verbose level, [0-2].
        targetmasks: File containing a list of target masks - required for\
            seeds_to_targets classification.
        mask2: Second mask in twomask_symm mode.
        waypoints: Waypoint mask or ascii list of waypoint masks - only keep\
            paths going through ALL the masks.
        network: Activate network mode - only keep paths going through at least\
            one seed mask (required if multiple seed masks).
        mesh: Freesurfer-type surface descriptor (in ascii format).
        seedref: Reference vol to define seed space in simple mode - diffusion\
            space assumed if absent.
        dir_: Directory to put the final volumes in - code makes this directory\
            - default='logdir'.
        forcedir: Use the actual directory name given - i.e. don't add + to\
            make a new directory.
        opd: Output path distribution.
        pd: Correct path distribution for the length of the pathways.
        os2t: Output seeds to targets.
        avoid: Reject pathways passing through locations given by this mask.
        stop: Stop tracking at locations given by this mask file.
        xfm: Transform taking seed space to DTI space (either FLIRT matrix or\
            FNIRT warpfield) - default is identity.
        invxfm: Transform taking DTI space to seed space (compulsory when using\
            a warpfield for seeds_to_dti).
        nsamples: Number of samples - default=5000.
        nsteps: Number of steps per sample - default=2000.
        distthresh: Discards samples shorter than this threshold (in mm -\
            default=0).
        cthr: Curvature threshold - default=0.2.
        fibthresh: Volume fraction before subsidary fibre orientations are\
            considered - default=0.01.
        sampvox: Sample random points within seed voxels.
        steplength: Steplength in mm - default=0.5.
        loopcheck: Perform loopchecks on paths - slower, but allows lower\
            curvature threshold.
        usef: Use anisotropy to constrain tracking.
        randfib: Default 0. Set to 1 to randomly sample initial fibres (with f\
            > fibthresh). Set to 2 to sample in proportion fibres (with\
            f>fibthresh) to f. Set to 3 to sample ALL populations at random (even\
            if f<fibthresh).
        fibst: Force a starting fibre for tracking - default=1, i.e. first\
            fibre orientation. Only works if randfib==0.
        modeuler: Use modified euler streamlining.
        rseed: Random seed.
        s2tastext: Output seed-to-target counts as a text file (useful when\
            seeding from a mesh).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `ProbtrackxOutputs`).
    """
    runner = runner or get_global_runner()
    if verbose is not None and not (0 <= verbose <= 2): 
        raise ValueError(f"'verbose' must be between 0 <= x <= 2 but was {verbose}")
    execution = runner.start_execution(PROBTRACKX_METADATA)
    cargs = []
    cargs.append("probtrackx")
    cargs.extend(["-s", execution.input_file(samples)])
    cargs.extend(["-m", execution.input_file(mask)])
    cargs.extend(["-x", execution.input_file(seed)])
    cargs.extend(["-o", out])
    if verbose is not None:
        cargs.extend(["--verbose", str(verbose)])
    if targetmasks is not None:
        cargs.extend(["--targetmasks", execution.input_file(targetmasks)])
    if mask2 is not None:
        cargs.extend(["--mask2", execution.input_file(mask2)])
    if waypoints is not None:
        cargs.extend(["--waypoints", execution.input_file(waypoints)])
    if network:
        cargs.append("--network")
    if mesh is not None:
        cargs.extend(["--mesh", execution.input_file(mesh)])
    if seedref is not None:
        cargs.extend(["--seedref", execution.input_file(seedref)])
    if dir_ is not None:
        cargs.extend(["--dir", dir_])
    if forcedir:
        cargs.append("--forcedir")
    if opd:
        cargs.append("--opd")
    if pd:
        cargs.append("--pd")
    if os2t:
        cargs.append("--os2t")
    if avoid is not None:
        cargs.extend(["--avoid", execution.input_file(avoid)])
    if stop is not None:
        cargs.extend(["--stop", execution.input_file(stop)])
    if xfm is not None:
        cargs.extend(["--xfm", execution.input_file(xfm)])
    if invxfm is not None:
        cargs.extend(["--invxfm", execution.input_file(invxfm)])
    if nsamples is not None:
        cargs.extend(["-P", str(nsamples)])
    if nsteps is not None:
        cargs.extend(["-S", str(nsteps)])
    if distthresh is not None:
        cargs.extend(["--distthresh", str(distthresh)])
    if cthr is not None:
        cargs.extend(["-c", str(cthr)])
    if fibthresh is not None:
        cargs.extend(["--fibthresh", str(fibthresh)])
    if sampvox:
        cargs.append("--sampvox")
    if steplength is not None:
        cargs.extend(["--steplength", str(steplength)])
    if loopcheck:
        cargs.append("-l")
    if usef:
        cargs.append("-f")
    if randfib is not None:
        cargs.extend(["--randfib", str(randfib)])
    if fibst is not None:
        cargs.extend(["--fibst", str(fibst)])
    if modeuler:
        cargs.append("--modeuler")
    if rseed is not None:
        cargs.extend(["--rseed", str(rseed)])
    if s2tastext:
        cargs.append("--s2tastext")
    ret = ProbtrackxOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PROBTRACKX_METADATA",
    "ProbtrackxOutputs",
    "probtrackx",
]
