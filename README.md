## A Speech Dataset Collected From the Data Structures Course by Prof. Yang
This repository contains the audio data from the recordings of [CSE215, Data Structures](http://par.cse.nsysu.edu.tw/~cbyang/course/ds/ds_index.htm) lectured by Professor [C. B. Yang](http://par.cse.nsysu.edu.tw/~cbyang/), and the preprocessing scripts. The original audio data are downloaded from the [YouTube playlist](https://youtube.com/playlist?list=PLs81hTyfCaoXSa8NVmVy7IZVzJLpNhglk) and can be downloaded at the [release](https://github.com/ernestchu/yang-ds-speech/releases/tag/0.0.1).

The original audio data is saved in **m4a** format. Nevertheless, we'll use **wav** during preprocessing for the performance concerns and thus a sufficient disk capacity is recommended.

## Preprocessing
Make sure to checkout the [environment guide](#prepare-environment) before trying any scripts.

### Noise reduction
First, make sure the original audio data are available.
```
.
├── scripts
│   ├── noise-reduction.py
│   └── segment.py
└── original.tar.gz
```
Extract the original audio data by `tar -xzf original.tar.gz`. Then perform the noise reduction by
```sh
python3 scripts/noise-reduction.py
```
You'll get a directory `noise-reduced` full of denoised audio data

### Create 5 sec segment
```sh
python3 scripts/segment.py
```

## Prepare environment
### Create virtual environment
It's always good to give your python project a dedicated environment (where pip packages installed) via **venv**.
```sh
python3 -m venv .venv --system-site-packages
source .venv/bin/activate
```
You'll get something like this in your terminal
```sh
(.venv) username@devicename $
```
If you want to exit the environment
```sh
deactivate
```

You can also check the status by
```sh
which pip
```
This should give you the path to your dedicated pip executable within `.venv`.

### Uninstall the environment
Remove `.venv` and remove the IPython kernel
```sh
rm -rf .venv
jupyter kernelspec remove tsm
```
### Install required packages
After activate the virtual environment
```sh
pip intall -r requirement.txt
```



