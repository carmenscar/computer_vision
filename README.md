[<img src="assets/evc_banner_wide.png" alt="Computer Vision Specialization | https://sigmoidal.ai" title="Computer Vision Specialization | https://sigmoidal.ai/en)"/>](https://sigmoidal.ai/)
# Computer Vision Specialization
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/packaging-poetry-yellowgreen)](https://python-poetry.org/)

This repository contains my projects and improvements for the "Computer Vision Specialization". Based on the [original course code](https://github.com/carlosfab/visao-computacional), I've added:

- ✔️ Improved setup documentation  
- ✔️ Optimized configuration for Jupyter Notebooks  
- ✔️ Solutions for common dependency issues  

## Table of Contents
- [Prerequisites](#prerequisites)
- [Environment Setup](#environment-setup)
- [Project Installation](#project-installation)
- [Jupyter Configuration](#jupyter-configuration)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)

---

## Prerequisites

### 📋 Required Software
| Tool            | Version  | Installation Guide |
|-----------------|---------|--------------------|
| VSCode          | Latest  | [Site](https://code.visualstudio.com/download) |
| Pyenv           | 2.3.0+  | [GitHub](https://github.com/pyenv/pyenv#installation) |
| Poetry          | 1.8.0+  | [Docs](https://python-poetry.org/docs/#installation) |
| Git             | 2.40+   | [Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |

### 💻 WSL Configuration
Open PowerShell on Windows and install WSL:
   ```powershell
   wsl --install
   ```
Create a folder in your Linux system, open VSCODE and connect to WSL.

## Environment Setup
### Pyenv
#### 1. Install pyenv
   Run the following command in VSCODE terminal to install pyenv:
   ```bash
   curl -fsSL https://pyenv.run | bash
   ```

After installation, the terminal will display instructions for additional shell configuration settings to add.

#### 2. Install System Dependencies
Before using pyenv, these Ubuntu dependencies must be installed:
   ```bash
   sudo apt update && sudo apt install -y \
   make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl \
   llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
   libxmlsec1-dev libffi-dev liblzma-dev
   ```
This step prevents "Build failed" errors when installing Python versions.

#### 3. Shell Environment Configuration

##### 3.1. Check which shell you're using:
   ```bash
   echo $SHELL
   ```

##### 3.2. Edit Configuration File

Open the configuration file corresponding to your shell:

| Shell Detected        | Configuration File               | Edit command                      |
|-----------------------|----------------------------------|-----------------------------------|
| **Bash** (`/bin/bash`)| `~/.bashrc` or `~/.bash_profile` | `code ~/.bashrc`                  |
| **Zsh** (`/bin/zsh`)  | `~/.zshrc`                       | `code ~/.zshrc`                   |
| **Fish**              | `~/.config/fish/config.fish`     | `code ~/.config/fish/config.fish` |

##### 3.3. Configure Environment
The settings shown after the CURL command (step 1) should match these configurations:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   ```

### Poetry

#### 1. Install Poetry
Run the following command in the VS Code terminal to install Poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
After successful installation, the terminal will display the PATH environment variable that needs to be configured (covered in next step).

#### 2. Edit Configuration File (same as pyenv step 3.2)
The information to be added will be similar to:
   ```bash
   # >>> poetry config >>> 
   export PATH="/home/carmenscar/.local/bin:$PATH"
   # <<< poetry config <<<
   ```

### Apply the bash configuration changes (pyenv and poetry)
In the terminal run:
   ```bash
   source ~/.bashrc
   ```

## Project Installation
#### 1. Clone the [Github Repository](https://github.com/carmenscar/computer_vision) to your local machine and navigate to the `computer_vision` folder. You can clone the original course files, but they won't include all the updates I made to the .toml file. These updates were necessary to make the Jupyter environment work properly in my VS Code setup:

   ```bash
   git clone https://github.com/carmenscar/computer_vision.git
   cd visao-computacional
   ```

#### 2. Configure Poetry's virtualenv location
Set Poetry to create virtual environments inside the project folder:

   ```bash
   poetry config virtualenvs.in-project true
   ```

#### 3. Set Python version `3.11.3` using Pyenv:

   ```bash
   pyenv install 3.11.3
   pyenv local 3.11.3
   ```

#### 4. Install all project dependencies:
   ```bash
   poetry install
   ```

#### 5. Environment Verification:
   ```bash
   poetry run task test
   ```
The expected output showing successful environment configuration should be similar to:

   ```bash
   ================================= test session starts ===========================================
   platform linux -- Python 3.11.3, pytest-8.3.5, pluggy-1.5.0 -- /home/carmenscar/computer_vision/visao-computacional/.venv/bin/python
   cachedir: .pytest_cache
   rootdir: /home/carmenscar/computer_vision/visao-computacional
   configfile: pyproject.toml
   plugins: anyio-4.9.0
   collected 1 item                                                                                                    

   tests/test_setup.py::test_python_version PASSED                                                               [100%]

   ================================= 1 passed in 0.02s ============================================
   ```

## Jupyter Configuration
These configurations were implemented to properly run Jupyter notebooks in VS Code with Poetry-managed dependencies.

#### 1. Automatic Environment Activation
   ```bash
    poetry self add poetry-shell-plugin
    poetry shell
   ```

#### 2. Set up the Jupyter kernel
Configure the Jupyter kernel to work with the Poetry environment:
   ```bash
   poetry run task setup_jupyter
   ```

#### 3. Select the "Python (Poetry)" kernel in VS Code
To run the notebooks, choose the "Python (Poetry)" kernel from the kernel selector in VS Code.

## **🚀 Support Materials by Module**

## 🚀 Support Materials by Module

### add module architeture here### (WIP)

