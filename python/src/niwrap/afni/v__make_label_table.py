# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

V__MAKE_LABEL_TABLE_METADATA = Metadata(
    id="ed5ca968ee83794fda1307ebaf226a6eedebf580.boutiques",
    name="@MakeLabelTable",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class VMakeLabelTableOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v__make_label_table(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_labeltable: OutputPathType
    """Output label table file"""
    output_atlas_pointlist: OutputPathType | None
    """Output atlas point list file"""
    output_csv: OutputPathType | None
    """Output CSV file from label table"""
    output_niml_atlas: OutputPathType | None
    """Output NIML file after atlasizing labeled dataset"""


def v__make_label_table(
    labeltable: str,
    atlas_pointlist: str | None = None,
    lab_r: list[str] | None = None,
    lab_v: list[str] | None = None,
    lab_file: list[str] | None = None,
    dset: InputPathType | None = None,
    longnames: float | None = None,
    last_longname_col: float | None = None,
    centers: bool = False,
    centertype: str | None = None,
    centermask: str | None = None,
    skip_novoxels: bool = False,
    all_labels: bool = False,
    all_keys: bool = False,
    lkeys: str | None = None,
    rkeys: str | None = None,
    klabel: str | None = None,
    match_label: str | None = None,
    labeltable_of_dset: InputPathType | None = None,
    word_label_match: bool = False,
    quiet_death: bool = False,
    lt_to_atlas_pl: str | None = None,
    dset_lt_to_atlas_pl: list[InputPathType] | None = None,
    lt_to_csv: InputPathType | None = None,
    atlasize_labeled_dset: InputPathType | None = None,
    atlas_file: str | None = None,
    atlas_name: str | None = None,
    atlas_description: str | None = None,
    replace: bool = False,
    add_atlas_dset: InputPathType | None = None,
    h_web: bool = False,
    h_view: bool = False,
    all_opts: bool = False,
    h_find: str | None = None,
    runner: Runner | None = None,
) -> VMakeLabelTableOutputs:
    """
    Script used to create, modify, and transform label tables.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        labeltable: Name of output label table.
        atlas_pointlist: Instead of a label table, produce an atlas point list.
        lab_r: Define a label with its minimum and maximum key values.
        lab_v: Define a label and its value.
        lab_file: Specify labels and keys from a text file.
        dset: Attach the label table (or atlas point list) to dataset.
        longnames: Allow for another column of long names for regions.
        last_longname_col: Limit long names to nth column.
        centers: Compute center of mass location for each ROI.
        centertype: Different ways to compute centers (Icent, Dcent, cm).
        centermask: Calculate center of mass locations using a subset of voxels.
        skip_novoxels: Skip regions without voxels.
        all_labels: Return a listing of all labels.
        all_keys: Return a listing of all keys.
        lkeys: Return the keys whose labels match a given label.
        rkeys: Return the range (min max) of keys whose labels match a given\
            label.
        klabel: Return the label associated with a given key.
        match_label: Return labels matching a given label.
        labeltable_of_dset: Dump the labeltable from a dataset.
        word_label_match: Use word matching for labels.
        quiet_death: Do not give error messages when failing.
        lt_to_atlas_pl: Transform Label Table to Atlas Point List.
        dset_lt_to_atlas_pl: Get Label Table in dataset and write as an Atlas\
            Point List.
        lt_to_csv: Transform Label Table to CSV format.
        atlasize_labeled_dset: Transform a labeled ROI dataset into an atlas.
        atlas_file: Specify the name of the NIML file where atlas attributes\
            are stored.
        atlas_name: Name of the Atlas.
        atlas_description: Description of the Atlas, which appears in AFNI's\
            whereami window.
        replace: Replace existing Atlas if the name already exists in the NIML\
            file.
        add_atlas_dset: Add an existing atlas to an atlas file.
        h_web: Open webpage with help for this program.
        h_view: Open -help output in a GUI editor.
        all_opts: List all of the options for this script.
        h_find: Search for lines containing a specific word in the help output.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `VMakeLabelTableOutputs`).
    """
    if lab_file is not None and not (1 <= len(lab_file) <= 2): 
        raise ValueError(f"Length of 'lab_file' must be between 1 and 2 but was {len(lab_file)}")
    if dset_lt_to_atlas_pl is not None and (len(dset_lt_to_atlas_pl) != 2): 
        raise ValueError(f"Length of 'dset_lt_to_atlas_pl' must be 2 but was {len(dset_lt_to_atlas_pl)}")
    runner = runner or get_global_runner()
    execution = runner.start_execution(V__MAKE_LABEL_TABLE_METADATA)
    cargs = []
    cargs.append("@MakeLabelTable")
    cargs.extend([
        "-labeltable",
        labeltable
    ])
    if atlas_pointlist is not None:
        cargs.extend([
            "-atlas_pointlist",
            atlas_pointlist
        ])
    if lab_r is not None:
        cargs.extend([
            "-lab_r",
            *lab_r
        ])
    if lab_v is not None:
        cargs.extend([
            "-lab_v",
            *lab_v
        ])
    if lab_file is not None:
        cargs.extend([
            "-lab_file",
            *lab_file
        ])
    if dset is not None:
        cargs.extend([
            "-dset",
            execution.input_file(dset)
        ])
    if longnames is not None:
        cargs.extend([
            "-longnames",
            str(longnames)
        ])
    if last_longname_col is not None:
        cargs.extend([
            "-last_longname_col",
            str(last_longname_col)
        ])
    if centers:
        cargs.append("-centers")
    if centertype is not None:
        cargs.extend([
            "-centertype",
            centertype
        ])
    if centermask is not None:
        cargs.extend([
            "-centermask",
            centermask
        ])
    if skip_novoxels:
        cargs.append("-skip_novoxels")
    if all_labels:
        cargs.append("-all_labels")
    if all_keys:
        cargs.append("-all_keys")
    if lkeys is not None:
        cargs.extend([
            "-lkeys",
            lkeys
        ])
    if rkeys is not None:
        cargs.extend([
            "-rkeys",
            rkeys
        ])
    if klabel is not None:
        cargs.extend([
            "-klabel",
            klabel
        ])
    if match_label is not None:
        cargs.extend([
            "-match_label",
            match_label
        ])
    if labeltable_of_dset is not None:
        cargs.extend([
            "-labeltable_of_dset",
            execution.input_file(labeltable_of_dset)
        ])
    if word_label_match:
        cargs.append("-word_label_match")
    if quiet_death:
        cargs.append("-quiet_death")
    if lt_to_atlas_pl is not None:
        cargs.extend([
            "-LT_to_atlas_PL",
            lt_to_atlas_pl
        ])
    if dset_lt_to_atlas_pl is not None:
        cargs.extend([
            "-dset_LT_to_atlas_PL",
            *[execution.input_file(f) for f in dset_lt_to_atlas_pl]
        ])
    if lt_to_csv is not None:
        cargs.extend([
            "-LT_to_CSV",
            execution.input_file(lt_to_csv)
        ])
    if atlasize_labeled_dset is not None:
        cargs.extend([
            "-atlasize_labeled_dset",
            execution.input_file(atlasize_labeled_dset)
        ])
    if atlas_file is not None:
        cargs.extend([
            "-atlas_file",
            atlas_file
        ])
    if atlas_name is not None:
        cargs.extend([
            "-atlas_name",
            atlas_name
        ])
    if atlas_description is not None:
        cargs.extend([
            "-atlas_description",
            atlas_description
        ])
    if replace:
        cargs.append("-replace")
    if add_atlas_dset is not None:
        cargs.extend([
            "-add_atlas_dset",
            execution.input_file(add_atlas_dset)
        ])
    if h_web:
        cargs.append("-h_web")
    if h_view:
        cargs.append("-h_view")
    if all_opts:
        cargs.append("-all_opts")
    if h_find is not None:
        cargs.extend([
            "-h_find",
            h_find
        ])
    ret = VMakeLabelTableOutputs(
        root=execution.output_file("."),
        output_labeltable=execution.output_file(labeltable + ".niml.lt"),
        output_atlas_pointlist=execution.output_file(atlas_pointlist + ".niml.atlas") if (atlas_pointlist is not None) else None,
        output_csv=execution.output_file(pathlib.Path(lt_to_csv).name + ".csv") if (lt_to_csv is not None) else None,
        output_niml_atlas=execution.output_file(pathlib.Path(atlasize_labeled_dset).name + ".niml") if (atlasize_labeled_dset is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VMakeLabelTableOutputs",
    "V__MAKE_LABEL_TABLE_METADATA",
    "v__make_label_table",
]
