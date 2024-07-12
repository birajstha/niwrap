# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

AFDCONNECTIVITY_METADATA = Metadata(
    id="429f23959d4722a6ab83e4728cf25f38407f7bda",
    name="afdconnectivity",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class AfdconnectivityConfig:
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


class AfdconnectivityOutputs(typing.NamedTuple):
    """
    Output object returned when calling `afdconnectivity(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    afd_map: OutputPathType | None
    """output a 3D image containing the AFD estimated for each voxel. """


def afdconnectivity(
    image: InputPathType,
    tracks: InputPathType,
    wbft: InputPathType | None = None,
    afd_map: str | None = None,
    all_fixels: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[AfdconnectivityConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> AfdconnectivityOutputs:
    """
    afdconnectivity by David Raffelt (david.raffelt@florey.edu.au) and Robert E.
    Smith (robert.smith@florey.edu.au).
    
    Obtain an estimate of fibre connectivity between two regions using AFD and
    streamlines tractography.
    
    This estimate is obtained by determining a fibre volume (AFD) occupied by
    the pathway of interest, and dividing by the streamline length.
    
    If only the streamlines belonging to the pathway of interest are provided,
    then ALL of the fibre volume within each fixel selected will contribute to
    the result. If the -wbft option is used to provide whole-brain
    fibre-tracking (of which the pathway of interest should contain a subset),
    only the fraction of the fibre volume in each fixel estimated to belong to
    the pathway of interest will contribute to the result.
    
    Use -quiet to suppress progress messages and output fibre connectivity value
    only.
    
    For valid comparisons of AFD connectivity across scans, images MUST be
    intensity normalised and bias field corrected, and a common response
    function for all subjects must be used.
    
    Note that the sum of the AFD is normalised by streamline length to account
    for subject differences in fibre bundle length. This normalisation results
    in a measure that is more related to the cross-sectional volume of the tract
    (and therefore 'connectivity'). Note that SIFT-ed tract count is a superior
    measure because it is unaffected by tangential yet unrelated fibres.
    However, AFD connectivity may be used as a substitute when Anatomically
    Constrained Tractography is not possible due to uncorrectable EPI
    distortions, and SIFT may therefore not be as effective.
    
    Longer discussion regarding this command can additionally be found at:
    https://mrtrix.readthedocs.io/en/3.0.4/concepts/afd_connectivity.html (as
    well as in the relevant reference).
    
    References:
    
    Smith, R. E.; Raffelt, D.; Tournier, J.-D.; Connelly, A. Quantitative
    Streamlines Tractography: Methods and Inter-Subject Normalisation. Open
    Science Framework, https://doi.org/10.31219/osf.io/c67kn.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/afdconnectivity.html
    
    Args:
        image: the input FOD image.
        tracks: the input track file defining the bundle of interest.
        wbft: provide a whole-brain fibre-tracking data set (of which the input\
            track file should be a subset), to improve the estimate of fibre bundle\
            volume in the presence of partial volume.
        afd_map: output a 3D image containing the AFD estimated for each voxel.
        all_fixels: if whole-brain fibre-tracking is NOT provided, then if\
            multiple fixels within a voxel are traversed by the pathway of\
            interest, by default the fixel with the greatest streamlines density is\
            selected to contribute to the AFD in that voxel. If this option is\
            provided, then ALL fixels with non-zero streamlines density will\
            contribute to the result, even if multiple fixels per voxel are\
            selected.
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
        NamedTuple of outputs (described in `AfdconnectivityOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(AFDCONNECTIVITY_METADATA)
    cargs = []
    cargs.append("afdconnectivity")
    if wbft is not None:
        cargs.extend(["-wbft", execution.input_file(wbft)])
    if afd_map is not None:
        cargs.extend(["-afd_map", afd_map])
    if all_fixels:
        cargs.append("-all_fixels")
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
    cargs.append(execution.input_file(image))
    cargs.append(execution.input_file(tracks))
    ret = AfdconnectivityOutputs(
        root=execution.output_file("."),
        afd_map=execution.output_file(f"{afd_map}") if afd_map is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "AFDCONNECTIVITY_METADATA",
    "AfdconnectivityConfig",
    "AfdconnectivityOutputs",
    "afdconnectivity",
]
