# This file was auto generated by Styx.
# Do not edit this file directly.

import dataclasses
import pathlib
import typing

from styxdefs import *


CONNECTOMESTATS_METADATA = Metadata(
    id="4f12433fa5e94d6b73db3e3d93dbf7e89441971b",
    name="connectomestats",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


class ColumnOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Column.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Column:
    """
    add a column to the design matrix corresponding to subject edge-wise values (note that the contrast matrix must include an additional column for each use of this option); the text file provided via this option should contain a file name for each subject
    """
    path: InputPathType
    """add a column to the design matrix corresponding to subject edge-wise
    values (note that the contrast matrix must include an additional column for
    each use of this option); the text file provided via this option should
    contain a file name for each subject"""
    
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
        cargs.append("-column")
        cargs.append(execution.input_file(self.path))
        return cargs
    
    def outputs(
        self,
        execution: Execution,
    ) -> ColumnOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ColumnOutputs`).
        """
        ret = ColumnOutputs(
            root=execution.output_file("."),
        )
        return ret


class ConfigOutputs(typing.NamedTuple):
    """
    Output object returned when calling `Config.run(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


@dataclasses.dataclass
class Config:
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
    
    def outputs(
        self,
        execution: Execution,
    ) -> ConfigOutputs:
        """
        Collect output file paths.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            NamedTuple of outputs (described in `ConfigOutputs`).
        """
        ret = ConfigOutputs(
            root=execution.output_file("."),
        )
        return ret


class ConnectomestatsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `connectomestats(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    column: ColumnOutputs
    """Subcommand outputs"""
    config: ConfigOutputs
    """Subcommand outputs"""


def connectomestats(
    input_: InputPathType,
    algorithm: typing.Literal["algorithm"],
    design: InputPathType,
    contrast: InputPathType,
    output: str,
    notest: bool = False,
    errors: typing.Literal["spec"] | None = None,
    exchange_within: InputPathType | None = None,
    exchange_whole: InputPathType | None = None,
    strong: bool = False,
    nshuffles: int | None = None,
    permutations: InputPathType | None = None,
    nonstationarity: bool = False,
    skew_nonstationarity: float | int | None = None,
    nshuffles_nonstationarity: int | None = None,
    permutations_nonstationarity: InputPathType | None = None,
    tfce_dh: float | int | None = None,
    tfce_e: float | int | None = None,
    tfce_h: float | int | None = None,
    variance: InputPathType | None = None,
    ftests: InputPathType | None = None,
    fonly: bool = False,
    column: list[Column] = None,
    threshold: float | int | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Config] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> ConnectomestatsOutputs:
    """
    connectomestats by Robert E. Smith (robert.smith@florey.edu.au).
    
    Connectome group-wise statistics at the edge level using non-parametric
    permutation testing.
    
    For the TFNBS algorithm, default parameters for statistical enhancement have
    been set based on the work in:
    Vinokur, L.; Zalesky, A.; Raffelt, D.; Smith, R.E. & Connelly, A. A Novel
    Threshold-Free Network-Based Statistics Method: Demonstration using
    Simulated Pathology. OHBM, 2015, 4144;
    and:
    Vinokur, L.; Zalesky, A.; Raffelt, D.; Smith, R.E. & Connelly, A. A novel
    threshold-free network-based statistical method: Demonstration and parameter
    optimisation using in vivo simulated pathology. In Proc ISMRM, 2015, 2846.
    Note however that not only was the optimisation of these parameters not very
    precise, but the outcomes of statistical inference (for both this algorithm
    and the NBS method) can vary markedly for even small changes to enhancement
    parameters. Therefore the specificity of results obtained using either of
    these methods should be interpreted with caution.
    
    In some software packages, a column of ones is automatically added to the
    GLM design matrix; the purpose of this column is to estimate the "global
    intercept", which is the predicted value of the observed variable if all
    explanatory variables were to be zero. However there are rare situations
    where including such a column would not be appropriate for a particular
    experimental design. Hence, in MRtrix3 statistical inference commands, it is
    up to the user to determine whether or not this column of ones should be
    included in their design matrix, and add it explicitly if necessary. The
    contrast matrix must also reflect the presence of this additional column.
    
    References:
    
    * If using the NBS algorithm:
    Zalesky, A.; Fornito, A. & Bullmore, E. T. Network-based statistic:
    Identifying differences in brain networks.
    NeuroImage, 2010, 53, 1197-1207
    
    * If using the TFNBS algorithm:
    Baggio, H.C.; Abos, A.; Segura, B.; Campabadal, A.; Garcia-Diaz, A.; Uribe,
    C.; Compta, Y.; Marti, M.J.; Valldeoriola, F.; Junque, C. Statistical
    inference in brain graphs using threshold-free network-based statistics.HBM,
    2018, 39, 2289-2302
    
    * If using the -nonstationary option:
    Salimi-Khorshidi, G.; Smith, S.M. & Nichols, T.E. Adjusting the effect of
    nonstationarity in cluster-based and TFCE inference.
    Neuroimage, 2011, 54(3), 2006-19.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/connectomestats.html
    
    Args:
        input_: a text file listing the file names of the input connectomes
        algorithm: the algorithm to use in network-based clustering/enhancement.
            Options are: nbs, tfnbs, none
        design: the design matrix
        contrast: the contrast matrix
        output: the filename prefix for all output.
        notest: don't perform statistical inference; only output population
            statistics (effect size, stdev etc)
        errors: specify nature of errors for shuffling; options are: ee,ise,both
            (default: ee)
        exchange_within: specify blocks of observations within each of which
            data may undergo restricted exchange
        exchange_whole: specify blocks of observations that may be exchanged
            with one another (for independent and symmetric errors, sign-flipping
            will occur block-wise)
        strong: use strong familywise error control across multiple hypotheses
        nshuffles: the number of shuffles (default: 5000)
        permutations: manually define the permutations (relabelling). The input
            should be a text file defining a m x n matrix, where each relabelling is
            defined as a column vector of size m, and the number of columns, n,
            defines the number of permutations. Can be generated with the
            palm_quickperms function in PALM
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM). Overrides the -nshuffles
            option.
        nonstationarity: perform non-stationarity correction
        skew_nonstationarity: specify the skew parameter for empirical statistic
            calculation (default for this command is 1)
        nshuffles_nonstationarity: the number of shuffles to use when
            precomputing the empirical statistic image for non-stationarity
            correction (default: 5000)
        permutations_nonstationarity: manually define the permutations
            (relabelling) for computing the emprical statistics for non-stationarity
            correction. The input should be a text file defining a m x n matrix,
            where each relabelling is defined as a column vector of size m, and the
            number of columns, n, defines the number of permutations. Can be
            generated with the palm_quickperms function in PALM
            (http://fsl.fmrib.ox.ac.uk/fsl/fslwiki/PALM) Overrides the
            -nshuffles_nonstationarity option.
        tfce_dh: the height increment used in the tfce integration (default:
            0.1)
        tfce_e: tfce extent exponent (default: 0.4)
        tfce_h: tfce height exponent (default: 3)
        variance: define variance groups for the G-statistic; measurements for
            which the expected variance is equivalent should contain the same index
        ftests: perform F-tests; input text file should contain, for each
            F-test, a row containing ones and zeros, where ones indicate the rows of
            the contrast matrix to be included in the F-test.
        fonly: only assess F-tests; do not perform statistical inference on
            entries in the contrast matrix
        column: add a column to the design matrix corresponding to subject
            edge-wise values (note that the contrast matrix must include an
            additional column for each use of this option); the text file provided
            via this option should contain a file name for each subject
        threshold: the t-statistic value to use in threshold-based clustering
            algorithms
        info: display information messages.
        quiet: do not display information messages or progress status;
            alternatively, this can be achieved by setting the MRTRIX_QUIET
            environment variable to a non-empty string.
        debug: display debugging messages.
        force: force overwrite of output files (caution: using the same file as
            input and output might cause unexpected behaviour).
        nthreads: use this number of threads in multi-threaded applications (set
            to 0 to disable multi-threading).
        config: temporarily set the value of an MRtrix config file entry.
        help_: display this information page and exit.
        version: display version information and exit.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ConnectomestatsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(CONNECTOMESTATS_METADATA)
    cargs = []
    cargs.append("connectomestats")
    if notest:
        cargs.append("-notest")
    if errors is not None:
        cargs.extend(["-errors", errors])
    if exchange_within is not None:
        cargs.extend(["-exchange_within", execution.input_file(exchange_within)])
    if exchange_whole is not None:
        cargs.extend(["-exchange_whole", execution.input_file(exchange_whole)])
    if strong:
        cargs.append("-strong")
    if nshuffles is not None:
        cargs.extend(["-nshuffles", str(nshuffles)])
    if permutations is not None:
        cargs.extend(["-permutations", execution.input_file(permutations)])
    if nonstationarity:
        cargs.append("-nonstationarity")
    if skew_nonstationarity is not None:
        cargs.extend(["-skew_nonstationarity", str(skew_nonstationarity)])
    if nshuffles_nonstationarity is not None:
        cargs.extend(["-nshuffles_nonstationarity", str(nshuffles_nonstationarity)])
    if permutations_nonstationarity is not None:
        cargs.extend(["-permutations_nonstationarity", execution.input_file(permutations_nonstationarity)])
    if tfce_dh is not None:
        cargs.extend(["-tfce_dh", str(tfce_dh)])
    if tfce_e is not None:
        cargs.extend(["-tfce_e", str(tfce_e)])
    if tfce_h is not None:
        cargs.extend(["-tfce_h", str(tfce_h)])
    if variance is not None:
        cargs.extend(["-variance", execution.input_file(variance)])
    if ftests is not None:
        cargs.extend(["-ftests", execution.input_file(ftests)])
    if fonly:
        cargs.append("-fonly")
    if column is not None:
        cargs.extend([a for c in [s.run(execution) for s in column] for a in c])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
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
    cargs.append(execution.input_file(input_))
    cargs.append(algorithm)
    cargs.append(execution.input_file(design))
    cargs.append(execution.input_file(contrast))
    cargs.append(output)
    ret = ConnectomestatsOutputs(
        root=execution.output_file("."),
        column=[column.outputs(execution) for column in column],
        config=[config.outputs(execution) for config in config],
    )
    execution.run(cargs)
    return ret


__all__ = [
    "CONNECTOMESTATS_METADATA",
    "Column",
    "ColumnOutputs",
    "Config",
    "ConfigOutputs",
    "ConnectomestatsOutputs",
    "connectomestats",
]
