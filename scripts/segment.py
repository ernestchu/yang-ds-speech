import numpy as np
import glob
import os
import torchaudio

os.makedirs('noise-reduced', exist_ok=True)
file_list = glob.glob('noise-reduced/*.wav')

for file in file_list:
    x, sr = torchaudio.load(file)
    assert len(x.shape) == 2
    
    basename = file.split('/')[-1]

    os.makedirs(f'data/{basename[:-4]}', exist_ok=True)

    for i in range(0, x.shape[1], 5*sr):
        torchaudio.save(f'data/{basename[:-4]}/{i//(5*sr):04}.wav', x[:, i: i+5*sr], sr)
