"""
Transposes csv files copied/pasted from ktrn-06-03-1067286-s001/Table S1.xlsx and saves them as a txt file for rtfbsdb
(Save to a folder that we zip to mimic CisDB zip file).
"""

import os
import glob
import pandas as pd
import pathlib

OUTDIR = './core_promoter_pwms/pwms_all_motifs/'
pathlib.Path(OUTDIR).mkdir(parents=True, exist_ok=True)

for f in glob.glob('*.csv'):
	df = pd.read_csv(f, header=None, index_col=0)
	T = df.T
	T['Pos'] = T['Pos'].astype(int)
	out_path = os.path.join(OUTDIR, '%s.txt' % f.split('.')[0])
	T.to_csv(out_path, sep='\t', index=False)
