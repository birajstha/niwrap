# This file was auto generated by Styx.
# Do not edit this file directly.

from styxdefs import *
import pathlib
import typing

WPNG_METADATA = Metadata(
    id="dd95d5c9953d753a616b57dafba4a2490df31e17",
    name="wpng",
)


class WpngOutputs(typing.NamedTuple):
    """
    Output object returned when calling `wpng(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_file: OutputPathType
    """Converted PNG file"""


def wpng(
    input_file: InputPathType | None = None,
    gamma: float | int | None = None,
    bgcolor: str | None = None,
    text_flag: bool = False,
    time_flag: bool = False,
    interlace_flag: bool = False,
    runner: Runner | None = None,
) -> WpngOutputs:
    """
    wpng by Unknown.
    
    Simple PGM/PPM/PAM to PNG Converter.
    
    Args:
        input_file: Input PNM file (binary PGM 'P5', PPM 'P6' or PAM 'P8').
        gamma: Transfer-function exponent (``gamma'') of the image in\
            floating-point format (e.g., ``0.45455''). If image looks correct on\
            given display system, image gamma is equal to inverse of display-system\
            exponent, i.e., 1 / (LUT * CRT) (where LUT = lookup-table exponent and\
            CRT = CRT exponent; first varies, second is usually 2.2, all are\
            positive).
        bgcolor: Desired background color for alpha-channel images, in\
            7-character hex RGB format (e.g., ``#ff7700'' for orange: same as HTML\
            colors).
        text_flag: Prompt interactively for text info (tEXt chunks).
        time_flag: Include a tIME chunk (last modification time).
        interlace_flag: Write interlaced PNG image.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `WpngOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(WPNG_METADATA)
    cargs = []
    cargs.append("wpng")
    if gamma is not None:
        cargs.extend(["-gamma", str(gamma)])
    if bgcolor is not None:
        cargs.extend(["-bgcolor", bgcolor])
    if text_flag:
        cargs.append("-text")
    if time_flag:
        cargs.append("-time")
    if interlace_flag:
        cargs.append("-interlace")
    if input_file is not None:
        cargs.append(execution.input_file(input_file))
    ret = WpngOutputs(
        root=execution.output_file("."),
        output_file=execution.output_file(f"[INPUT_FILE_BASE_NAME].png", optional=True),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "WPNG_METADATA",
    "WpngOutputs",
    "wpng",
]
