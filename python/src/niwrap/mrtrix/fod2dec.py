# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import dataclasses
import pathlib
import typing

FOD2DEC_METADATA = Metadata(
    id="aac2ac1ce7621d3fce08d22d3e9b29354906d5f9",
    name="fod2dec",
    container_image_type="docker",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class Fod2decConfig:
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


class Fod2decOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fod2dec(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """The output DEC image (weighted RGB triplets)."""


def fod2dec(
    input_: InputPathType,
    output: str,
    mask: InputPathType | None = None,
    contrast: InputPathType | None = None,
    lum: bool = False,
    lum_coefs: list[float | int] = None,
    lum_gamma: float | int | None = None,
    threshold: float | int | None = None,
    no_weight: bool = False,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[Fod2decConfig] = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner = None,
) -> Fod2decOutputs:
    """
    fod2dec by Thijs Dhollander (thijs.dhollander@gmail.com).
    
    Generate FOD-based DEC maps, with optional panchromatic sharpening and/or
    luminance/perception correction.
    
    By default, the FOD-based DEC is weighted by the integral of the FOD. To
    weight by another scalar map, use the -contrast option. This option can also
    be used for panchromatic sharpening, e.g., by supplying a T1 (or other
    sensible) anatomical volume with a higher spatial resolution.
    
    References:
    
    Dhollander T, Smith RE, Tournier JD, Jeurissen B, Connelly A. Time to move
    on: an FOD-based DEC map to replace DTI's trademark DEC FA. Proc Intl Soc
    Mag Reson Med, 2015, 23, 1027
    
    Dhollander T, Raffelt D, Smith RE, Connelly A. Panchromatic sharpening of
    FOD-based DEC maps by structural T1 information. Proc Intl Soc Mag Reson
    Med, 2015, 23, 566.
    
    More information:
    https://mrtrix.readthedocs.io/en/latest/reference/commands/fod2dec.html
    
    Args:
        input_: The input FOD image (spherical harmonic coefficients).
        output: The output DEC image (weighted RGB triplets).
        mask: Only perform DEC computation within the specified mask image.
        contrast: Weight the computed DEC map by the provided image contrast.\
            If the contrast has a different image grid, the DEC map is first\
            resliced and renormalised. To achieve panchromatic sharpening, provide\
            an image with a higher spatial resolution than the input FOD image;\
            e.g., a T1 anatomical volume. Only the DEC is subject to the mask, so\
            as to allow for partial colouring of the contrast image.\
            Default when this option is *not* provided: integral of input FOD,\
            subject to the same mask/threshold as used for DEC computation.
        lum: Correct for luminance/perception, using default values Cr,Cg,Cb =\
            0.3,0.5,0.2 and gamma = 2.2 (*not* correcting is the theoretical\
            equivalent of Cr,Cg,Cb = 1,1,1 and gamma = 2).
        lum_coefs: The coefficients Cr,Cg,Cb to correct for\
            luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default gamma = 2.2 unless specified otherwise.
        lum_gamma: The gamma value to correct for luminance/perception.\
            Note: this implicitly switches on luminance/perception correction,\
            using a default Cr,Cg,Cb = 0.3,0.5,0.2 unless specified otherwise.
        threshold: FOD amplitudes below the threshold value are considered\
            zero.
        no_weight: Do not weight the DEC map; just output the unweighted\
            colours. Reslicing and renormalising of colours will still happen when\
            providing the -contrast option as a template.
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
        NamedTuple of outputs (described in `Fod2decOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FOD2DEC_METADATA)
    cargs = []
    cargs.append("fod2dec")
    if mask is not None:
        cargs.extend(["-mask", execution.input_file(mask)])
    if contrast is not None:
        cargs.extend(["-contrast", execution.input_file(contrast)])
    if lum:
        cargs.append("-lum")
    if lum_coefs is not None:
        cargs.extend(["-lum_coefs", *map(str, lum_coefs)])
    if lum_gamma is not None:
        cargs.extend(["-lum_gamma", str(lum_gamma)])
    if threshold is not None:
        cargs.extend(["-threshold", str(threshold)])
    if no_weight:
        cargs.append("-no_weight")
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
    cargs.append(output)
    ret = Fod2decOutputs(
        root=execution.output_file("."),
        output=execution.output_file(f"{output}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FOD2DEC_METADATA",
    "Fod2decConfig",
    "Fod2decOutputs",
    "fod2dec",
]
