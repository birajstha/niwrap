# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

MAKE_CORTEX_LABEL_METADATA = Metadata(
    id="bc9db42feeb6c156b6f40c957b8a6e6c8e3082e6.boutiques",
    name="make_cortex_label",
    package="freesurfer",
    container_image_tag="freesurfer/freesurfer:7.4.1",
)


class MakeCortexLabelOutputs(typing.NamedTuple):
    """
    Output object returned when calling `make_cortex_label(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_label_file: OutputPathType | None
    """The output cortex label file."""


def make_cortex_label(
    subject: str,
    hemi: str | None = None,
    use_a2009s: bool = False,
    output_name: str | None = "cortex",
    runner: Runner | None = None,
) -> MakeCortexLabelOutputs:
    """
    A tool to create cortical labels.
    
    Author: FreeSurfer Developers
    
    URL: https://github.com/freesurfer/freesurfer
    
    Args:
        subject: The subject for which the cortex label is to be created.
        hemi: The hemisphere(s) on which to operate. Default is both\
            hemispheres.
        use_a2009s: Use aparc.a2009 instead of aparc.
        output_name: Output name. The output will be ?h.outname.label. Default\
            is 'cortex'.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `MakeCortexLabelOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(MAKE_CORTEX_LABEL_METADATA)
    cargs = []
    cargs.append("make_cortex_label")
    cargs.append("--s")
    cargs.extend([
        "--s",
        subject
    ])
    if hemi is not None:
        cargs.extend([
            "--h",
            hemi
        ])
    if use_a2009s:
        cargs.append("--a2009s")
    cargs.append("--o")
    if output_name is not None:
        cargs.extend([
            "--o",
            output_name
        ])
    ret = MakeCortexLabelOutputs(
        root=execution.output_file("."),
        output_label_file=execution.output_file("?h." + output_name + ".label") if (output_name is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "MAKE_CORTEX_LABEL_METADATA",
    "MakeCortexLabelOutputs",
    "make_cortex_label",
]