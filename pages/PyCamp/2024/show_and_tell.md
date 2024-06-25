.. title: Show & Tell 2024
.. slug: showntell2024

El **Show & Tell** de herramientas y configuraciones fue una de las actividades que realizamos en el [PyCamp2024](link://post_path/PyCamp/2024) y post evento se armó un grupo de Telegram [Show&Tell](https://t.me/+cvDe4Dk5nV1kZjIx) para seguir manijeando.

### Andre

**Sublime-Text**

[Filter Lines](https://packagecontrol.io/packages/Filter%20Lines)

[CoolBase64](https://packagecontrol.io/packages/CoolBase64)  lo uso para decodear el contenido de un archivo en un servidor al que me conecto por SSH, y que previamente encodeo


### Facu

**python**

auto-import mágico 

Implementación que [Andre](#andre) compartió por el grupo.

```python
import importlib
import sys

original_hook = sys.excepthook

def my_hook(type_, value, traceback):
    if type_ is not NameError:
        original_hook(type_, value, traceback)
        return

    module_name = value.args[0].split("'")[1]

    print(f'Attempting to import module "{module_name}"')

    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f'Module "{module_name}" not found, resuming normal flow')
        original_hook(type_, value, traceback)
        return

    globals()[module_name] = module

sys.excepthook = my_hook
```

### Fede

[tmuxinator](https://github.com/tmuxinator/tmuxinator)

**VSCode**

[Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers)

**Extras**

[dokur windows](https://github.com/dockur/windows) / 
[dokur macOS](https://github.com/dockur/macos)

    Una que no dije pero que esta buenísima por si alguien necesita probar algo en windows o macOS desde un linux. 
    Esos repos levanta un windows (tenes versiones de windows server, xp,. vista, 7, ... 11 pro, 11 enterprise, etc y en distintos idiomas)  o un macOS (también hay varias versiones y todo) adentro de un docker con qemu y podes entrar a la interfaz gráfica por vnc desde el navegador directamente.

### Fisa

[eg]()

[tig](https://github.com/jonas/tig) interfaz de texto para git

[fd](https://github.com/sharkdp/fd) buscador de archivos, alternativa moderna de `find` 

**aliases**


### José Luis

[RSS feed](https://newsboat.org/) lector de RSS en la terminal

**browser**

[Vimium](https://vimium.github.io/) bindings de VIM para el navegador

### Marian

[fish shell](https://fishshell.com/) shell moderna, alternativa a `bash`

[ranger](https://github.com/ranger/ranger) un administrador de archivos en la consola

[fzf](https://github.com/junegunn/fzf) / [zoxide](https://github.com/ajeetdsouza/zoxide)

    Fuzzy finder es una genialidad que te permite saltar de directorio a directorio, ya que memoriza los últimos usados y te da agilidad para cambiarte de uno a otro.
    Además podés tener un visualizador y buscador de variables de entorno, ultimos comandos, archivos, procesos, git status y log.


**Extras**

[lazygit](https://github.com/jesseduffield/lazygit)

    Una interfaz TUI para Git. Permite hacer casi toda operación mucho más rápido. 
    Tiene una ayuda que aparece con ?, es muy completa. Destaca la facilidad para hacer cherry pick, copiando commits de branch a branch.


### Osiux


**Extras**

[duf](https://github.com/muesli/duf/) en lugar de `df` uso `duf` y obvio uso `df` como alias de `duf` 

[fdupes](https://github.com/adrianlopezroche/fdupes) para eliminar fácilmente archivos duplicados

```bash
cd ~/fotos
fdupes -dNr .
```

> Gran parte de lo que mostré en Show & Tell esta mejor explicado en la Charla [Conectando Soluciones](https://osiux.com/2024-04-27-flisol-caba-2024-conectando-soluciones.html)


### Sasha

[helix](https://helix-editor.com/) editor de texto en la terminal (similar a `vim`) con muchos features para desarrollo ya configurados por default (lsp, syntax-highlight, movements....)

[bat](https://github.com/sharkdp/bat) alternativa de `cat` con syntax highlight

[nix]()

[buscador de paquetes](https://search.nixos.org/packages) (como `pypi.org`)

**emacs**

[which-key](https://github.com/justbur/emacs-which-key)

**git**

```bash
ssh config
```

**VSCode**

[Path Intellisense](https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense) para autocompletado inteligente de paths en cualquier tipo de archivo, muy útil para trabajar en markdown.

**Windows**

[Scoop](https://scoop.sh/) es un instalador de línea de comando (como `apt`) en Windows

[Windows Terminal](https://github.com/microsoft/terminal)

[PowerToys](https://github.com/microsoft/PowerToys) herramientas de "productividad", recomiendo PowerToysRun y Keyboard Manager.

**browser**

[I still don't care about cookies](https://github.com/OhMyGuus/I-Still-Dont-Care-About-Cookies)

**Extras**

[gitui](https://github.com/extrawurst/gitui) otra TUI de git


### SKA

[vcsh](https://github.com/RichiH/vcsh) Configuración centralizda de dotfiles

[myrepos](https://myrepos.branchable.com/)

> [Guía](https://srijanshetty.in/technical/vcsh-mr-dotfiles-nirvana/) con ejemplos

[powerlevel10k ](https://github.com/romkatv/powerlevel10k )

> Prompt multishell con la posibilidad de configurarlo como "transient prompt" y que vaya borrando el prompt luego de correr cada comando 

**vim**

[astrovim](https://astronvim.com/) Configuración de Neovim "cheta" lista para usar

**Extras**

Me quedó mostrar [Syncthing](https://syncthing.net/) para sincronización de archivos peer to peer. Lo uso para sincronizar mi [Logseq](https://logseq.com/)

### Zoe

[zsh + ohmyzsh](https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH)

**VSCode**

[GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)
