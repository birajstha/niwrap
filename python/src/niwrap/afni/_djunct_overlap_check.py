# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

_DJUNCT_OVERLAP_CHECK_METADATA = Metadata(
    id="742d5817fdc45fe04e551d642aaef270989eb4e2",
    name="@djunct_overlap_check",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class DjunctOverlapCheckOutputs(typing.NamedTuple):
    """
    Output object returned when calling `_djunct_overlap_check(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def _djunct_overlap_check(
    ulay: InputPathType,
    olay: InputPathType,
    prefix: str,
    box_focus_slices: InputPathType | None = None,
    montgap: float | int | None = None,
    montcolor: str | None = None,
    cbar: str | None = None,
    opacity: float | int | None = None,
    zerocolor: str | None = None,
    set_dicom_xyz: list[float | int] | None = None,
    ulay_range: list[float | int] | None = None,
    ulay_range_nz: list[float | int] | None = None,
    montx: float | int | None = None,
    monty: float | int | None = None,
    montx_cat: float | int | None = None,
    monty_cat: float | int | None = None,
    label_mode: str | None = None,
    pbar_posonly_off: bool = False,
    edgy_ulay: bool = False,
    set_dicom_xyz_off: bool = False,
    no_cor: bool = False,
    no_axi: bool = False,
    no_sag: bool = False,
    no_clean: bool = False,
    runner: Runner | None = None,
) -> DjunctOverlapCheckOutputs:
    """
    @djunct_overlap_check by AFNI Team.
    
    A helper script for visualizing overlap between datasets in AFNI.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/@djunct_overlap_check.html
    
    Args:
        ulay: Dataset to use as the underlay (background).
        olay: Dataset to use as the overlay (foreground).
        prefix: Prefix for the output files.
        box_focus_slices: Dataset for box focus slices.
        montgap: Gap between montage slices.
        montcolor: Color of the montage gap.
        cbar: Colorbar for the overlay.
        opacity: Opacity of the overlay.
        zerocolor: Color for zero values.
        set_dicom_xyz: Set DICOM coordinates for slice location.
        ulay_range: Range for underlay values.
        ulay_range_nz: Range for non-zero underlay values.
        montx: Number of panels in X direction in montage.
        monty: Number of panels in Y direction in montage.
        montx_cat: Number of X panes per image in montage.
        monty_cat: Number of Y panes per image in montage.
        label_mode: Label mode.
        pbar_posonly_off: Turn off position-only p-bar.
        edgy_ulay: Edgify the underlay.
        set_dicom_xyz_off: Turn off DICOM coordinates setting.
        no_cor: Skip coronal slices.
        no_axi: Skip axial slices.
        no_sag: Skip sagittal slices.
        no_clean: Do not clean up temporary files.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `DjunctOverlapCheckOutputs`).
    """
    runner = runner or get_global_runner()
    if set_dicom_xyz is not None and (len(set_dicom_xyz) != 3): 
        raise ValueError(f"Length of 'set_dicom_xyz' must be 3 but was {len(set_dicom_xyz)}")
    if ulay_range is not None and (len(ulay_range) != 2): 
        raise ValueError(f"Length of 'ulay_range' must be 2 but was {len(ulay_range)}")
    if ulay_range_nz is not None and (len(ulay_range_nz) != 2): 
        raise ValueError(f"Length of 'ulay_range_nz' must be 2 but was {len(ulay_range_nz)}")
    execution = runner.start_execution(_DJUNCT_OVERLAP_CHECK_METADATA)
    cargs = []
    cargs.append("@djunct_overlap_check")
    cargs.append(execution.input_file(ulay))
    cargs.append(execution.input_file(olay))
    cargs.append(prefix)
    if box_focus_slices is not None:
        cargs.append(execution.input_file(box_focus_slices))
    if montgap is not None:
        cargs.extend(["-montgap", str(montgap)])
    if montcolor is not None:
        cargs.extend(["-montcolor", montcolor])
    if cbar is not None:
        cargs.extend(["-cbar", cbar])
    if opacity is not None:
        cargs.extend(["-opacity", str(opacity)])
    if zerocolor is not None:
        cargs.extend(["-zerocolor", zerocolor])
    cargs.append("[XX]")
    cargs.append("[YY]")
    cargs.append("[ZZ]")
    cargs.append("[umin]")
    cargs.append("[umax]")
    if montx is not None:
        cargs.extend(["-montx", str(montx)])
    if monty is not None:
        cargs.extend(["-monty", str(monty)])
    if montx_cat is not None:
        cargs.extend(["-montx_cat", str(montx_cat)])
    if monty_cat is not None:
        cargs.extend(["-monty_cat", str(monty_cat)])
    if label_mode is not None:
        cargs.extend(["-label_mode", label_mode])
    if pbar_posonly_off:
        cargs.append("-pbar_posonly_off")
    if edgy_ulay:
        cargs.append("-edgy_ulay")
    if set_dicom_xyz_off:
        cargs.append("-set_dicom_xyz_off")
    if no_cor:
        cargs.append("-no_cor")
    if no_axi:
        cargs.append("-no_axi")
    if no_sag:
        cargs.append("-no_sag")
    if no_clean:
        cargs.append("-no_clean")
    ret = DjunctOverlapCheckOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "DjunctOverlapCheckOutputs",
    "_DJUNCT_OVERLAP_CHECK_METADATA",
    "_djunct_overlap_check",
]
