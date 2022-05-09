
import mne
from pathlib import Path

data_path = Path(mne.datasets.sample.data_path(verbose=False))
sample_dir = data_path / 'MEG' / 'sample'
subjects_dir = data_path / 'subjects'

raw_path = sample_dir / 'sample_audvis_filt-0-40_raw.fif'

report = mne.Report(title='BEM example')
report.add_bem(
    subject='sample', subjects_dir=subjects_dir, title='MRI & BEM',
    decim=20,
    width=256
)

trans_path = sample_dir / 'sample_audvis_raw-trans.fif'


report.add_trans(
    trans=trans_path, info=raw_path, subject='sample',
    subjects_dir=subjects_dir, alpha=1.0, title='Coregistration'


)


fwd_path = sample_dir / 'sample_audvis-meg-oct-6-fwd.fif'


report.add_forward(forward=fwd_path, title='Forward solution')

report.save('report_mri_and_bem.html', overwrite=True)