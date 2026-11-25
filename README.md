# app-forward

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Builds an MNE-Python HTML report showing the FreeSurfer BEM surfaces and an MEG forward solution.**

Code on the repository's main branch adds the subject's MRI and BEM surfaces (from the FreeSurfer directory) and the forward solution to an mne.Report and saves report.html. The registered branch 'master' no longer exists in the repository, so the App cannot be staged as registered. The transform input is declared as an ICA datatype but is read as a head-MRI transform and then not used.

| | |
|---|---|
| 📥 **Inputs** | `neuro/meeg/mne/ica` · `neuro/meeg/mne/forward-inverse` · `neuro/freesurfer` |
| 📤 **Outputs** | `report/html` |
| 🐳 **Container** | `brainlife/mne:1.0.2` |
| ⚙️ **Resources** | 8 CPUs · 0.17 h walltime |
| 🔗 **Run it** | [doi.org/10.25663/brainlife.app.627](https://doi.org/10.25663/brainlife.app.627) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `transform` | `neuro/meeg/mne/ica` | yes | Head-to-MRI transform file; read by the code but not used. |
| `forward` | `neuro/meeg/mne/forward-inverse` | yes | MNE forward solution (-fwd.fif) to show in the report. |
| `freesurfer` | `neuro/freesurfer` | yes | FreeSurfer subject directory with BEM surfaces. |

#### 📤 Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_dir_report` | `report/html` | report.html with the MRI/BEM figures and the forward solution. |

<!-- brainlife-app:end -->

