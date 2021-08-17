## A Speech Dataset Collected From the Data Structure Course by Prof. Yang
This repository contains .The original audio data are downloaded from the [YouTube playlist](https://youtube.com/playlist?list=PLs81hTyfCaoXSa8NVmVy7IZVzJLpNhglk) and can be downloaded at the [release].

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



