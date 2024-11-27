# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

QUICKSPEC_SL_METADATA = Metadata(
    id="25906cfa619866947e348b53b2e212694192bdac.boutiques",
    name="quickspecSL",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class QuickspecSlOutputs(typing.NamedTuple):
    """
    Output object returned when calling `quickspec_sl(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_spec_file: OutputPathType
    """Output spec file"""


def quickspec_sl(
    surf_a: InputPathType,
    surf_b: InputPathType,
    surf_intermed_pref: str | None = None,
    infl_surf_a: InputPathType | None = None,
    infl_surf_b: InputPathType | None = None,
    infl_surf_intermed_pref: str | None = None,
    both_lr_flag: bool = False,
    out_spec: str | None = None,
    runner: Runner | None = None,
) -> QuickspecSlOutputs:
    """
    This program makes a *.spec file after a set of intermediate surfaces have been
    generated with SurfLayers. It can also make a *.spec file that relates inflated
    surfaces to anatomically-correct surfaces.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        surf_a: Inner (anatomically-correct) boundary surface dataset (e.g.\
            smoothwm.gii).
        surf_b: Outer (anatomically-correct) boundary surface dataset (e.g.\
            pial.gii).
        surf_intermed_pref: Prefix for (anatomically-correct) intermediate\
            surfaces, typically output by SurfLayers (default: isurf).
        infl_surf_a: Inner (inflated) boundary surface dataset (e.g.\
            infl.smoothwm.gii).
        infl_surf_b: Outer (inflated) boundary surface dataset (e.g.\
            infl.pial.gii).
        infl_surf_intermed_pref: Prefix for (inflated) intermediate surfaces,\
            typically output by SurfLayers (default: infl.isurf).
        both_lr_flag: Specify an output spec for both hemispheres if surfaces\
            for both exist.
        out_spec: Name for output *.spec file (default: newspec.spec).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `QuickspecSlOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(QUICKSPEC_SL_METADATA)
    cargs = []
    cargs.append("quickspecSL")
    cargs.extend([
        "-surf_A",
        execution.input_file(surf_a)
    ])
    cargs.extend([
        "-surf_B",
        execution.input_file(surf_b)
    ])
    if surf_intermed_pref is not None:
        cargs.extend([
            "-surf_intermed_pref",
            surf_intermed_pref
        ])
    if infl_surf_a is not None:
        cargs.extend([
            "-infl_surf_A",
            execution.input_file(infl_surf_a)
        ])
    if infl_surf_b is not None:
        cargs.extend([
            "-infl_surf_B",
            execution.input_file(infl_surf_b)
        ])
    if infl_surf_intermed_pref is not None:
        cargs.extend([
            "-infl_surf_intermed_pref",
            infl_surf_intermed_pref
        ])
    if both_lr_flag:
        cargs.append("-both_lr")
    if out_spec is not None:
        cargs.extend([
            "-out_spec",
            out_spec
        ])
    ret = QuickspecSlOutputs(
        root=execution.output_file("."),
        output_spec_file=execution.output_file("[out_spec]"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "QUICKSPEC_SL_METADATA",
    "QuickspecSlOutputs",
    "quickspec_sl",
]
