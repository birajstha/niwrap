# This file was auto generated by styx
# Do not edit this file directly

import dataclasses
import pathlib
import typing

from styxdefs import *


VOLUME_MATH_METADATA = Metadata(
    id="58ee3192dd278e3aeb1b1bc93411172a6b20be67",
    name="volume-math",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


@dataclasses.dataclass
class VolumeMathVar:
    """
    a volume file to use as a variable
    """
    opt_subvolume_subvol: str | None = None
    """select a single subvolume: the subvolume number or name"""
    opt_repeat: bool = False
    """reuse a single subvolume for each subvolume of calculation"""
    
    def run(
        self,
        execution: Execution,
    ) -> list[str]:
        """
        Build command line arguments. This method is called by the main command.
        
        Args:
            self: The sub-command object.
            execution: The execution object.
        Returns:
            
        """
        cargs = []
        if self.opt_subvolume_subvol is not None:
            cargs.extend(["-subvolume", self.opt_subvolume_subvol])
        if self.opt_repeat:
            cargs.append("-repeat")
        return cargs


class VolumeMathOutputs(typing.NamedTuple):
    """
    Output object returned when calling `volume_math(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""
    volume_out: OutputPathType
    """the output volume"""


def volume_math(
    expression: str,
    volume_out: InputPathType,
    opt_fixnan_replace: float | int | None = None,
    var: list[VolumeMathVar] = None,
    runner: Runner = None,
) -> VolumeMathOutputs:
    """
    volume-math by Washington University School of Medicin.
    
    Evaluate expression on volume files.
    
    This command evaluates <expression> at each voxel independently. There must
    be at least one -var option (to get the volume space from), even if the
    <name> specified in it isn't used in <expression>. All volumes must have the
    same volume space. Filenames are not valid in <expression>, use a variable
    name and a -var option with matching <name> to specify an input file. If the
    -subvolume option is given to any -var option, only one subvolume is used
    from that file. If -repeat is specified, the file must either have only one
    subvolume, or have the -subvolume option specified. All files that don't use
    -repeat must have the same number of subvolumes requested to be used. The
    format of <expression> is as follows:
    
    Expressions consist of constants, variables, operators, parentheses, and
    functions, in infix notation, such as 'exp(-x + 3) * scale'. Variables are
    strings of any length, using the characters a-z, A-Z, 0-9, and _, but may
    not take the name of a named constant. Currently, there is only one named
    constant, PI. The operators are +, -, *, /, ^, >, <, >=, <=, ==, !=, !, &&,
    ||. These behave as in C, except that ^ is exponentiation, i.e. pow(x, y),
    and takes higher precedence than other binary operators (also, '-3^-4^-5'
    means '-(3^(-(4^-5)))'). The <=, >=, ==, and != operators are given a small
    amount of wiggle room, equal to one millionth of the smaller of the absolute
    values of the values being compared.
    
    Comparison and logical operators return 0 or 1, you can do masking with
    expressions like 'x * (mask > 0)'. For all logical operators, an input is
    considered true iff it is greater than 0. The expression '0 < x < 5' is not
    syntactically wrong, but it will NOT do what is desired, because it is
    evaluated left to right, i.e. '((0 < x) < 5)', which will always return 1,
    as both possible results of a comparison are less than 5. A warning is
    generated if an expression of this type is detected. Use something like 'x >
    0 && x < 5' to get the desired behavior.
    
    Whitespace between elements is ignored, ' sin ( 2 * x ) ' is equivalent to
    'sin(2*x)', but 's in(2*x)' is an error. Implied multiplication is not
    allowed, the expression '2x' will be parsed as a variable. Parentheses are
    (), do not use [] or {}. Functions require parentheses, the expression 'sin
    x' is an error.
    
    The following functions are supported:
    
    sin: 1 argument, the sine of the argument (units are radians)
    cos: 1 argument, the cosine of the argument (units are radians)
    tan: 1 argument, the tangent of the argument (units are radians)
    asin: 1 argument, the inverse of sine of the argument, in radians
    acos: 1 argument, the inverse of cosine of the argument, in radians
    atan: 1 argument, the inverse of tangent of the argument, in radians
    atan2: 2 arguments, atan2(y, x) returns the inverse of tangent of (y/x), in
    radians, determining quadrant by the sign of both arguments
    sinh: 1 argument, the hyperbolic sine of the argument
    cosh: 1 argument, the hyperbolic cosine of the argument
    tanh: 1 argument, the hyperbolic tangent of the argument
    asinh: 1 argument, the inverse hyperbolic sine of the argument
    acosh: 1 argument, the inverse hyperbolic cosine of the argument
    atanh: 1 argument, the inverse hyperbolic tangent of the argument
    sinc: 1 argument, sinc(0) = 1, sin(x) / x otherwise
    ln: 1 argument, the natural logarithm of the argument
    exp: 1 argument, the constant e raised to the power of the argument
    log: 1 argument, the base 10 logarithm of the argument
    log2: 1 argument, the base 2 logarithm of the argument
    sqrt: 1 argument, the square root of the argument
    abs: 1 argument, the absolute value of the argument
    floor: 1 argument, the largest integer not greater than the argument
    round: 1 argument, the nearest integer, with ties rounded away from zero
    ceil: 1 argument, the smallest integer not less than the argument
    min: 2 arguments, min(x, y) returns y if (x > y), x otherwise
    max: 2 arguments, max(x, y) returns y if (x < y), x otherwise
    mod: 2 arguments, mod(x, y) = x - y * floor(x / y), or 0 if y == 0
    clamp: 3 arguments, clamp(x, low, high) = min(max(x, low), high)
    .
    
    Args:
        expression: the expression to evaluate, in quotes
        volume_out: the output volume
        opt_fixnan_replace: replace NaN results with a value: value to replace
            NaN with
        var: a volume file to use as a variable
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `VolumeMathOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(VOLUME_MATH_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-volume-math")
    cargs.append(expression)
    cargs.append(execution.input_file(volume_out))
    if opt_fixnan_replace is not None:
        cargs.extend(["-fixnan", str(opt_fixnan_replace)])
    if var is not None:
        cargs.extend(["-var", *[a for c in [s.run(execution) for s in var] for a in c]])
    ret = VolumeMathOutputs(
        root=execution.output_file("."),
        volume_out=execution.output_file(f"{pathlib.Path(volume_out).stem}"),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "VOLUME_MATH_METADATA",
    "VolumeMathOutputs",
    "VolumeMathVar",
    "volume_math",
]
