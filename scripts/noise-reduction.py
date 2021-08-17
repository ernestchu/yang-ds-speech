import audioread
import numpy as np
import noisereduce as nr
import soundfile as sf
import glob
import os

def load(file_path, start=None, end=None, verbose=False):
    '''
    args:
      file_path(str): file to load
      start(scalar, optional): start time in second. Default: `None`
      end(scalar, optional): end time in second. Default: `None`
      verbose(bool, optional): print additional messages. Default: `False`
    notes:
      - If you don't understand some syntax, please refer to short-circuiting behavior in operator and, or
      - Supported audio file extenstion: please refer to the `audioread` package
      - Albeit its bad performance, it can decode .m4a files
    '''
    nc = sr = du = None # num channels, sample rate, and duration
    x = []
    
    with audioread.audio_open(file_path) as f:
        nc, sr, du = f.channels, f.samplerate, f.duration
        verbose and print(f'number of channels: {nc}, sample rate: {sr}Hz, duration: {du:.3f}s')
        [x.extend(np.frombuffer(buf, dtype='int16').tolist()) for buf in f]
        
    x = np.array(x, np.int16).reshape(-1, nc).T # seperate channels
    verbose and print(f'data shape: {x.shape}')
    
    t_start = start or 0
    t_end   = end   or None
        
    x = x[:, t_start*sr:(end and end*sr)]
    return x, sr

os.makedirs('noise-reduced', exist_ok=True)
file_list = glob.glob('original/*.m4a')

for file in file_list:
    x, sr = load(file)
    reduced_noise = nr.reduce_noise(x, sr, stationary=True, n_std_thresh_stationary=0.5, n_jobs=-1)
    basename = file.split('/')[-1]
    sf.write(f'noise-reduced/{basename[:-3]}wav', reduced_noise.T, sr)
    
