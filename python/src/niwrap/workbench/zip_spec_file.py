# This file was auto generated by Styx.
# Do not edit this file directly.

import pathlib
import typing

from styxdefs import *


ZIP_SPEC_FILE_METADATA = Metadata(
    id="31589ac899c3dda0868712af0f1d5390ddfb5543",
    name="zip-spec-file",
    container_image_type="docker",
    container_image_tag="fcpindi/c-pac:latest",
)


class ZipSpecFileOutputs(typing.NamedTuple):
    """
    Output object returned when calling `zip_spec_file(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def zip_spec_file(
    spec_file: str,
    extract_folder: str,
    zip_file: str,
    opt_base_dir_directory: str | None = None,
    opt_skip_missing: bool = False,
    runner: Runner = None,
) -> ZipSpecFileOutputs:
    """
    zip-spec-file by Washington University School of Medicin.
    
    Zip a spec file and its data files.
    
    If zip-file already exists, it will be overwritten. If -base-dir is not
    specified, the directory containing the spec file is used for the base
    directory. The spec file must contain only relative paths, and no data files
    may be outside the base directory. Scene files inside spec files are not
    checked for what files they reference, ensure that all data files referenced
    by the scene files are also referenced by the spec file.
    
    Args:
        spec_file: the specification file to add to zip file
        extract_folder: the name of the folder created when the zip file is
            unzipped
        zip_file: out - the zip file that will be created
        opt_base_dir_directory: specify a directory that all data files are
            somewhere within, this will become the root of the zipfile's directory
            structure: the directory
        opt_skip_missing: any missing files will generate only warnings, and the
            zip file will be created anyway
        runner: Command runner
    Returns:
        NamedTuple of outputs (described in `ZipSpecFileOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(ZIP_SPEC_FILE_METADATA)
    cargs = []
    cargs.append("wb_command")
    cargs.append("-zip-spec-file")
    cargs.append(spec_file)
    cargs.append(extract_folder)
    cargs.append(zip_file)
    if opt_base_dir_directory is not None:
        cargs.extend(["-base-dir", opt_base_dir_directory])
    if opt_skip_missing:
        cargs.append("-skip-missing")
    ret = ZipSpecFileOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "ZIP_SPEC_FILE_METADATA",
    "ZipSpecFileOutputs",
    "zip_spec_file",
]
