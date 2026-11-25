<h1 align="center">app-forward</h1>

<p align="center">
  Builds an MNE-Python HTML report showing the FreeSurfer BEM surfaces and an MEG forward solution.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.627"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.627-blue.svg" alt="Run on brainlife.io"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Builds an MNE-Python HTML report showing the FreeSurfer BEM surfaces and an MEG forward solution.**

Code on the repository's main branch adds the subject's MRI and BEM surfaces (from the FreeSurfer directory) and the forward solution to an mne.Report and saves report.html. The registered branch 'master' no longer exists in the repository, so the App cannot be staged as registered. The transform input is declared as an ICA datatype but is read as a head-MRI transform and then not used.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/ica` · `neuro/meeg/mne/forward-inverse` · `neuro/freesurfer` |
| **Outputs** | `report/html` |
| **Container** | `brainlife/mne:1.0.2` |
| **Resources** | 8 CPUs · 0.17 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.627](https://doi.org/10.25663/brainlife.app.627) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `transform` | `neuro/meeg/mne/ica` | yes | Head-to-MRI transform file; read by the code but not used. |
| `forward` | `neuro/meeg/mne/forward-inverse` | yes | MNE forward solution (-fwd.fif) to show in the report. |
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directory with BEM surfaces. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir_report` | `report/html` | report.html with the MRI/BEM figures and the forward solution. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.627](https://doi.org/10.25663/brainlife.app.627), choose `neuro/meeg/mne/ica`, `neuro/meeg/mne/forward-inverse`, `neuro/freesurfer` from your project and press **Execute**. The results are saved to your project as `report/html`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlife/mne:1.0.2`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "transform": "/path/to/transform/transform",
       "forward": "/path/to/forward/forward",
       "freesurfer": "/path/to/freesurfer/freesurfer"
   }
   ```

3. Run `./main`.

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- app-forward. brainlife.io App. [doi:10.25663/brainlife.app.627](https://doi.org/10.25663/brainlife.app.627)
- Fischl. FreeSurfer. *NeuroImage* 62:774-781 (2012). [doi:10.1016/j.neuroimage.2012.01.021](https://doi.org/10.1016/j.neuroimage.2012.01.021)
- Gramfort et al. MEG and EEG data analysis with MNE-Python. *Frontiers in Neuroscience* 7 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

Maintained by [@zahransa](https://github.com/zahransa).
