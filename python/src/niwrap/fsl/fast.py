# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


FAST_METADATA = Metadata(
    id="ae80f76ab518e5af78abbedeb400e1687400674e",
    name="FAST",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class FastOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fast(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    mixeltype: OutputPathType | None
    """Path/name of mixeltype volume file _mixeltype."""
    bias_field: OutputPathType | None
    """No description provided."""
    partial_volume_files: OutputPathType | None
    """No description provided."""
    partial_volume_map: OutputPathType | None
    """Path/name of partial volume file _pveseg."""
    probability_maps_outfile: OutputPathType | None
    """No description provided."""
    restored_image: OutputPathType | None
    """No description provided."""
    tissue_class_files: OutputPathType | None
    """No description provided."""
    tissue_class_map: OutputPathType | None
    """Path/name of binary segmented volume file one val for each class  _seg."""


def fast(
    in_files: list[InputPathType],
    number_classes: int | None = 3,
    bias_iters: int | None = 3,
    bias_lowpass: float | int | None = 20,
    img_type: typing.Literal[1, 2, 3] | None = 1,
    init_seg_smooth: float | int | None = 0.02,
    segments: bool = False,
    init_transform: InputPathType | None = None,
    other_priors: list[InputPathType] = None,
    output_biasfield: bool = False,
    output_biascorrected: bool = False,
    no_bias: bool = False,
    channels: int | None = 1,
    out_basename: InputPathType | None = "BrainExtractionBrain",
    use_priors: bool = False,
    no_pve: bool = False,
    segment_iters: int | None = 15,
    mixel_smooth: float | int | None = 0.3,
    iters_afterbias: int | None = 4,
    hyper: float | int | None = 0.1,
    verbose: bool = False,
    manual_seg: InputPathType | None = None,
    runner: Runner = None,
) -> FastOutputs:
    """
    FAST by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    FAST (FMRIB's Automated Segmentation Tool) segments a 3D image of the brain
    into different tissue types (Grey Matter, White Matter, CSF, etc.), whilst
    also correcting for spatial intensity variations (also known as bias field
    or RF inhomogeneities). The underlying method is based on a hidden Markov
    random field model and an associated Expectation-Maximization algorithm. The
    whole process is fully automated and can also produce a bias field-corrected
    input image and a probabilistic and/or partial volume tissue segmentation.
    It is robust and reliable, compared to most finite mixture model-based
    methods, which are sensitive to noise.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FAST
    
    Args:
        in_files: Image, or multi-channel set of images, to be segmented.
        number_classes: number of tissue-type classes; default=3
        bias_iters: number of main-loop iterations during bias-field removal;
            default=4
        bias_lowpass: bias field smoothing extent (FWHM) in mm; default=20
        img_type: type of image 1=T1, 2=T2, 3=PD; default=T1
        init_seg_smooth: initial segmentation spatial smoothness (during bias
            field estimation); default=0.02
        segments: outputs a separate binary image for each tissue type
        init_transform: initialise using priors; you must supply a FLIRT
            transform
        other_priors: Alternative prior images.
        output_biasfield: Output estimated bias field.
        output_biascorrected: Output restored image (bias-corrected image).
        no_bias: Do not remove bias field.
        channels: number of input images (channels); default 1
        out_basename: Base name of output files.
        use_priors: Use priors throughout.
        no_pve: Turn off pve (partial volume estimation).
        segment_iters: number of segmentation-initialisation iterations;
            default=15
        mixel_smooth: spatial smoothness for mixeltype; default=0.3
        iters_afterbias: number of main-loop iterations after bias-field
            removal; default=4
        hyper: 0.0 <= a floating point number <= 1.0. segmentation spatial
            smoothness; default=0.1
        verbose: Switch on diagnostic messages.
        manual_seg: Filename containing intensities.
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `FastOutputs`).
    """
    runner = runner or get_global_runner()
    if number_classes is not None and not (1 <= number_classes): 
        raise ValueError(f"'number_classes' must be greater than 1 <= x but was {number_classes}")
    if bias_iters is not None and not (1 <= bias_iters): 
        raise ValueError(f"'bias_iters' must be greater than 1 <= x but was {bias_iters}")
    if bias_lowpass is not None and not (0 <= bias_lowpass): 
        raise ValueError(f"'bias_lowpass' must be greater than 0 <= x but was {bias_lowpass}")
    if init_seg_smooth is not None and not (0.0001 <= init_seg_smooth <= 0.1): 
        raise ValueError(f"'init_seg_smooth' must be between 0.0001 <= x <= 0.1 but was {init_seg_smooth}")
    if channels is not None and not (1 <= channels): 
        raise ValueError(f"'channels' must be greater than 1 <= x but was {channels}")
    if segment_iters is not None and not (1 <= segment_iters): 
        raise ValueError(f"'segment_iters' must be greater than 1 <= x but was {segment_iters}")
    if mixel_smooth is not None and not (0.0 <= mixel_smooth <= 1.0): 
        raise ValueError(f"'mixel_smooth' must be between 0.0 <= x <= 1.0 but was {mixel_smooth}")
    if iters_afterbias is not None and not (1 <= iters_afterbias <= 20): 
        raise ValueError(f"'iters_afterbias' must be between 1 <= x <= 20 but was {iters_afterbias}")
    if hyper is not None and not (0.0 <= hyper <= 1.0): 
        raise ValueError(f"'hyper' must be between 0.0 <= x <= 1.0 but was {hyper}")
    execution = runner.start_execution(FAST_METADATA)
    cargs = []
    cargs.append("FAST")
    if number_classes is not None:
        cargs.extend(["-n", str(number_classes)])
    if bias_iters is not None:
        cargs.extend(["-I", str(bias_iters)])
    if bias_lowpass is not None:
        cargs.extend(["-l", str(bias_lowpass)])
    if img_type is not None:
        cargs.extend(["-t", str(img_type)])
    if init_seg_smooth is not None:
        cargs.extend(["-f", str(init_seg_smooth)])
    if segments:
        cargs.append("-g")
    if init_transform is not None:
        cargs.extend(["-a", execution.input_file(init_transform)])
    if other_priors is not None:
        cargs.extend(["-A", *[execution.input_file(f) for f in other_priors]])
    if output_biasfield:
        cargs.append("-b")
    if output_biascorrected:
        cargs.append("-B")
    if no_bias:
        cargs.append("-N")
    if channels is not None:
        cargs.extend(["-S", str(channels)])
    if out_basename is not None:
        cargs.extend(["-o", execution.input_file(out_basename)])
    if use_priors:
        cargs.append("-P")
    if no_pve:
        cargs.append("--nopve")
    if segment_iters is not None:
        cargs.extend(["-W", str(segment_iters)])
    if mixel_smooth is not None:
        cargs.extend(["-R", str(mixel_smooth)])
    if hyper is not None:
        cargs.extend(["-H", str(hyper)])
    if verbose:
        cargs.append("-v")
    if manual_seg is not None:
        cargs.extend(["-s", execution.input_file(manual_seg)])
    if iters_afterbias is not None:
        cargs.extend(["-O", str(iters_afterbias)])
    cargs.append("[PROBABILITY_MAPS]")
    cargs.extend([execution.input_file(f) for f in in_files])
    ret = FastOutputs(
        root=execution.output_file("."),
        mixeltype=execution.output_file(f"{pathlib.Path(out_basename).name}_mixeltype.nii.gz", optional=True) if out_basename is not None else None,
        bias_field=execution.output_file(f"{pathlib.Path(out_basename).name}_bias.nii.gz", optional=True) if out_basename is not None else None,
        partial_volume_files=execution.output_file(f"{pathlib.Path(out_basename).name}_pve_*.nii.gz", optional=True) if out_basename is not None else None,
        partial_volume_map=execution.output_file(f"{pathlib.Path(out_basename).name}_pveseg.nii.gz", optional=True) if out_basename is not None else None,
        probability_maps_outfile=execution.output_file(f"{pathlib.Path(out_basename).name}_prob_*.nii.gz", optional=True) if out_basename is not None else None,
        restored_image=execution.output_file(f"{pathlib.Path(out_basename).name}_restore.nii.gz", optional=True) if out_basename is not None else None,
        tissue_class_files=execution.output_file(f"{pathlib.Path(out_basename).name}_seg_*.nii.gz", optional=True) if out_basename is not None else None,
        tissue_class_map=execution.output_file(f"{pathlib.Path(out_basename).name}_seg.nii.gz", optional=True) if out_basename is not None else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAST_METADATA",
    "FastOutputs",
    "fast",
]
