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
### Pyenv
#### 1. Download do pyenv
Execute o comando abaixo na linha de comando do VSCODE para fazer o download do pyenv:
   ```bash
   curl -fsSL https://pyenv.run | bash
   ```

Após a instalação, o terminal mostrará instruções sobre quais configurações adicionar ao seu arquivo de configuração do shell.

#### 2. Instalação das Dependências do Sistema
Antes de usar o pyenv, é essencial instalar estas dependências no Ubuntu:
    ```bash
    sudo apt update && sudo apt install -y \
    make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl \
    llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev
    ```
Essa etapa previne erros como "Build failed" ao instalar versões do Python.

##### 3. Configuração do ambiente shell

###### 3.1. Verifique qual shell está usando:
   ```bash
   echo $SHELL
   ```

###### 3.2. Edite o Arquivo de Configuração

Abra o arquivo correspondente ao seu shell:

| Shell Detectado       | Arquivo de Configuração          | Comando para Editar               |
|-----------------------|----------------------------------|-----------------------------------|
| **Bash** (`/bin/bash`)| `~/.bashrc` ou `~/.bash_profile` | `code ~/.bashrc`                  |
| **Zsh** (`/bin/zsh`)  | `~/.zshrc`                       | `code ~/.zshrc`                   |
| **Fish**              | `~/.config/fish/config.fish`     | `code ~/.config/fish/config.fish` |

##### 3.3. Adicione as Configurações 
As configurações foram exibidas na etapa 1 (informações após CURL) e são semelhantes as configurações abaixo:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)" 
   ```
### Poetry

#### 1. Download do Poetry
Execute o comando abaixo na linha de comando do VSCODE para fazer o download do poetry:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
Ao final da instalação, será mostrado o path que precisa ser adicionado ao seu shell(próximo passo).

#### 2. Edite o Arquivo de Configuração (mesmo do passo 3.2 do pyenv)
A informação a ser incluinda será semelhante a abaixo:
   ```bash
   # >>> poetry config >>> 
   export PATH="/home/carmenscar/.local/bin:$PATH"
   # <<< poetry config <<<
   ```

### Aplique as alterações do bash incluídas (pyenv e poetry)
No terminal:
   ```bash
   source ~/.bashrc
   ```

## Instalação do Projeto
#### 1. Clonar o [Repositório Github](https://github.com/carmenscar/computer_vision) para a sua máquina local e acessar a pasta `computer_vision`. Você pode clonar o arquivo original do curso mas não tem todas as atualizações feitas por mim no arquivo .toml. Essas atualizações pra que o ambiente do jupyter funcionasse adequadamente dentro do meu VSCODE:

   ```bash
   git clone https://github.com/carmenscar/computer_vision.git
   cd visao-computacional
   ```

#### 2. Configurar o Poetry para criar ambientes virtuais dentro do diretório do projeto.

   ```bash
   poetry config virtualenvs.in-project true
   ```

#### 3. Configurar a versão `3.11.3` do Python com Pyenv:

   ```bash
   pyenv install 3.11.3
   pyenv local 3.11.3
   ```

#### 4. Instalar as dependencias do projeto:
   ```bash
   poetry install
   ```

#### 5. Verificação do ambiente:
   ```bash
   poetry run task test
   ```
O resultado foi:
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

## Configuração do Jupyter
Essas configurações foram feitas pra conseguir rodar o Jupyter no kernell adequado no ambiente do VScode com as dependências gerenciadas pelo poetry

#### 1. Ativação Automática do Ambiente
   ```bash
    poetry self add poetry-shell-plugin
    poetry shell
   ```

#### 2. Ative o setup do kernel para rodar o jupyter notebook:
   ```bash
   poetry run task setup_jupyter
   ```

#### 3.  Procure pelo kernel "Python (Poetry)" no ambiente do VSCode para rodar os notebooks

## **🚀 Material de apoio por módulo**

| Módulo | Descrição | Link para o Notebook |
|--------|-----------|----------------------|
| **1 - Introdução à Visão Computacional** | Apresentação do conteúdo do curso, conceitos fundamentais da Visão Computacional e introdução ao OpenCV. | [Notebook 1](notebooks/01_introducao_a_visao_computacional.ipynb) |
| **2 - Fundamentos do Processamento de Imagens** | Conceitos básicos das técnicas de manipulação de imagens no Processamento de Imagens. | [Notebook 2](notebooks/02_fundamentos_do_processamento_de_imagens.ipynb) |
| **3 - Filtragem e Aprimoramento de Imagens** | Técnicas de filtragem e aprimoramento de imagens e detecção de contornos baseada em bordas. | [Atualizando...](https://github.com/carlosfab/visao-computacional/blob/main/notebooks/) |
| **4 - Detecção Facial e Pontos de Referência** | Técnicas para detecção facial e identificação de pontos de referência (*landmarks*). | [Notebook 4](notebooks/04_deteccao_facial_e_landmarks.ipynb) |
| **Módulo 5 - Detecção de Objetos com *Deep Learning*** | Desenvolvimento de modelos para detecção de objetos, introdução ao TensorFlow e YOLOv8 para detecção de objetos em tempo real. | [Atualizando...](https://github.com/carlosfab/visao-computacional/blob/main/notebooks/) |

## 🚀 Projetos

Atualmente, os projetos da Especialização em Visão Computacional estão disponíveis apenas na plataforma de cursos do Sigmoidal (ao final de cada módulo), mas em breve serão atualizados neste repositório 🔥.

<p align="left">
<a href="projetos/projeto_01/" title="Detecção e Substituição de Fundo em Vídeos (Chroma Key)"><img src="assets/projeto_01_thumb.png" alt="Detecção e Substituição de Fundo em Vídeos (Chroma Key)" width="300px" align="left" /></a>
<a href="projetos/projeto_01/" title="Detecção e Substituição de Fundo em Vídeos (Chroma Key)"><strong>Chroma Keying para criação de cenários</strong></a>
<div><strong>Projeto 01</strong> | <strong>Atualizado: 8 Nov 2023</strong></div>
<br/> Neste primeiro projeto do curso, você irá implementar um algoritmo capaz de identificar e isolar o range de intensidade do fundo verde, e substituí-lo por um cenário alternativo (que pode ser uma imagem estática ou um outro vídeo qualquer...</p>

#

<p align="left">
<a href="#" title="Análise de Desmatamento através de Imagens de Satélite"><img src="assets/projeto_02_thumb.png" alt="Análise de Desmatamento através de Imagens de Satélite" width="300px" align="left" /></a>
<a href="#" title="Análise de Desmatamento através de Imagens de Satélite"><strong>Análise de Desmatamento através de Imagens de Satélite</strong></a>
<div><strong>Projeto 02</strong> | <strong>Em Atualização...</strong></div>
<br/> Neste projeto você irá aprender a usar recursos de sensoriamento remoto para detectar desmatamentos em regiões de florestas. Especificamente, exploraremos imagens do satélite Landsat 8 (OLI/TIRS) usando a biblioteca Google Earth Engine (GEE)... </p>

#

<p align="left">
<a href="#" title="Reconhecimento e Contagem de Moedas"><img src="assets/projeto_03_thumb.png" alt="Reconhecimento e Contagem de Moedas" width="300px" align="left" /></a>
<a href="#" title="Reconhecimento e Contagem de Moedas"><strong>Reconhecimento e Contagem de Moedas</strong></a>
<div><strong>Projeto 03</strong> | <strong>Em Atualização...</strong></div>
<br/> Neste projeto você irá desenvolver um *script* para detectar e identificar diferentes tipos de moedas, além de calcular o valor total das moedas detectadas a partir de vídeos gravaods ou transmissões em tempo real via webcam...</p>

#

<p align="left">
<a href="#" title="Alarme para Detecção de Intrusos"><img src="assets/projeto_04_thumb.png" alt="Alarme para Detecção de Intrusos" width="300px" align="left" /></a>
<a href="#" title="Alarme para Detecção de Intrusos"><strong>Alarme para Detecção de Intrusos</strong></a>
<div><strong>Projeto 04</strong> | <strong>Em Atualização...</strong></div>
<br/> Este projeto tem como objetivo desenvolver um sistema de vigilância utilizando técnicas de processamento de imagem para detectar movimentos a partir de uma câmera externa. Serão utilizadas técnicas para isolar o fundo com uma máscara...</p><br/>

## Sobre o Instrutor

<p align="left">
Carlos Melo é <strong>Engenheiro de Visão Computacional</strong> com formação em Ciências Aeronáuticas pela Academia da Força Aérea e <strong>Mestrado em Engenharia Aeroespacial</strong> pelo Instituto Tecnológico de Aeronáutica (ITA).
</p>

### Contato

Para dúvidas, sugestões ou feedbacks:

* **Carlos Melo** - [Contato](https://sigmoidal.ai/contato/)
