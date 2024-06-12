# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

PULSE_METADATA = Metadata(
    id="5fd32e85eaac71412c384fa108df01143f5cf12b",
    name="pulse",
    container_image_type="docker",
    container_image_index="index.docker.io",
    container_image_tag="mcin/docker-fsl:6.0.5",
)


class PulseOutputs(typing.NamedTuple):
    """
    Output object returned when calling `pulse(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_pulse_sequence_matrix: OutputPathType
    """Pulse sequence matrix output"""


def pulse(
    input_file: InputPathType,
    output_base: str,
    seq: str | None = "epi",
    angle: float | int | None = 90,
    te: float | int | None = 0.03,
    tr: float | int | None = 3,
    trslc: float | int | None = 0.12,
    nx: float | int | None = 64,
    ny: float | int | None = 64,
    dx: float | int | None = 0.004,
    dy: float | int | None = 0.004,
    max_g: float | int | None = 0.055,
    riset: float | int | None = 0.00022,
    bw: float | int | None = 100000,
    numvol: float | int | None = 1,
    numslc: float | int | None = 1,
    slcthk: float | int | None = 0.006,
    gap: float | int | None = 0,
    zstart: float | int | None = 0,
    slcdir: str | None = "z-",
    phasedir: str | None = "y+",
    readdir: str | None = "x+",
    verbose_flag: bool = False,
    kcoord_flag: bool = False,
    cover: float | int | None = None,
    runner: Runner = None,
) -> PulseOutputs:
    """
    pulse by University of Oxford (Ivana Drobnjak and Mark Jenkinson).
    
    Generates a pulse sequence matrix for a given digital brain image.
    
    More information: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Pulse
    
    Args:
        input_file: 4D digital brain, resolution can be any.
        output_base: Output base name.
        seq: Type of pulse sequence; default=epi (epi OR ge).
        angle: Flip angle in degrees; default=90.
        te: The time from the first RF to the first echo; default=0.03s.
        tr: The time between the two RF pulses applied on the same part of the\
            object; default=3s.
        trslc: The time that takes for the acquisition of one slice;\
            default=0.12s.
        nx: Resolution in x of the output image; default=64.
        ny: Resolution in y of the output image; default=64.
        dx: Image voxel x-dimension; default=0.004m.
        dy: Image voxel y-dimension; default=0.004m.
        max_g: Maximum gradient strength; default=0.055 T/m.
        riset: Time it takes for the gradient to reach its max value;\
            default=0.00022s.
        bw: Receiving bandwidth; default=100000Hz.
        numvol: Number of volumes; default=1.
        numslc: Number of slices; default=1.
        slcthk: Slice thickness; default=0.006m.
        gap: Gap between the slices in meters; default=0m.
        zstart: The lowest position in the slice direction in meters;\
            default=0m.
        slcdir: Slice acquisition direction/orientation; default=z- (x+,x-,\
            y+,y- or z+,or z-).
        phasedir: Phase encode direction/orientation; default=y+ (x+,x-, y+,y-\
            or z+,or z-).
        readdir: Read-out direction/orientation; default=x+ (x+,x-, y+,y- or\
            z+,or z-).
        verbose_flag: Switch on diagnostic messages.
        kcoord_flag: Save k-space coordinates; default=no.
        cover: Phase partial Fourier coverage in percentage; default=100\
            (min=50, max=100).
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `PulseOutputs`).
    """
    runner = runner or get_global_runner()
    if cover is not None and not (50 <= cover <= 100): 
        raise ValueError(f"'cover' must be between 50 <= x <= 100 but was {cover}")
    execution = runner.start_execution(PULSE_METADATA)
    cargs = []
    cargs.append("pulse")
    cargs.append("-i")
    cargs.extend(["-i", execution.input_file(input_file)])
    cargs.append("-o")
    cargs.extend(["-o", output_base])
    if seq is not None:
        cargs.extend(["--seq", seq])
    if angle is not None:
        cargs.extend(["--angle", str(angle)])
    if te is not None:
        cargs.extend(["--te", str(te)])
    if tr is not None:
        cargs.extend(["--tr", str(tr)])
    if trslc is not None:
        cargs.extend(["--trslc", str(trslc)])
    if nx is not None:
        cargs.extend(["--nx", str(nx)])
    if ny is not None:
        cargs.extend(["--ny", str(ny)])
    if dx is not None:
        cargs.extend(["--dx", str(dx)])
    if dy is not None:
        cargs.extend(["--dy", str(dy)])
    if max_g is not None:
        cargs.extend(["--maxG", str(max_g)])
    if riset is not None:
        cargs.extend(["--riset", str(riset)])
    if bw is not None:
        cargs.extend(["--bw", str(bw)])
    if numvol is not None:
        cargs.extend(["--numvol", str(numvol)])
    if numslc is not None:
        cargs.extend(["--numslc", str(numslc)])
    if slcthk is not None:
        cargs.extend(["--slcthk", str(slcthk)])
    if gap is not None:
        cargs.extend(["--gap", str(gap)])
    if zstart is not None:
        cargs.extend(["--zstart", str(zstart)])
    if slcdir is not None:
        cargs.extend(["--slcdir", slcdir])
    if phasedir is not None:
        cargs.extend(["--phasedir", phasedir])
    if readdir is not None:
        cargs.extend(["--readdir", readdir])
    if verbose_flag:
        cargs.append("-v")
    if kcoord_flag:
        cargs.append("-k")
    if cover is not None:
        cargs.extend(["--cover", str(cover)])
    ret = PulseOutputs(
        root=execution.output_file("."),
        output_pulse_sequence_matrix=execution.output_file(f"{output_base}_pulsesequence_matrix"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "PULSE_METADATA",
    "PulseOutputs",
    "pulse",
]
