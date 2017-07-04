# Set the correct encoding settings.
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Define the username that is displayed.
export USER='fousa'

# Set name of the theme to load.
ZSH_THEME="agnoster"

# Set the installed plugins
plugins=(git git-flow rails ruby)

source $ZSH/oh-my-zsh.sh

### Setup ZSK syntax highlighting.
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

###############
### ALIASES ###
###############

### Developer
alias gt='gittower'
alias br='bundle exec rake'
alias be='bundle exec'
alias pi='pod install'

### Git
alias gffs='git flow feature start'
alias gfff='git flow feature finish'
alias gs='git shortlog -s -n --all'

############
### PATH ###
############

### User
export PATH="/usr/local/bin:/bin:/usr/sbin:/sbin:/usr/bin"

### Postgres.app
export PATH="/Applications/Postgres.app/Contents/Versions/9.6/bin:$PATH"

### rbenv
export PATH="$HOME/.rbenv/bin:$PATH"
eval "$(rbenv init -)"
