# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

RSFGEN_METADATA = Metadata(
    id="42de4c95300ddfa6a27f2ddbc5b6d9dc63cdd292.boutiques",
    name="RSFgen",
    package="afni",
    container_image_tag="afni/afni_make_build:AFNI_24.2.06",
)


class RsfgenOutputs(typing.NamedTuple):
    """
    Output object returned when calling `rsfgen(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    output_files: OutputPathType | None
    """Output .1D stimulus function files prefixed with the provided output
    prefix."""


def rsfgen(
    length: int,
    num_experimental_conditions: int,
    block_length: str | None = None,
    random_seed: float | None = None,
    suppress_output_flag: bool = False,
    single_file_flag: bool = False,
    single_column_flag: bool = False,
    output_prefix: str | None = None,
    num_reps: str | None = None,
    permutation_seed: float | None = None,
    markov_file: InputPathType | None = None,
    prob_zero: float | None = None,
    input_table: InputPathType | None = None,
    runner: Runner | None = None,
) -> RsfgenOutputs:
    """
    Program to generate random stimulus functions.
    
    Author: AFNI Developers
    
    URL: https://afni.nimh.nih.gov/
    
    Args:
        length: Length of time series.
        num_experimental_conditions: Number of input stimuli (experimental\
            conditions).
        block_length: Block length for stimulus. Must specify stimulus index\
            and length. Example: -nblock 1 5.
        random_seed: Random number seed.
        suppress_output_flag: Flag to suppress screen output.
        single_file_flag: Place stimulus functions into a single .1D file.
        single_column_flag: Write stimulus functions as a single column of\
            decimal integers.
        output_prefix: Prefix for output .1D stimulus functions.
        num_reps: Number of repetitions for stimulus.
        permutation_seed: Stim label permutation random number seed.
        markov_file: File containing the transition probability matrix.
        prob_zero: Probability of a zero (i.e., null) state (default: 0).
        input_table: Filename of column or table of numbers. All other input\
            options (except -seed and -prefix) are ignored with this option.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `RsfgenOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(RSFGEN_METADATA)
    cargs = []
    cargs.append("RSFgen")
    cargs.extend([
        "-nt",
        str(length)
    ])
    cargs.extend([
        "-num_stimts",
        str(num_experimental_conditions)
    ])
    if block_length is not None:
        cargs.extend([
            "-nblock",
            block_length
        ])
    if random_seed is not None:
        cargs.extend([
            "-seed",
            str(random_seed)
        ])
    if suppress_output_flag:
        cargs.append("-quiet")
    if single_file_flag:
        cargs.append("-one_file")
    if single_column_flag:
        cargs.append("-one_col")
    if output_prefix is not None:
        cargs.extend([
            "-prefix",
            output_prefix
        ])
    if num_reps is not None:
        cargs.extend([
            "-nreps",
            num_reps
        ])
    if permutation_seed is not None:
        cargs.extend([
            "-pseed",
            str(permutation_seed)
        ])
    if markov_file is not None:
        cargs.extend([
            "-markov",
            execution.input_file(markov_file)
        ])
    if prob_zero is not None:
        cargs.extend([
            "-pzero",
            str(prob_zero)
        ])
    if input_table is not None:
        cargs.extend([
            "-table",
            execution.input_file(input_table)
        ])
    ret = RsfgenOutputs(
        root=execution.output_file("."),
        output_files=execution.output_file(output_prefix + "1.1D") if (output_prefix is not None) else None,
    )
    execution.run(cargs)
    return ret


__all__ = [
    "RSFGEN_METADATA",
    "RsfgenOutputs",
    "rsfgen",
]
