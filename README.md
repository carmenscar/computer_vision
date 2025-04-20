[<img src="assets/evc_banner_wide.png" alt="Especialização em Visão Computacional | https://sigmoidal.ai)" title="Especialização em Visão Computacional | https://sigmoidal.ai/en)"/>](https://sigmoidal.ai/)

<div align="center">
  
  [![Linkedin Badge](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/carlos-melo-data-science/)](https://www.linkedin.com/in/carlos-melo-data-science/)
  [![YouTube Badge](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/@CarlosMeloSigmoidal)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-E4405F?style=flat-square&logo=instagram&logoColor=white)](https://www.instagram.com/carlos_melo.py)
  [![Twitter Badge](https://img.shields.io/twitter/follow/:carlos_melo_py)](https://twitter.com/carlos_melo_py)

</div>

# Especialização em Visão Computacional

Este repositório é dedicado à "Especialização em Visão Computacional". Eu segui os passos abaixo para configurar o ambiente de desenvolvimento local e instalar as dependências utilizadas durante as aulas.

## Pré-requisitos

* **VSCode** - Editor de código utilizado durante o treinamento. Disponível para Windows, macOS e Linux. [Instalação oficial do VSCode](https://code.visualstudio.com/download)

* **Pyenv** - Ferramenta para gerenciar múltiplas versões do Python. A versão recomendada do Python para este projeto é a `3.11.3`. [Instruções oficiais de instalação do Pyenv](https://github.com/pyenv/pyenv#installation)

Eu segui os seguintes passos no meu WSL:Ubuntu:

1. Baixei o pyenv:
   ```bash
   curl -fsSL https://pyenv.run | bash
   ```
2. Em um novo terminal eu verifiquei qual shell eu estava usando (no caso /bin/bash)
   ```bash
   echo $SHELL
   ```
3. Editei o arquivo ".bashrc", abrindo ele no editor:
   ```bash
   code ~/.bashrc
   ```

   PS: caso eu não estivesse usando o /bin/bash, eu usaria outros arquivos de configuração.
   Abaixo seguem as opções:
   | Shell            | Comando `echo $SHELL` retorna | Arquivo de configuração                            |
   |------------------|-------------------------------|----------------------------------------------------|
   | **Bash**         | `/bin/bash`                   | `~/.bashrc` (ou `~/.bash_profile` no macOS)        |
   | **Zsh**          | `/bin/zsh`                    | `~/.zshrc`                                         |
   | **Fish**         | `/usr/bin/fish`               | `~/.config/fish/config.fish`                       |
   | **Dash, Sh etc.**| Pode variar                   | Pode exigir configurações no sistema ou `.profile` |

4. Após abrir, colei as seguintes linhas no final do arquivo:
   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   [[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)" 
   ```

5. Para instalar o pyenv precisei antes intalar algumas dependencias de sistema (pois quando fui fazer um "pyenv install"tive um erro de  build failed)
   ```bash
   sudo apt update && sudo apt install -y \
   make build-essential libssl-dev zlib1g-dev \
   libbz2-dev libreadline-dev libsqlite3-dev wget curl \
   llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
   libxmlsec1-dev libffi-dev liblzma-dev
   ```

* **Poetry** - Ferramenta de gerenciamento de dependências em Python. [Instruções oficiais de instalação do Poetry](https://python-poetry.org/docs/#installation)
Eu fiz os seguintes passos para fazer a instalação do poetry
1. Fiz a instalação do poetry que me gerou um path(incluído no passo 3)
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```
2. Precisei novamente editar o arquivo .bashrc para incluir esse path:
   ```bash
   code ~/.bashrc
   ```
3. Ao final do  arquivo, adicionei a seguinte linha (sugerida pela instalação no passo 1):
   ```bash
   # >>> poetry config >>> 
   export PATH="/home/carmenscar/.local/bin:$PATH"
   # <<< poetry config <<<
   ```

4. adiconei o codigo abaixo para Ajustar a formatação da minha linha de comando que estava desconfigurada

   ```bash
   __update_prompt() {
      local venv_name=""
      if [[ -n "$VIRTUAL_ENV" ]]; then
         venv_name="(.venv)"  # Mostra (.venv) para ambientes do Poetry
      elif [[ -n "$PYENV_VERSION" ]]; then
         venv_name="($PYENV_VERSION)"  # Mostra (nome) para Pyenv puro
      fi
      PS1="${venv_name}\u@\h:\w\$ "
   }
   PROMPT_COMMAND=__update_prompt
   ```

Para executar no terminal as atualizações do poetry e do pyenv:
   ```bash
   source ~/.bashrc
   ```
Essas atualizações que foram feitas no bashrc preparam o ambiente com pyenv e poetry. 

* **Git** - Ferramenta de controle de versão distribuído. [Instruções oficiais de instalação do Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

* **GitHub** - Plataforma de hospedagem de código. É essencial ter uma conta para interagir com os repositórios. [Como criar uma conta no GitHub](https://docs.github.com/pt/get-started/onboarding/getting-started-with-your-github-account)

## Instalação e Configuração

Aqui está um resumo dos passos que você precisa seguir:

1. Clonar o [Repositório Github](https://github.com/carlosfab/visao-computacional) para a sua máquina local e acessar a pasta `visao-computacional`:

   ```bash
   git clone https://github.com/carlosfab/visao-computacional.git
   cd visao-computacional
   ```

2. Configurar o Poetry para criar ambientes virtuais dentro do diretório do projeto.

   ```bash
   poetry config virtualenvs.in-project true
   ```

3. Configurar a versão `3.11.3` do Python com Pyenv:

   ```bash
   pyenv install 3.11.3
   pyenv local 3.11.3
   ```

5. instalar e ativar as dependencias do projeto:
   ```bash
   poetry install
   ```
6. Rodar os testes que o curso sugeriu pra ter certeza que mmeu ambiente estava funcionando corretamente:
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

7. Ao abrir o vscode, meu ambiente virtual ja estava fazendo a ativação automatica, então eu não precisei digitar "poetry shell". Lembre-se de entrar na pasta "computer_vision" (cd computer vision) e ativar o ambiente virtual caso isso não esteja acontecendo de maneira automatica (poetry shell)

8. Para ativar o setup do kernel para rodar o jupyter digite:
   ```bash
   poetry run task register_kernel
   ```
Ao fechar e abrir verifique se o kernel já esta ativo. Caso esteja não é necessário rodar essa task
verifique com 
   ```bash
   poetry run jupyter kernelspec list
   ```
Caso o kernel "jupyter_poetry_kernel" esteja na lista não é necessário ativa-lo, porém as vezes o vscode demora a reconhecer e você precisa ajustar o noetebook (as vezes o proprio vscode sugere o uso do kernel .venv) para selecionar p kernel do caminho .venv ()

* **PS**: Para rodar o notebook no vscode precisei fazer alguns ajustes no arquivo original .toml. Foi necessário fixar as versões das bibliotecas opencv-python, ultralytics, mediapipe e numpy. Sempre que eu tentava fazer o import cv2 no notebook o kernel crashava e isso foi resolvido fixando a bibilioteca do open cv o que acabou levando a fixar as outras também. O poetry deveria fazer a gestão mas pode ter ocorrido algum problema que eu não investiguei mais profundamente mas foi resolvido instalando bibliotecas nativas (libgl1, ffmpeg, etc) e fixando as bibiliotecas no .toml.



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
