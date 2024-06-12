# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

MTNORMALISE_METADATA = Metadata(
    id="cd3ae6497f3cf8d45319da581cf911bc038953a1",
    name="mtnormalise",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class MtnormaliseConfig:
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
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        cargs.append("-config")
        cargs.append(self.key)
        cargs.append(self.value)
        return cargs


class MtnormaliseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `mtnormalise(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    check_norm: OutputPathType | None
    """output the final estimated spatially varying intensity level that is used for normalisation. """
    check_mask: OutputPathType | None
    """output the final mask used to compute the normalisation. This mask excludes regions identified as outliers by the optimisation process. """
    check_factors: OutputPathType | None
    """output the tissue balance factors computed during normalisation. """


def mtnormalise(
    input_output: list[str],
    mask: InputPathType,
    order: typing.Literal["number"] | None = None,
    niter: list[int] = None,
    reference: float | int | None = None,
    balanced: bool = False,
    check_norm: InputPathType | None = None,
    check_mask: InputPathType | None = None,
    check_factors: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[MtnormaliseConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> MtnormaliseOutputs:
    """
    mtnormalise by Thijs Dhollander (thijs.dhollander@gmail.com), Rami Tabbara
    (rami.tabbara@florey.edu.au), David Raffelt (david.raffelt@florey.edu.au), Jonas
    Rosnarho-Tornstrand (jonas.rosnarho-tornstrand@kcl.ac.uk) and J-Donald Tournier
    (jdtournier@gmail.com).
    
    Multi-tissue informed log-domain intensity normalisation.
    
    This command takes as input any number of tissue components (e.g. from
    multi-tissue CSD) and outputs corresponding normalised tissue components
    corrected for the effects of (residual) intensity inhomogeneities. Intensity
    normalisation is performed by optimising the voxel-wise sum of all tissue
    compartments towards a constant value, under constraints of spatial
    smoothness (polynomial basis of a given order). Different to the Raffelt et
    al. 2017 abstract, this algorithm performs this task in the log-domain
    instead, with added gradual outlier rejection, different handling of the
    balancing factors between tissue compartments and a different iteration
    structure.
    
    The -mask option is mandatory and is optimally provided with a brain mask
    (such as the one obtained from dwi2mask earlier in the processing pipeline).
    Outlier areas with exceptionally low or high combined tissue contributions
    are accounted for and reoptimised as the intensity inhomogeneity estimation
    becomes more accurate.
    
    References:
    
    Raffelt, D.; Dhollander, T.; Tournier, J.-D.; Tabbara, R.; Smith, R. E.;
    Pierre, E. & Connelly, A. Bias Field Correction and Intensity Normalisation
    for Quantitative Analysis of Apparent Fibre Density. In Proc. ISMRM, 2017,
    26, 3541
    
    Dhollander, T.; Tabbara, R.; Rosnarho-Tornstrand, J.; Tournier, J.-D.;
    Raffelt, D. & Connelly, A. Multi-tissue log-domain intensity and
    inhomogeneity normalisation for quantitative apparent fibre density. In
    Proc. ISMRM, 2021, 29, 2472.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/mtnormalise.html
    
    Args:
        input_output: list of all input and output tissue compartment files\
            (see example usage).
        mask: the mask defines the data used to compute the intensity\
            normalisation. This option is mandatory.
        order: the maximum order of the polynomial basis used to fit the\
            normalisation field in the log-domain. An order of 0 is equivalent to\
            not allowing spatial variance of the intensity normalisation factor.\
            (default: 3).
        niter: set the number of iterations. The first (and potentially only)\
            entry applies to the main loop. If supplied as a comma-separated list\
            of integers, the second entry applies to the inner loop to update the\
            balance factors (default: 15,7).
        reference: specify the (positive) reference value to which the summed\
            tissue compartments will be normalised. (default: 0.282095, SH DC term\
            for unit angular integral).
        balanced: incorporate the per-tissue balancing factors into scaling of\
            the output images (NOTE: use of this option has critical consequences\
            for AFD intensity normalisation; should not be used unless these\
            consequences are fully understood).
        check_norm: output the final estimated spatially varying intensity\
            level that is used for normalisation.
        check_mask: output the final mask used to compute the normalisation.\
            This mask excludes regions identified as outliers by the optimisation\
            process.
        check_factors: output the tissue balance factors computed during\
            normalisation.
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
        NamedTuple of outputs (described in `MtnormaliseOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MTNORMALISE_METADATA)
    cargs = []
    cargs.append("mtnormalise")
    cargs.extend(["-mask", execution.input_file(mask)])
    if order is not None:
        cargs.extend(["-order", order])
    if niter is not None:
        cargs.extend(["-niter", *map(str, niter)])
    if reference is not None:
        cargs.extend(["-reference", str(reference)])
    if balanced:
        cargs.append("-balanced")
    if check_norm is not None:
        cargs.extend(["-check_norm", execution.input_file(check_norm)])
    if check_mask is not None:
        cargs.extend(["-check_mask", execution.input_file(check_mask)])
    if check_factors is not None:
        cargs.extend(["-check_factors", execution.input_file(check_factors)])
    if info:
        cargs.append("-info")
    if quiet:
        cargs.append("-quiet")
    if debug:
        cargs.append("-debug")
    if force:
        cargs.append("-force")
    if nthreads is not None:
        cargs.extend(["-nthreads", str(nthreads)])
    if config is not None:
        cargs.extend([a for c in [s.run(execution) for s in config] for a in c])
    if help_:
        cargs.append("-help")
    if version:
        cargs.append("-version")
    cargs.extend(input_output)
    ret = MtnormaliseOutputs(
        root=execution.output_file("."),
        check_norm=execution.output_file(f"{pathlib.Path(check_norm).name}") if check_norm is not None else None,
        check_mask=execution.output_file(f"{pathlib.Path(check_mask).name}") if check_mask is not None else None,
        check_factors=execution.output_file(f"{pathlib.Path(check_factors).name}") if check_factors is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MTNORMALISE_METADATA",
    "MtnormaliseConfig",
    "MtnormaliseOutputs",
    "mtnormalise",
]
