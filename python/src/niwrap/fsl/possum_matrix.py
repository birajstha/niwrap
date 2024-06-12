# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

POSSUM_MATRIX_METADATA = Metadata(
    id="9935aeab25a1e5b48e3ade64a5c36ff606fb74fa",
    name="possum_matrix",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="fsl:6.0.5",
)


class PossumMatrixOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum_matrix(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_main_matrix: OutputPathType
    """Main event matrix output file"""


def possum_matrix(
    pulse_sequence: str,
    motion_matrix: str,
    output_matrix: str,
    verbose_flag: bool = False,
    help_flag: bool = False,
    old_version_flag: bool = False,
    segment_size: float | int | None = None,
    runner: Runner = None,
) -> PossumMatrixOutputs:
    """
    possum_matrix by University of Oxford (Ivana Drobnjak).
    
    Event matrix generator for POSSUM simulation in FSL.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/POSSUM
    
    Args:
        pulse_sequence: Pulse sequence - all additional files with extensions\
            .posx, .posy, etc., expected to be in the same directory.
        motion_matrix: Motion matrix [time(s) Tx(m) Ty(m) Tz(m) Rx(rad) Ry(rad)\
            Rz(rad)].
        output_matrix: Main event matrix [t(s), rf_ang(rad), rf_freq_band(Hz),\
            (4)=rf_cent_freq(Hz), read(1/0), Gx, Gy, Gz(T/m), Tx, Ty, Tz(m),\
            angle_of_rot B(rad), rot_axis Bx, By, Bz(m), angle_of_rot A(rad),\
            rot_axis Ax, Ay, Az(m)].
        verbose_flag: Switch on diagnostic messages.
        help_flag: Display this help message.
        old_version_flag: Allows for the old version of the sorter to run.
        segment_size: Setting the size of the segment of the matrix that is\
            read in one at a time.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PossumMatrixOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_MATRIX_METADATA)
    cargs = []
    cargs.append("possum_matrix")
    cargs.append("-p")
    cargs.extend(["-p", pulse_sequence])
    cargs.append("-m")
    cargs.extend(["-m", motion_matrix])
    cargs.append("-o")
    cargs.extend(["-o", output_matrix])
    if verbose_flag:
        cargs.append("-v")
    if help_flag:
        cargs.append("-h")
    if old_version_flag:
        cargs.append("--old")
    if segment_size is not None:
        cargs.extend(["--seg", str(segment_size)])
    ret = PossumMatrixOutputs(
        root=execution.output_file("."),
        output_main_matrix=execution.output_file(f"{output_matrix}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POSSUM_MATRIX_METADATA",
    "PossumMatrixOutputs",
    "possum_matrix",
]
