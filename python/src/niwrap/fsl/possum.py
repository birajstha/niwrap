# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

POSSUM_METADATA = Metadata(
    id="8d3256af4165cf8a2a5ebb1c21c522164306d6cc",
    name="possum",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:latest",
)


class PossumOutputs(typing.NamedTuple):
    """
    Output object returned when calling `possum(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_matrix: OutputPathType
    """Output matrix file generated by possum"""


def possum(
    input_volume: InputPathType,
    mr_parameters: InputPathType,
    motion_matrix: InputPathType,
    pulse_sequence: str,
    rf_slice_profile: InputPathType,
    output_signal: str,
    event_matrix: InputPathType,
    verbose: bool = False,
    help_: bool = False,
    kcoord: bool = False,
    b0_inhomogeneities: str | None = None,
    extra_b0_inhomogeneities: InputPathType | None = None,
    b0_inhomogeneities_timecourse: InputPathType | None = None,
    rf_inhomogeneity_receive: InputPathType | None = None,
    rf_inhomogeneity_transmit: InputPathType | None = None,
    activation_volume: InputPathType | None = None,
    activation_timecourse: InputPathType | None = None,
    activation_4d_volume: InputPathType | None = None,
    activation_4d_timecourse: InputPathType | None = None,
    level: str | None = None,
    num_procs: float | int | None = None,
    proc_id: float | int | None = None,
    no_speedup: bool = False,
    rf_average: bool = False,
    runner: Runner = None,
) -> PossumOutputs:
    """
    possum by University of Oxford (Ivana Drobnjak).
    
    Positron emission tomography (PET) simulation tool as part of FSL suite.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/POSSUM
    
    Args:
        input_volume: Input 4D volume filename
        mr_parameters: Input matrix filename containing MR parameters
        motion_matrix: Input motion matrix filename (time(s) Tx(m) Ty(m) Tz(m)
            Rx(rad) Ry(rad) Rz(rad))
        pulse_sequence: Input matrix basename for pulse sequence files (.posx,
            .posy, etc.)
        rf_slice_profile: Input matrix filename containing RF slice profile
        output_signal: Output matrix filename for the signal
        event_matrix: Main event matrix file [(t(s), rf_ang(rad),
            rf_freq_band(Hz), rf_cent_freq(Hz), ...)]
        verbose: Switch on diagnostic messages
        help_: Display help message
        kcoord: Save the k-space coordinates
        b0_inhomogeneities: B0 inhomogeneities due to susceptibility differences
            (basename)
        extra_b0_inhomogeneities: B0 inhomogeneities due to an extra field
        b0_inhomogeneities_timecourse: B0 inhomogeneities timecourse file
        rf_inhomogeneity_receive: RF inhomogeneity - receive
        rf_inhomogeneity_transmit: RF inhomogeneity - transmit
        activation_volume: Activation volume file
        activation_timecourse: Activation time course file
        activation_4d_volume: Activation 4D volume file
        activation_4d_timecourse: Activation 4D time course file
        level: Level of processing: 1.no motion//basic B0, 2.motion//basic B0,
            3.motion//full B0, 4.no motion//time changing B0
        num_procs: Number of processors available for parallelisation
        proc_id: ID of the processor
        no_speedup: If ON, will not do the speedup but perform signal
            calculation for all slices for each voxel
        rf_average: If ON, it will use RF angle averaging
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `PossumOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(POSSUM_METADATA)
    cargs = []
    cargs.append("possum")
    cargs.append("-i")
    cargs.append("<input")
    cargs.append("phantom")
    cargs.append("volume>")
    cargs.append("-x")
    cargs.append("<MR")
    cargs.append("parameters")
    cargs.append("matrix>")
    cargs.append("-p")
    cargs.append("<pulse>")
    cargs.append("-f")
    cargs.append("<RF")
    cargs.append("slice")
    cargs.append("profile>")
    cargs.append("-m")
    cargs.append("<motion")
    cargs.append("file>")
    cargs.append("-o")
    cargs.append("<output")
    cargs.append("signal")
    cargs.append("matrix>")
    cargs.append("[additional")
    cargs.append("options]")
    ret = PossumOutputs(
        root=execution.output_file("."),
        output_matrix=execution.output_file(f"[OUTPUT_MATRIX].mat", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "POSSUM_METADATA",
    "PossumOutputs",
    "possum",
]
