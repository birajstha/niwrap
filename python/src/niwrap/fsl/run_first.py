# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

RUN_FIRST_METADATA = Metadata(
    id="513ac693cec3476ae5a2662d43afee950a3d6856",
    name="run_first",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class RunFirstOutputs(typing.NamedTuple):
    """
    Output object returned when calling `run_first(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType
    """Output files generated by FIRST"""


def run_first(
    input_image: InputPathType,
    transformation_matrix: InputPathType,
    n_modes: float | int,
    output_basename: str,
    model_name: InputPathType,
    verbose_flag: bool = False,
    intref_model_name: str | None = None,
    load_bvars: InputPathType | None = None,
    multiple_images_flag: bool = False,
    runner: Runner | None = None,
) -> RunFirstOutputs:
    """
    run_first by Oxford Centre for Functional MRI of the Brain (FMRIB).
    
    A tool to run FSL's FIRST for subcortical segmentation.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FIRST
    
    Args:
        input_image: Input image file (e.g. img.nii.gz).
        transformation_matrix: Input transformation matrix file (e.g.\
            input_to_mni.mat).
        n_modes: Number of modes.
        output_basename: Output basename.
        model_name: Model name.
        verbose_flag: Verbose mode.
        intref_model_name: Reference structure for the local intensity\
            normalization.
        load_bvars: Initializes FIRST with a previous estimate of the structure.
        multiple_images_flag: Run FIRST on multiple images; provide a list of\
            images, transformation matrices, and output names.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RunFirstOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RUN_FIRST_METADATA)
    cargs = []
    cargs.append("run_first")
    cargs.append("-i")
    cargs.append(execution.input_file(input_image))
    cargs.append("-t")
    cargs.append(execution.input_file(transformation_matrix))
    cargs.append("-n")
    cargs.append(str(n_modes))
    cargs.append("-o")
    cargs.append(output_basename)
    cargs.append("-m")
    cargs.append(execution.input_file(model_name))
    if verbose_flag:
        cargs.append("-v")
    if intref_model_name is not None:
        cargs.extend(["-intref", intref_model_name])
    if load_bvars is not None:
        cargs.extend(["-loadBvars", execution.input_file(load_bvars)])
    if multiple_images_flag:
        cargs.append("-multipleImages")
    ret = RunFirstOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(f"{output_basename}*", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RUN_FIRST_METADATA",
    "RunFirstOutputs",
    "run_first",
]
