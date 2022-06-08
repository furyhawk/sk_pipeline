# sk_pipeline
 
## Local Setup
The following instructions should work on Linux, Windows and MacOS. If you are a Windows user familiar with Linux, you should check out the [Windows Subsystem for Linux, Version 2 (WSL2)](https://docs.microsoft.com/en-us/windows/wsl/).

### Python virtual env setup
For local setup, I recommend to use [Miniconda](https://docs.conda.io/en/latest/miniconda.html), a minimal version of the popular [Anaconda](https://www.anaconda.com/) distribution that contains only the package manager `conda` and Python. Follow the installation instructions on the [Miniconda Homepage](https://docs.conda.io/en/latest/miniconda.html).

After installation of Anaconda/Miniconda, run the following command(s) from the project directory:

### Requirements
* Python >= `3.10`
* Packages included in `requirements.txt` file
* (Anaconda for easy installation)

### Install dependencies
```sh
conda create --name myenv python=3.10
conda activate myenv
conda install --file requirements.txt -c conda-forge
```

## Usage
Activate and install the correct python3 env before proceeding.

This will run the Survive classification task using XGBoost:
```sh
chmod +x run.sh
./run.sh
```

or

```sh
cd src/
python3 main.py -c configs/config_xgb.json
```