
import mne
from pathlib import Path

import json

#to fix
#qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

with open('config.json') as config_json:
    config = json.load(config_json)

    # Read the meg file
fwd_path= config.pop('forward')
#subjects_dir= config.pop('output')
subject_dir='../62bcba44fd504b9f17ad2be0/61164b436135cd2478c53c88'
trans_path = config.pop('transform')

subject='output'




report = mne.Report(title='BEM example')
report.add_bem(
    subject=subject, subjects_dir=subjects_dir, title='MRI & BEM',
    decim=20,
    width=256
)



report.add_forward(forward=fwd_path, title='Forward solution')
report.save('out_dir_report/report.html', overwrite=True)
