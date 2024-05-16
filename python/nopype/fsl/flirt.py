# This file was auto generated by styx-boutiques-codegen
# Do not edit this file directly
# Timestamp: 2024-05-16T18:58:56.021811

import typing

from ..styxdefs import *


FLIRT_METADATA = Metadata(
    id="5a6670d6e94d71d202f5633155acca488f17fca5",
    name="FLIRT",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FlirtOutputs(typing.NamedTuple):
    """
    Output object returned when calling `flirt(...)`.
    """
    out_file: OutputPathType
    """Registered output file."""
    out_matrix_file: OutputPathType
    """Output affine matrix in 4x4 asciii format."""


def flirt(
    runner: Runner,
    in_file: InputPathType,
    reference: InputPathType,
    angle_rep: typing.Literal["quaternion", "euler"] | None = "euler",
    apply_isoxfm: float | int | None = None,
    apply_xfm: bool = False,
    bbrslope: float | int | None = None,
    bbrtype: typing.Literal["signed", "global_abs", "local_abs"] | None = "signed",
    bgvalue: float | int | None = None,
    bins: int | None = None,
    coarse_search: int | None = 60,
    cost: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff", "bbr"] | None = "corratio",
    cost_func: typing.Literal["mutualinfo", "corratio", "normcorr", "normmi", "leastsq", "labeldiff", "bbr"] | None = "corratio",
    datatype: typing.Literal["char", "short", "int", "float", "double"] | None = None,
    display_init: bool = False,
    dof: int | None = 12,
    echospacing: float | int | None = None,
    fieldmap: InputPathType | None = None,
    fieldmapmask: InputPathType | None = None,
    fine_search: int | None = 18,
    force_scaling: bool = False,
    in_matrix_file: InputPathType | None = None,
    in_weight: InputPathType | None = None,
    interp: typing.Literal["trilinear", "nearestneighbour", "sinc", "spline"] | None = "trilinear",
    min_sampling: float | int | None = None,
    no_clamp: bool = False,
    no_resample: bool = False,
    no_resample_blur: bool = False,
    no_search: bool = False,
    padding_size: int | None = None,
    pedir: int | None = None,
    ref_weight: InputPathType | None = None,
    rigid2_d: bool = False,
    schedule: InputPathType | None = None,
    searchr_x: list[int] = None,
    searchr_y: list[int] = None,
    searchr_z: list[int] = None,
    sinc_width: int | None = 7,
    sinc_window: typing.Literal["rectangular", "hanning", "blackman"] | None = None,
    uses_qform: bool = False,
    verbose: int | None = 0,
    wm_seg: InputPathType | None = None,
    wmcoords: InputPathType | None = None,
    wmnorms: InputPathType | None = None,
) -> FlirtOutputs:
    """
    FLIRT, as implemented in Nipype (module: nipype.interfaces.fsl, interface:
    FLIRT).
    FSL FLIRT wrapper for coregistration
    For complete details, see the `FLIRT Documentation.
    <https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FLIRT>`_
    To print out the command line help, use: fsl.FLIRT().inputs_help()
    
    Args:
        runner: Command runner
        in_file: Input file.
        reference: Reference file.
        angle_rep: 'quaternion' or 'euler'. Representation of rotation angles.
        apply_isoxfm: As applyxfm but forces isotropic resampling.
        apply_xfm: Apply transformation supplied by in_matrix_file or uses_qform
            to use the affine matrix stored in the reference header.
        bbrslope: Value of bbr slope.
        bbrtype: 'signed' or 'global_abs' or 'local_abs'. Type of bbr cost
            function: signed [default], global_abs, local_abs.
        bgvalue: Use specified background value for points outside fov.
        bins: Number of histogram bins.
        coarse_search: Coarse search delta angle.
        cost: 'mutualinfo' or 'corratio' or 'normcorr' or 'normmi' or 'leastsq'
            or 'labeldiff' or 'bbr'. Cost function.
        cost_func: 'mutualinfo' or 'corratio' or 'normcorr' or 'normmi' or
            'leastsq' or 'labeldiff' or 'bbr'. Cost function.
        datatype: 'char' or 'short' or 'int' or 'float' or 'double'. Force
            output data type.
        display_init: Display initial matrix.
        dof: Number of transform degrees of freedom.
        echospacing: Value of epi echo spacing - units of seconds.
        fieldmap: Fieldmap image in rads/s - must be already registered to the
            reference image.
        fieldmapmask: Mask for fieldmap image.
        fine_search: Fine search delta angle.
        force_scaling: Force rescaling even for low-res images.
        in_matrix_file: Input 4x4 affine matrix.
        in_weight: File for input weighting volume.
        interp: 'trilinear' or 'nearestneighbour' or 'sinc' or 'spline'. Final
            interpolation method used in reslicing.
        min_sampling: Set minimum voxel dimension for sampling.
        no_clamp: Do not use intensity clamping.
        no_resample: Do not change input sampling.
        no_resample_blur: Do not use blurring on downsampling.
        no_search: Set all angular searches to ranges 0 to 0.
        padding_size: For applyxfm: interpolates outside image by size.
        pedir: Phase encode direction of epi - 1/2/3=x/y/z & -1/-2/-3=-x/-y/-z.
        ref_weight: File for reference weighting volume.
        rigid2_d: Use 2d rigid body mode - ignores dof.
        schedule: Replaces default schedule.
        searchr_x: Search angles along x-axis, in degrees.
        searchr_y: Search angles along y-axis, in degrees.
        searchr_z: Search angles along z-axis, in degrees.
        sinc_width: Full-width in voxels.
        sinc_window: 'rectangular' or 'hanning' or 'blackman'. Sinc window.
        uses_qform: Initialize using sform or qform.
        verbose: Verbose mode, 0 is least.
        wm_seg: White matter segmentation volume needed by bbr cost function.
        wmcoords: White matter boundary coordinates for bbr cost function.
        wmnorms: White matter boundary normals for bbr cost function.
    Returns:
        NamedTuple of outputs (described in `FlirtOutputs`).
    """
    if searchr_x is not None and (len(searchr_x) != 2): 
        raise ValueError(f"Length of 'searchr_x' must be 2 but was {len(searchr_x)}")
    if searchr_y is not None and (len(searchr_y) != 2): 
        raise ValueError(f"Length of 'searchr_y' must be 2 but was {len(searchr_y)}")
    if searchr_z is not None and (len(searchr_z) != 2): 
        raise ValueError(f"Length of 'searchr_z' must be 2 but was {len(searchr_z)}")
    if (
        apply_xfm +
        (apply_isoxfm is not None)
    ) > 1:
        raise ValueError(
            "Only one of the following arguments can be specified:\n"
            "apply_xfm,\n"
            "apply_isoxfm"
        )
    execution = runner.start_execution(FLIRT_METADATA)
    cargs = []
    cargs.append("FLIRT")
    cargs.extend(["-in", execution.input_file(in_file)])
    cargs.extend(["-ref", execution.input_file(reference)])
    cargs.append("[OUT_FILE]")
    cargs.append("[OUT_MATRIX_FILE]")
    if angle_rep is not None:
        cargs.extend(["-anglerep", angle_rep])
    if apply_isoxfm is not None:
        cargs.extend(["-applyisoxfm", str(apply_isoxfm)])
    if apply_xfm:
        cargs.append("-applyxfm")
    if bbrslope is not None:
        cargs.extend(["-bbrslope", str(bbrslope)])
    if bbrtype is not None:
        cargs.extend(["-bbrtype", bbrtype])
    if bgvalue is not None:
        cargs.extend(["-setbackground", str(bgvalue)])
    if bins is not None:
        cargs.extend(["-bins", str(bins)])
    if coarse_search is not None:
        cargs.extend(["-coarsesearch", str(coarse_search)])
    if cost is not None:
        cargs.extend(["-cost", cost])
    if cost_func is not None:
        cargs.extend(["-searchcost", cost_func])
    if datatype is not None:
        cargs.extend(["-datatype", datatype])
    if display_init:
        cargs.append("-displayinit")
    if dof is not None:
        cargs.extend(["-dof", str(dof)])
    if echospacing is not None:
        cargs.extend(["-echospacing", str(echospacing)])
    if fieldmap is not None:
        cargs.extend(["-fieldmap", execution.input_file(fieldmap)])
    if fieldmapmask is not None:
        cargs.extend(["-fieldmapmask", execution.input_file(fieldmapmask)])
    if fine_search is not None:
        cargs.extend(["-finesearch", str(fine_search)])
    if force_scaling:
        cargs.append("-forcescaling")
    if in_matrix_file is not None:
        cargs.extend(["-init", execution.input_file(in_matrix_file)])
    if in_weight is not None:
        cargs.extend(["-inweight", execution.input_file(in_weight)])
    if interp is not None:
        cargs.extend(["-interp", interp])
    if min_sampling is not None:
        cargs.extend(["-minsampling", str(min_sampling)])
    if no_clamp:
        cargs.append("-noclamp")
    if no_resample:
        cargs.append("-noresample")
    if no_resample_blur:
        cargs.append("-noresampblur")
    if no_search:
        cargs.append("-nosearch")
    if padding_size is not None:
        cargs.extend(["-paddingsize", str(padding_size)])
    if pedir is not None:
        cargs.extend(["-pedir", str(pedir)])
    if ref_weight is not None:
        cargs.extend(["-refweight", execution.input_file(ref_weight)])
    if rigid2_d:
        cargs.append("-2D")
    if schedule is not None:
        cargs.extend(["-schedule", execution.input_file(schedule)])
    if searchr_x is not None:
        cargs.extend(["-searchrx", *map(str, searchr_x)])
    if searchr_y is not None:
        cargs.extend(["-searchry", *map(str, searchr_y)])
    if searchr_z is not None:
        cargs.extend(["-searchrz", *map(str, searchr_z)])
    if sinc_width is not None:
        cargs.extend(["-sincwidth", str(sinc_width)])
    if sinc_window is not None:
        cargs.extend(["-sincwindow", sinc_window])
    if uses_qform:
        cargs.append("-usesqform")
    if verbose is not None:
        cargs.extend(["-verbose", str(verbose)])
    if wm_seg is not None:
        cargs.extend(["-wmseg", execution.input_file(wm_seg)])
    if wmcoords is not None:
        cargs.extend(["-wmcoords", execution.input_file(wmcoords)])
    if wmnorms is not None:
        cargs.extend(["-wmnorms", execution.input_file(wmnorms)])
    def _rstrip(s, r):
        for postfix in r:
            if s.endswith(postfix):
                return s[: -len(postfix)]
        return s
    ret = FlirtOutputs(
        out_file=execution.output_file(f"{_rstrip(in_file, ['.nii.gz', '.nii'])}_flirt.nii", optional=True),
        out_matrix_file=execution.output_file(f"{_rstrip(in_file, ['.nii.gz', '.nii'])}_flirt.mat", optional=True),
    )
    execution.run(cargs)
    return ret