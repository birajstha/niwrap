# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

WARP2METRIC_METADATA = Metadata(
    id="2fd5850bcb7f32a9c9c10cc3635b0b1b82152cda",
    name="warp2metric",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Warp2metricFc:
    """
    use an input template fixel image to define fibre orientations and output a fixel image describing the change in fibre cross-section (FC) in the perpendicular plane to the fixel orientation. e.g. warp2metric warp.mif -fc fixel_template_directory output_fixel_directory fc.mif
    """
    template_fixel_directory: InputPathType
    """use an input template fixel image to define fibre orientations and output
    a fixel image describing the change in fibre cross-section (FC) in the
    perpendicular plane to the fixel orientation. e.g. warp2metric warp.mif -fc
    fixel_template_directory output_fixel_directory fc.mif"""
    output_fixel_directory: str
    """use an input template fixel image to define fibre orientations and output
    a fixel image describing the change in fibre cross-section (FC) in the
    perpendicular plane to the fixel orientation. e.g. warp2metric warp.mif -fc
    fixel_template_directory output_fixel_directory fc.mif"""
    output_fixel_data: str
    """use an input template fixel image to define fibre orientations and output
    a fixel image describing the change in fibre cross-section (FC) in the
    perpendicular plane to the fixel orientation. e.g. warp2metric warp.mif -fc
    fixel_template_directory output_fixel_directory fc.mif"""
    
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
        cargs.append("-fc")
        cargs.append(execution.input_file(self.template_fixel_directory))
        cargs.append(self.output_fixel_directory)
        cargs.append(self.output_fixel_data)
        return cargs


@dataclasses.dataclass
class Warp2metricConfig:
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


class Warp2metricOutputs(typing.NamedTuple):
    """
    Output object returned when calling `warp2metric(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    jmat: OutputPathType | None
    """output a Jacobian matrix image stored in column-major order along the 4th dimension.Note the output jacobian describes the warp gradient w.r.t the scanner space coordinate system """
    jdet: OutputPathType | None
    """output the Jacobian determinant instead of the full matrix """


def warp2metric(
    in_: InputPathType,
    fc: Warp2metricFc | None = None,
    jmat: str | None = None,
    jdet: str | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Warp2metricConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> Warp2metricOutputs:
    """
    warp2metric by David Raffelt (david.raffelt@florey.edu.au).
    
    Compute fixel-wise or voxel-wise metrics from a 4D deformation field.
    
    
    
    References:
    
    Raffelt, D.; Tournier, JD/; Smith, RE.; Vaughan, DN.; Jackson, G.; Ridgway,
    GR. Connelly, A.Investigating White Matter Fibre Density and Morphology
    using Fixel-Based Analysis. Neuroimage, 2017, 144, 58-73, doi:
    10.1016/j.neuroimage.2016.09.029.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/warp2metric.html
    
    Args:
        in_: the input deformation field.
        fc: use an input template fixel image to define fibre orientations and\
            output a fixel image describing the change in fibre cross-section (FC)\
            in the perpendicular plane to the fixel orientation. e.g. warp2metric\
            warp.mif -fc fixel_template_directory output_fixel_directory fc.mif.
        jmat: output a Jacobian matrix image stored in column-major order along\
            the 4th dimension.Note the output jacobian describes the warp gradient\
            w.r.t the scanner space coordinate system.
        jdet: output the Jacobian determinant instead of the full matrix.
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
        NamedTuple of outputs (described in `Warp2metricOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WARP2METRIC_METADATA)
    cargs = []
    cargs.append("warp2metric")
    if fc is not None:
        cargs.extend(fc.run(execution))
    if jmat is not None:
        cargs.extend(["-jmat", jmat])
    if jdet is not None:
        cargs.extend(["-jdet", jdet])
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
    cargs.append(execution.input_file(in_))
    ret = Warp2metricOutputs(
        root=execution.output_file("."),
        jmat=execution.output_file(f"{jmat}") if jmat is not None else None,
        jdet=execution.output_file(f"{jdet}") if jdet is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WARP2METRIC_METADATA",
    "Warp2metricConfig",
    "Warp2metricFc",
    "Warp2metricOutputs",
    "warp2metric",
]
