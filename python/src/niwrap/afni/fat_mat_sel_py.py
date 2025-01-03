# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FAT_MAT_SEL_PY_METADATA = Metadata(
    id="507d4511ca162d3a004cc7ca58b188298e3eea66.boutiques",
    name="fat_mat_sel.py",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class FatMatSelPyOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fat_mat_sel_py(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    individual_images: OutputPathType
    """Individual images of matrix plots."""
    matrix_grids: OutputPathType
    """Output matrix grid files."""
    v_1_d_dsets: OutputPathType
    """Output 1D dataset files."""


def fat_mat_sel_py(
    parameters: str,
    matr_in: str | None = None,
    list_match: InputPathType | None = None,
    out_ind_matr: bool = False,
    out_ind_1ddset: bool = False,
    hold_image: bool = False,
    extern_labs_no: bool = False,
    type_file: str | None = None,
    dpi_file: float | None = None,
    xlen_file: float | None = None,
    ylen_file: float | None = None,
    tight_layout_on: bool = False,
    fig_off: bool = False,
    size_font: float | None = None,
    lab_size_font: float | None = None,
    a_plotmin: float | None = None,
    b_plotmax: float | None = None,
    cbar_off: bool = False,
    map_of_colors: str | None = None,
    cbar_int_num: float | None = None,
    width_cbar_perc: float | None = None,
    specifier: str | None = None,
    xtick_lab_off: bool = False,
    runner: Runner | None = None,
) -> FatMatSelPyOutputs:
    """
    Perform simple matrix plotting operations from outputs of FATCAT programs
    3dNetCorr and 3dTrackID.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        parameters: Supply names of parameters, separated by whitespace, for\
            selecting from a matrix file.
        matr_in: Provide the set of matrix (*.grid or *.netcc) files by\
            searchable path. This can be a globbable entry in quotes containing\
            wildcard characters.
        list_match: Provide the matrix (*.grid or *.netcc) files by explicit\
            path, matched per file with a CSV subject ID.
        out_ind_matr: Output individual matrix files of properties.
        out_ind_1ddset: Output as a 1D dset, more easily readable by other\
            programs.
        hold_image: Switch to hold the Python-produced image on the output\
            screen until a key has been hit.
        extern_labs_no: Switch to turn off the usage of user-defined labels in\
            the *.grid/*.netcc files.
        type_file: Select image format type (e.g., jpg, png, pdf).
        dpi_file: Set resolution (dots per inch) of output image.
        xlen_file: Horizontal dimension of output saved image, in units of\
            inches.
        ylen_file: Vertical dimension of output saved image, in units of\
            inches.
        tight_layout_on: Use matplotlib's tight_layout() option to ensure no\
            overlap of features in the image.
        fig_off: Switch if you don't want matrix figure output.
        size_font: Set font size for colorbar and title.
        lab_size_font: Set font size for x- and y-axis labels.
        a_plotmin: Minimum colorbar value.
        b_plotmax: Maximum colorbar value.
        cbar_off: Switch to not include a colorbar at the right side of the\
            plot.
        map_of_colors: Change the colormap style used in the plot.
        cbar_int_num: Set the number of intervals on the colorbar.
        width_cbar_perc: Width of colorbar as percentage of width of the\
            correlation matrix.
        specifier: Specify number formatting for the colorbar numbers (e.g.,\
            '%.4f' for four decimal places).
        xtick_lab_off: Switch to turn off labels along the x- (horizontal) axis\
            but leave those along the y- (vertical) axis.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FatMatSelPyOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FAT_MAT_SEL_PY_METADATA)
    cargs = []
    cargs.append("fat_mat_sel.py")
    cargs.extend([
        "--Pars",
        parameters
    ])
    if matr_in is not None:
        cargs.extend([
            "--matr_in",
            matr_in
        ])
    if list_match is not None:
        cargs.extend([
            "--list_match",
            execution.input_file(list_match)
        ])
    if out_ind_matr:
        cargs.append("--out_ind_matr")
    if out_ind_1ddset:
        cargs.append("--Out_ind_1ddset")
    if hold_image:
        cargs.append("--Hold_image")
    if extern_labs_no:
        cargs.append("--ExternLabsNo")
    if type_file is not None:
        cargs.extend([
            "--type_file",
            type_file
        ])
    if dpi_file is not None:
        cargs.extend([
            "--dpi_file",
            str(dpi_file)
        ])
    if xlen_file is not None:
        cargs.extend([
            "--xlen_file",
            str(xlen_file)
        ])
    if ylen_file is not None:
        cargs.extend([
            "--ylen_file",
            str(ylen_file)
        ])
    if tight_layout_on:
        cargs.append("--Tight_layout_on")
    if fig_off:
        cargs.append("--Fig_off")
    if size_font is not None:
        cargs.extend([
            "--Size_font",
            str(size_font)
        ])
    if lab_size_font is not None:
        cargs.extend([
            "--Lab_size_font",
            str(lab_size_font)
        ])
    if a_plotmin is not None:
        cargs.extend([
            "--A_plotmin",
            str(a_plotmin)
        ])
    if b_plotmax is not None:
        cargs.extend([
            "--B_plotmax",
            str(b_plotmax)
        ])
    if cbar_off:
        cargs.append("--Cbar_off")
    if map_of_colors is not None:
        cargs.extend([
            "--Map_of_colors",
            map_of_colors
        ])
    if cbar_int_num is not None:
        cargs.extend([
            "--cbar_int_num",
            str(cbar_int_num)
        ])
    if width_cbar_perc is not None:
        cargs.extend([
            "--width_cbar_perc",
            str(width_cbar_perc)
        ])
    if specifier is not None:
        cargs.extend([
            "--specifier",
            specifier
        ])
    if xtick_lab_off:
        cargs.append("--Xtick_lab_off")
    ret = FatMatSelPyOutputs(
        root=execution.output_file("."),
        individual_images=execution.output_file("individual_images/*"),
        matrix_grids=execution.output_file("matrix_grids/*"),
        v_1_d_dsets=execution.output_file("1D_dsets/*"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FAT_MAT_SEL_PY_METADATA",
    "FatMatSelPyOutputs",
    "fat_mat_sel_py",
]
