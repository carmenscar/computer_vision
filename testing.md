[<img src="assets/evc_banner_wide.png" alt="Especialização em Visão Computacional | https://sigmoidal.ai)" title="Especialização em Visão Computacional | https://sigmoidal.ai/en)"/>](https://sigmoidal.ai/)
# Especialização em Visão Computacional
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/badge/packaging-poetry-yellowgreen)](https://python-poetry.org/)

Este repositório contém meus projetos e melhorias para a "Especialização em Visão Computacional". Partindo do [código original do curso](https://github.com/carlosfab/visao-computacional), adicionei:

- ✔️ Melhor documentação do setup
- ✔️ Configuração otimizada para Jupyter Notebooks
- ✔️ Soluções para problemas comuns de dependências

## Índice
- [Pré-requisitos](#pré-requisitos)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Instalação do Projeto](#instalação-do-projeto)
- [Configuração do Jupyter](#configuração-do-jupyter)
- [Solução de Problemas](#solução-de-problemas)
- [FAQ](#faq)

---

## Pré-requisitos

### 📋 Software Necessário
| Ferramenta       | Versão  | Guia de Instalação |
|------------------|---------|--------------------|
| VSCode           | Latest  | [Site](https://code.visualstudio.com/download) |
| Pyenv            | 2.3.0+  | [GitHub](https://github.com/pyenv/pyenv#installation) |
| Poetry           | 1.8.0+  | [Docs](https://python-poetry.org/docs/#installation) |
| Git              | 2.40+   | [Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) |

### 💻 Configuração WSL
Abra o PowerShell no windows e instale o WSL
```powershell
wsl --install
```
Crie uma pasta no seu Linux, abra seu VSCODE e faça a conexão com WSL.

## Configuração do Ambiente

1. Download do pyenv
Execute o comando abaixo na linha de comando do VSCODE para fazer o download do pyenv:
   ```bash
   curl -fsSL https://pyenv.run | bash
   ```

Após a instalação, o terminal mostrará instruções sobre quais configurações adicionar ao seu arquivo de configuração do shell.

2. Instalação das Dependências do Sistema
Antes de usar o pyenv, é essencial instalar estas dependências no Ubuntu:
    ```bash
    sudo apt update && sudo apt install -y \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl \
    llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev
    ```
Essa etapa previne erros como "Build failed" ao instalar versões do Python.

3. Configuração do ambiente shell

### 3.1. Verifique qual shell está usando:
   ```bash
   echo $SHELL
   ```

### 3.2: Edite o Arquivo de Configuração

Abra o arquivo correspondente ao seu shell:

| Shell Detectado       | Arquivo de Configuração          | Comando para Editar               |
|-----------------------|----------------------------------|-----------------------------------|
| **Bash** (`/bin/bash`)| `~/.bashrc` ou `~/.bash_profile` | `code ~/.bashrc`                  |
| **Zsh** (`/bin/zsh`)  | `~/.zshrc`                       | `code ~/.zshrc`                   |
| **Fish**              | `~/.config/fish/config.fish`     | `code ~/.config/fish/config.fish` |

### 3.3: Adicione as Configurações 
As configurações foram exibidas na etapa 1 (informações após CURL) e são semelhantes as configurações abaixo:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)" 
   ```

