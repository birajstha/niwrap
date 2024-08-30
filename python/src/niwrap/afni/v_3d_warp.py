# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

V_3D_WARP_METADATA = Metadata(
    id="596ed74ea429713ba4b99a676c769adae11fc2b4",
    name="3dWarp",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class V3dWarpOutputs(typing.NamedTuple):
    """
    Output object returned when calling `v_3d_warp(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def v_3d_warp(
    dataset: str,
    matvec_in2out: InputPathType | None = None,
    matvec_out2in: InputPathType | None = None,
    tta2mni: bool = False,
    mni2tta: bool = False,
    matparent: str | None = None,
    card2oblique: str | None = None,
    oblique_parent: str | None = None,
    deoblique: bool = False,
    oblique2card: bool = False,
    disp_obl_xform_only: bool = False,
    linear: bool = False,
    cubic: bool = False,
    nn: bool = False,
    quintic: bool = False,
    wsinc5: bool = False,
    fsl_matvec: bool = False,
    newgrid: float | int | None = None,
    gridset: str | None = None,
    zpad: float | int | None = None,
    verb: bool = False,
    prefix: str | None = None,
    runner: Runner | None = None,
) -> V3dWarpOutputs:
    """
    3dWarp by AFNI Team.
    
    Warp (spatially transform) one 3D dataset.
    
    More information:
    https://afni.nimh.nih.gov/pub/dist/doc/program_help/3dWarp.html
    
    Args:
        dataset: Input dataset to be warped.
        matvec_in2out: Read a 3x4 affine transform matrix+vector from file.
        matvec_out2in: Read a 3x4 affine transform matrix+vector from file.
        tta2mni: Transform a dataset in Talairach-Tournoux Atlas coordinates to\
            MNI-152 coordinates.
        mni2tta: Transform a dataset in MNI-152 coordinates to\
            Talairach-Tournoux Atlas coordinates.
        matparent: Read in the matrix from WARPDRIVE_MATVEC_* attributes in the\
            header of dataset.
        card2oblique: Make cardinal dataset oblique to match oblique dataset.
        oblique_parent: Make cardinal dataset oblique to match oblique dataset.
        deoblique: Transform an oblique dataset to a cardinal dataset.
        oblique2card: Transform an oblique dataset to a cardinal dataset.
        disp_obl_xform_only: Display the obliquity transform matrix.
        linear: Use linear interpolation.
        cubic: Use cubic interpolation.
        nn: Use nearest neighbor interpolation.
        quintic: Use quintic interpolation.
        wsinc5: Use wsinc5 interpolation.
        fsl_matvec: Indicates that the matrix file uses FSL ordered coordinates\
            ('LPI').
        newgrid: Compute new dataset on a new 3D grid, with specified spacing.
        gridset: Compute new dataset on the same grid as another dataset.
        zpad: Pad input dataset with specified planes of zeros on all sides\
            before transformation.
        verb: Print out some information along the way.
        prefix: Set the prefix of the output dataset.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `V3dWarpOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(V_3D_WARP_METADATA)
    cargs = []
    cargs.append("3dWarp")
    cargs.append("[OPTIONS]")
    cargs.append(dataset)
    ret = V3dWarpOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "V3dWarpOutputs",
    "V_3D_WARP_METADATA",
    "v_3d_warp",
]