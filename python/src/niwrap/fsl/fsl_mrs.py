# This file was auto generated by Styx.
# Do not edit this file directly.

import typing
import pathlib
from styxdefs import *
import dataclasses

FSL_MRS_METADATA = Metadata(
    id="d80204b557139acdcc98d0c5bde0734e2d60b693.boutiques",
    name="fsl_mrs",
    package="fsl",
    container_image_tag="mcin/fsl:6.0.5",
)


class FslMrsOutputs(typing.NamedTuple):
    """
    Output object returned when calling `fsl_mrs(...)`.
    """
    root: OutputPathType
    """Output root folder. This is the root folder for all outputs."""


def fsl_mrs(
    data: InputPathType,
    basis: InputPathType,
    output: str,
    algo: str | None = None,
    ignore_metab: list[str] | None = None,
    keep_metab: list[str] | None = None,
    combine_metab: list[str] | None = None,
    ppmlim: list[float] | None = None,
    h2o_file: InputPathType | None = None,
    baseline_order: float | None = None,
    metab_groups: list[str] | None = None,
    add_mm_flag: bool = False,
    add_mm_mega_flag: bool = False,
    lorentzian_flag: bool = False,
    ind_scaling: list[str] | None = None,
    disable_mh_priors_flag: bool = False,
    t1_image: InputPathType | None = None,
    te: float | None = None,
    tr: float | None = None,
    tissue_frac: list[str] | None = None,
    internal_ref: list[str] | None = None,
    wref_metabolite: str | None = None,
    ref_protons: float | None = None,
    ref_int_limits: list[float] | None = None,
    h2o_scale: float | None = None,
    report_flag: bool = False,
    verbose_flag: bool = False,
    overwrite_flag: bool = False,
    conj_fid: bool = False,
    no_conj_fid: bool = False,
    conj_basis: bool = False,
    no_conj_basis: bool = False,
    no_rescale: bool = False,
    config: InputPathType | None = None,
    runner: Runner | None = None,
) -> FslMrsOutputs:
    """
    FSL Magnetic Resonance Spectroscopy Wrapper Script.
    
    Author: FMRIB Analysis Group, University of Oxford
    
    URL: https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    
    Args:
        data: Input FID file.
        basis: .BASIS file or folder containing basis spectra (will read all\
            files within).
        output: Output folder.
        algo: Algorithm [Newton (fast, default) or MH (slow)].
        ignore_metab: Ignore certain metabolites [repeatable].
        keep_metab: Only keep these metabolites.
        combine_metab: Combine certain metabolites [repeatable].
        ppmlim: Limit the fit to a frequency range (default=(.2,4.2)).
        h2o_file: Input .H2O file for quantification.
        baseline_order: Order of baseline polynomial (default=2, -1 disables).
        metab_groups: Metabolite groups: list of groups or list of names for\
            independent groups.
        add_mm_flag: Include default macromolecule peaks.
        add_mm_mega_flag: Include default MEGA-PRESS macromolecule peaks. This\
            option is experimental!.
        lorentzian_flag: Enable purely Lorentzian broadening (default is Voigt).
        ind_scaling: List of basis spectra to scale independently of other\
            basis spectra.
        disable_mh_priors_flag: Disable MH priors.
        t1_image: Structural image (for report).
        te: Echo time for relaxation correction (ms).
        tr: Repetition time for relaxation correction (s).
        tissue_frac: Fractional tissue volumes for WM, GM, CSF or json\
            segmentation file. Defaults to pure water scaling.
        internal_ref: Metabolite(s) used as an internal reference. Defaults to\
            tCr (Cr+PCr).
        wref_metabolite: Metabolite(s) used as the reference for water scaling.\
            Uses internal defaults otherwise.
        ref_protons: Number of protons that reference metabolite is equivalent\
            to. No effect without setting --wref_metabolite.
        ref_int_limits: Reference spectrum integration limits (low, high). No\
            effect without setting --wref_metabolite.
        h2o_scale: Additional scaling modifier for external water referencing.
        report_flag: Output HTML report.
        verbose_flag: Spit out verbose info.
        overwrite_flag: Overwrite existing output folder.
        conj_fid: Force conjugation of FID.
        no_conj_fid: Forbid automatic conjugation of FID.
        conj_basis: Force conjugation of basis.
        no_conj_basis: Forbid automatic conjugation of basis.
        no_rescale: Forbid rescaling of FID/basis/H2O.
        config: Configuration file.
        runner: Command runner.
    Returns:
        NamedTuple of outputs (described in `FslMrsOutputs`).
    """
    runner = runner or get_global_runner()
    execution = runner.start_execution(FSL_MRS_METADATA)
    cargs = []
    cargs.append("fsl_mrs")
    cargs.append(execution.input_file(data))
    cargs.append(execution.input_file(basis))
    cargs.append(output)
    if algo is not None:
        cargs.extend([
            "--algo",
            algo
        ])
    if ignore_metab is not None:
        cargs.extend([
            "--ignore",
            *ignore_metab
        ])
    if keep_metab is not None:
        cargs.extend([
            "--keep",
            *keep_metab
        ])
    if combine_metab is not None:
        cargs.extend([
            "--combine",
            *combine_metab
        ])
    if ppmlim is not None:
        cargs.extend([
            "--ppmlim",
            *map(str, ppmlim)
        ])
    if h2o_file is not None:
        cargs.extend([
            "--h2o",
            execution.input_file(h2o_file)
        ])
    if baseline_order is not None:
        cargs.extend([
            "--baseline_order",
            str(baseline_order)
        ])
    if metab_groups is not None:
        cargs.extend([
            "--metab_groups",
            *metab_groups
        ])
    if add_mm_flag:
        cargs.append("--add_MM")
    if add_mm_mega_flag:
        cargs.append("--add_MM_MEGA")
    if lorentzian_flag:
        cargs.append("--lorentzian")
    if ind_scaling is not None:
        cargs.extend([
            "--ind_scale",
            *ind_scaling
        ])
    if disable_mh_priors_flag:
        cargs.append("--disable_MH_priors")
    if t1_image is not None:
        cargs.extend([
            "--t1",
            execution.input_file(t1_image)
        ])
    if te is not None:
        cargs.extend([
            "--TE",
            str(te)
        ])
    if tr is not None:
        cargs.extend([
            "--TR",
            str(tr)
        ])
    if tissue_frac is not None:
        cargs.extend([
            "--tissue_frac",
            *tissue_frac
        ])
    if internal_ref is not None:
        cargs.extend([
            "--internal_ref",
            *internal_ref
        ])
    if wref_metabolite is not None:
        cargs.extend([
            "--wref_metabolite",
            wref_metabolite
        ])
    if ref_protons is not None:
        cargs.extend([
            "--ref_protons",
            str(ref_protons)
        ])
    if ref_int_limits is not None:
        cargs.extend([
            "--ref_int_limits",
            *map(str, ref_int_limits)
        ])
    if h2o_scale is not None:
        cargs.extend([
            "--h2o_scale",
            str(h2o_scale)
        ])
    if report_flag:
        cargs.append("--report")
    if verbose_flag:
        cargs.append("--verbose")
    if overwrite_flag:
        cargs.append("--overwrite")
    if conj_fid:
        cargs.append("--conj_fid")
    if no_conj_fid:
        cargs.append("--no_conj_fid")
    if conj_basis:
        cargs.append("--conj_basis")
    if no_conj_basis:
        cargs.append("--no_conj_basis")
    if no_rescale:
        cargs.append("--no_rescale")
    if config is not None:
        cargs.extend([
            "--config",
            execution.input_file(config)
        ])
    ret = FslMrsOutputs(
        root=execution.output_file("."),
    )
    execution.run(cargs)
    return ret


__all__ = [
    "FSL_MRS_METADATA",
    "FslMrsOutputs",
    "fsl_mrs",
]
