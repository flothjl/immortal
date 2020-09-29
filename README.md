# Immortal
A cli to manage and install dotfiles, among other likely-useless stuff 👨🏼‍🌾

The ultimate reason this project was started was because I'm close to being in the market for a new personal laptop and wanted to faciliate the transition. 

#### Dotfile Installation

```bash
immortal dotfiles install --file /my/config.yaml
```
Example config.yaml
```yaml
- type: zsh
  base-path: /Users/joshuafloth/Developer/immortal/config/dotfiles/
  files:
    - path: ~/.dotfiles/zshrc
      destination: ~/.zshrc
  name: oh-my-zsh
  install-file: "install.sh"
  themes:
    - install-file: "p10k.sh"
- type: generic
  files:
    - path: ~/.dotfiles/ssh/config
      destination: ~/.ssh/config
```

<small>Cheers 🍻</small>

