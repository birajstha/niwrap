# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

TENSOR2METRIC_METADATA = Metadata(
    id="97ac6caa4e40a551fdd4a0175886b4557265bd4e",
    name="tensor2metric",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Tensor2metricConfig:
    """
    temporarily set the value of an MRtrix config file entry.
    """
    key: str
    """temporarily set the value of an MRtrix config file entry."""
    value_: str
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
        cargs.append(self.value_)
        return cargs


class Tensor2metricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tensor2metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    adc: OutputPathType | None
    """compute the mean apparent diffusion coefficient (ADC) of the diffusion tensor. (sometimes also referred to as the mean diffusivity (MD)) """
    fa: OutputPathType | None
    """compute the fractional anisotropy (FA) of the diffusion tensor. """
    ad: OutputPathType | None
    """compute the axial diffusivity (AD) of the diffusion tensor. (equivalent to the principal eigenvalue) """
    rd: OutputPathType | None
    """compute the radial diffusivity (RD) of the diffusion tensor. (equivalent to the mean of the two non-principal eigenvalues) """
    cl: OutputPathType | None
    """compute the linearity metric of the diffusion tensor. (one of the three Westin shape metrics) """
    cp: OutputPathType | None
    """compute the planarity metric of the diffusion tensor. (one of the three Westin shape metrics) """
    cs: OutputPathType | None
    """compute the sphericity metric of the diffusion tensor. (one of the three Westin shape metrics) """
    value: OutputPathType | None
    """compute the selected eigenvalue(s) of the diffusion tensor. """
    vector: OutputPathType | None
    """compute the selected eigenvector(s) of the diffusion tensor. """


def tensor2metric(
    tensor: InputPathType,
    adc: InputPathType | None = None,
    fa: InputPathType | None = None,
    ad: InputPathType | None = None,
    rd: InputPathType | None = None,
    cl: InputPathType | None = None,
    cp: InputPathType | None = None,
    cs: InputPathType | None = None,
    value: InputPathType | None = None,
    vector: InputPathType | None = None,
    num: list[int] = None,
    modulate: typing.Literal["choice"] | None = None,
    mask: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Tensor2metricConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Tensor2metricOutputs:
    """
    tensor2metric by Thijs Dhollander (thijs.dhollander@gmail.com) & Ben Jeurissen
    (ben.jeurissen@uantwerpen.be) & J-Donald Tournier (jdtournier@gmail.com).
    
    Generate maps of tensor-derived parameters.
    
    
    
    References:
    
    Basser, P. J.; Mattiello, J. & Lebihan, D. MR diffusion tensor spectroscopy
    and imaging. Biophysical Journal, 1994, 66, 259-267
    
    Westin, C. F.; Peled, S.; Gudbjartsson, H.; Kikinis, R. & Jolesz, F. A.
    Geometrical diffusion measures for MRI from tensor basis analysis. Proc Intl
    Soc Mag Reson Med, 1997, 5, 1742.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/tensor2metric.html
    
    Args:
        tensor: the input tensor image.
        adc: compute the mean apparent diffusion coefficient (ADC) of the\
            diffusion tensor. (sometimes also referred to as the mean diffusivity\
            (MD)).
        fa: compute the fractional anisotropy (FA) of the diffusion tensor.
        ad: compute the axial diffusivity (AD) of the diffusion tensor.\
            (equivalent to the principal eigenvalue).
        rd: compute the radial diffusivity (RD) of the diffusion tensor.\
            (equivalent to the mean of the two non-principal eigenvalues).
        cl: compute the linearity metric of the diffusion tensor. (one of the\
            three Westin shape metrics).
        cp: compute the planarity metric of the diffusion tensor. (one of the\
            three Westin shape metrics).
        cs: compute the sphericity metric of the diffusion tensor. (one of the\
            three Westin shape metrics).
        value: compute the selected eigenvalue(s) of the diffusion tensor.
        vector: compute the selected eigenvector(s) of the diffusion tensor.
        num: specify the desired eigenvalue/eigenvector(s). Note that several\
            eigenvalues can be specified as a number sequence. For example, '1,3'\
            specifies the principal (1) and minor (3) eigenvalues/eigenvectors\
            (default = 1).
        modulate: specify how to modulate the magnitude of the eigenvectors.\
            Valid choices are: none, FA, eigval (default = FA).
        mask: only perform computation within the specified binary brain mask\
            image.
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
        NamedTuple of outputs (described in `Tensor2metricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TENSOR2METRIC_METADATA)
    cargs = []
    cargs.append("tensor2metric")
    if adc is not None:
        cargs.extend(["-adc", execution.input_file(adc)])
    if fa is not None:
        cargs.extend(["-fa", execution.input_file(fa)])
    if ad is not None:
        cargs.extend(["-ad", execution.input_file(ad)])
    if rd is not None:
        cargs.extend(["-rd", execution.input_file(rd)])
    if cl is not None:
        cargs.extend(["-cl", execution.input_file(cl)])
    if cp is not None:
        cargs.extend(["-cp", execution.input_file(cp)])
    if cs is not None:
        cargs.extend(["-cs", execution.input_file(cs)])
    if value is not None:
        cargs.extend(["-value", execution.input_file(value)])
    if vector is not None:
        cargs.extend(["-vector", execution.input_file(vector)])
    if num is not None:
        cargs.extend(["-num", *map(str, num)])
    if modulate is not None:
        cargs.extend(["-modulate", modulate])
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
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
    cargs.append(execution.input_file(tensor))
    ret = Tensor2metricOutputs(
        root=execution.output_file("."),
        adc=execution.output_file(f"{pathlib.Path(adc).name}") if adc is not None else None,
        fa=execution.output_file(f"{pathlib.Path(fa).name}") if fa is not None else None,
        ad=execution.output_file(f"{pathlib.Path(ad).name}") if ad is not None else None,
        rd=execution.output_file(f"{pathlib.Path(rd).name}") if rd is not None else None,
        cl=execution.output_file(f"{pathlib.Path(cl).name}") if cl is not None else None,
        cp=execution.output_file(f"{pathlib.Path(cp).name}") if cp is not None else None,
        cs=execution.output_file(f"{pathlib.Path(cs).name}") if cs is not None else None,
        value=execution.output_file(f"{pathlib.Path(value).name}") if value is not None else None,
        vector=execution.output_file(f"{pathlib.Path(vector).name}") if vector is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TENSOR2METRIC_METADATA",
    "Tensor2metricConfig",
    "Tensor2metricOutputs",
    "tensor2metric",
]
