# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

TCKMAP_METADATA = Metadata(
    id="20fc0eb1cf1e5881a0131f8a9755f1e2d22946f9.boutiques",
    name="tckmap",
    package="mrtrix",
    container_image_tag="mrtrix3/mrtrix3:3.0.4",
)


@dataclasses.dataclass
class TckmapVariousString:
    obj: str
    """String object."""
    
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
        cargs.append(self.obj)
        return cargs


@dataclasses.dataclass
class TckmapVariousFile:
    obj: InputPathType
    """File object."""
    
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
        cargs.append(execution.input_file(self.obj))
        return cargs


@dataclasses.dataclass
class TckmapConfig:
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


class TckmapOutputs(typing.NamedTuple):
    """
    Output object returned when calling `tckmap(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output: OutputPathType
    """the output track-weighted image"""


def tckmap(
    tracks: InputPathType,
    output: str,
    template: InputPathType | None = None,
    vox: list[float] | None = None,
    datatype: str | None = None,
    dec: bool = False,
    dixel: typing.Union[TckmapVariousString, TckmapVariousFile] | None = None,
    tod: int | None = None,
    contrast: str | None = None,
    image: InputPathType | None = None,
    vector_file: InputPathType | None = None,
    stat_vox: str | None = None,
    stat_tck: str | None = None,
    fwhm_tck: float | None = None,
    map_zero: bool = False,
    backtrack: bool = False,
    upsample: int | None = None,
    precise: bool = False,
    ends_only: bool = False,
    tck_weights_in: InputPathType | None = None,
    info: bool = False,
    quiet: bool = False,
    debug: bool = False,
    force: bool = False,
    nthreads: int | None = None,
    config: list[TckmapConfig] | None = None,
    help_: bool = False,
    version: bool = False,
    runner: Runner | None = None,
) -> TckmapOutputs:
    """
    Use track data as a form of contrast for producing a high-resolution image.
    
    Note: if you run into limitations with RAM usage, make sure you output the
    results to a .mif file or .mih / .dat file pair - this will avoid the
    allocation of an additional buffer to store the output for write-out.
    
    References:
    
    * For TDI or DEC TDI:
    Calamante, F.; Tournier, J.-D.; Jackson, G. D. & Connelly, A. Track-density
    imaging (TDI): Super-resolution white matter imaging using whole-brain
    track-density mapping. NeuroImage, 2010, 53, 1233-1243
    
    * If using -contrast length and -stat_vox mean:
    Pannek, K.; Mathias, J. L.; Bigler, E. D.; Brown, G.; Taylor, J. D. & Rose,
    S. E. The average pathlength map: A diffusion MRI tractography-derived index
    for studying brain pathology. NeuroImage, 2011, 55, 133-141
    
    * If using -dixel option with TDI contrast only:
    Smith, R.E., Tournier, J-D., Calamante, F., Connelly, A. A novel paradigm
    for automated segmentation of very large whole-brain probabilistic
    tractography data sets. In proc. ISMRM, 2011, 19, 673
    
    * If using -dixel option with any other contrast:
    Pannek, K., Raffelt, D., Salvado, O., Rose, S. Incorporating directional
    information in diffusion tractography derived maps: angular track imaging
    (ATI). In Proc. ISMRM, 2012, 20, 1912
    
    * If using -tod option:
    Dhollander, T., Emsell, L., Van Hecke, W., Maes, F., Sunaert, S., Suetens,
    P. Track Orientation Density Imaging (TODI) and Track Orientation
    Distribution (TOD) based tractography. NeuroImage, 2014, 94, 312-336
    
    * If using other contrasts / statistics:
    Calamante, F.; Tournier, J.-D.; Smith, R. E. & Connelly, A. A generalised
    framework for super-resolution track-weighted imaging. NeuroImage, 2012, 59,
    2494-2503
    
    * If using -precise mapping option:
    Smith, R. E.; Tournier, J.-D.; Calamante, F. & Connelly, A. SIFT:
    Spherical-deconvolution informed filtering of tractograms. NeuroImage, 2013,
    67, 298-312 (Appendix 3).
    
    Author: MRTrix3 Developers
    
    URL: https://www.mrtrix.org/
    
    Args:
        tracks: the input track file.
        output: the output track-weighted image.
        template: an image file to be used as a template for the output (the\
            output image will have the same transform and field of view).
        vox: provide either an isotropic voxel size (in mm), or comma-separated\
            list of 3 voxel dimensions.
        datatype: specify output image data type.
        dec: perform track mapping in directionally-encoded colour (DEC) space.
        dixel: map streamlines to dixels within each voxel; requires either a\
            number of dixels (references an internal direction set), or a path to a\
            text file containing a set of directions stored as azimuth/elevation\
            pairs.
        tod: generate a Track Orientation Distribution (TOD) in each voxel;\
            need to specify the maximum spherical harmonic degree lmax to use when\
            generating Apodised Point Spread Functions.
        contrast: define the desired form of contrast for the output image\
            Options are: tdi, length, invlength, scalar_map, scalar_map_count,\
            fod_amp, curvature, vector_file (default: tdi).
        image: provide the scalar image map for generating images with\
            'scalar_map' / 'scalar_map_count' contrast, or the spherical harmonics\
            image for 'fod_amp' contrast.
        vector_file: provide the vector data file for generating images with\
            'vector_file' contrast.
        stat_vox: define the statistic for choosing the final voxel intensities\
            for a given contrast type given the individual values from the tracks\
            passing through each voxel.\
            Options are: sum, min, mean, max (default: sum).
        stat_tck: define the statistic for choosing the contribution to be made\
            by each streamline as a function of the samples taken along their\
            lengths.\
            Only has an effect for 'scalar_map', 'fod_amp' and 'curvature'\
            contrast types.\
            Options are: sum, min, mean, max, median, mean_nonzero, gaussian,\
            ends_min, ends_mean, ends_max, ends_prod (default: mean).
        fwhm_tck: when using gaussian-smoothed per-track statistic, specify the\
            desired full-width half-maximum of the Gaussian smoothing kernel (in\
            mm).
        map_zero: if a streamline has zero contribution based on the contrast &\
            statistic, typically it is not mapped; use this option to still\
            contribute to the map even if this is the case (these non-contributing\
            voxels can then influence the mean value in each voxel of the map).
        backtrack: when using -stat_tck ends_*, if the streamline endpoint is\
            outside the FoV, backtrack along the streamline trajectory until an\
            appropriate point is found.
        upsample: upsample the tracks by some ratio using Hermite interpolation\
            before mappping\
            (If omitted, an appropriate ratio will be determined automatically).
        precise: use a more precise streamline mapping strategy, that\
            accurately quantifies the length through each voxel (these lengths are\
            then taken into account during TWI calculation).
        ends_only: only map the streamline endpoints to the image.
        tck_weights_in: specify a text scalar file containing the streamline\
            weights.
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
        NamedTuple of outputs (described in `TckmapOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(TCKMAP_METADATA)
    cargs = []
    cargs.append("tckmap")
    if template is not None:
        cargs.extend([
            "-template",
            execution.input_file(template)
        ])
    if vox is not None:
        cargs.extend([
            "-vox",
            ",".join(map(str, vox))
        ])
    if datatype is not None:
        cargs.extend([
            "-datatype",
            datatype
        ])
    if dec:
        cargs.append("-dec")
    if dixel is not None:
        cargs.extend([
            "-dixel",
            *dixel.run(execution)
        ])
    if tod is not None:
        cargs.extend([
            "-tod",
            str(tod)
        ])
    if contrast is not None:
        cargs.extend([
            "-contrast",
            contrast
        ])
    if image is not None:
        cargs.extend([
            "-image",
            execution.input_file(image)
        ])
    if vector_file is not None:
        cargs.extend([
            "-vector_file",
            execution.input_file(vector_file)
        ])
    if stat_vox is not None:
        cargs.extend([
            "-stat_vox",
            stat_vox
        ])
    if stat_tck is not None:
        cargs.extend([
            "-stat_tck",
            stat_tck
        ])
    if fwhm_tck is not None:
        cargs.extend([
            "-fwhm_tck",
            str(fwhm_tck)
        ])
    if map_zero:
        cargs.append("-map_zero")
    if backtrack:
        cargs.append("-backtrack")
    if upsample is not None:
        cargs.extend([
            "-upsample",
            str(upsample)
        ])
    if precise:
        cargs.append("-precise")
    if ends_only:
        cargs.append("-ends_only")
    if tck_weights_in is not None:
        cargs.extend([
            "-tck_weights_in",
            execution.input_file(tck_weights_in)
        ])
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
    cargs.append(execution.input_file(tracks))
    cargs.append(output)
    ret = TckmapOutputs(
        root=execution.output_file("."),
        output=execution.output_file(output),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "TCKMAP_METADATA",
    "TckmapConfig",
    "TckmapOutputs",
    "TckmapVariousFile",
    "TckmapVariousString",
    "tckmap",
]
