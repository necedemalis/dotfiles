# ZSH - Konfigurationen
        HISTFILE=~/.zsh_histfile
        HISTSIZE=1000
        SAVEHIST=1000
        unsetopt beep
        bindkey -v
        zstyle :compinstall filename '/home/joecool/.zshrc'
        autoload -U compinit && compinit #Autocomplete

#Präambel
        export EDITOR="vim"
        export MOZ_DISABLE_PANGO=1

#History Search
        [[ -n "${key[PageUp]}"   ]]  && bindkey  "${key[PageUp]}"    history-beginning-search-backward
        [[ -n "${key[PageDown]}" ]]  && bindkey  "${key[PageDown]}"  history-beginning-search-forward

#Tmux
        [[ $- != *i* ]] && return
        [[ $TERM != screen* ]] && exec tmux
        if which tmux 2>&1 >/dev/null; then
            #if not inside a tmux session, and if no session is started, start a new session
            test -z "$TMUX" && (tmux attach || tmux new-session)
        fi

#Keybindings
        bindkey -M viins 'jk' vi-cmd-mode

#Set VIMODE 
        function zle-line-init zle-keymap-select {
            RPS1="${${KEYMAP/vicmd/-- N --}/(main|viins)/-- I --}"
            zle reset-prompt
        }
        zle -N zle-line-init
        zle -N zle-keymap-select

#Prompt
        autoload -U promptinit
        promptinit
        autoload -U colors && colors

        if [ -n "$(pacman -Qs zsh-syntax-highlighting)" ] ; then
                PROMPT="┌─ %{$fg[red]%}%n %{$fg_no_bold[yellow]%}%~ %{$fg[red]%}$ %{$reset_color%}
└──╼ "
        else
                PROMPT="┌─ %{$fg[red]%}%n %{$fg_no_bold[yellow]%}%~ %{$fg[red]%}$ %{$reset_color%}
└──> "
        fi

        if [ -n "$SSH_CLIENT" ] ; then
                RPROMPT="SSH"
        else
                RPROMPT=""
        fi

#Add $PATH
        export PATH=$PATH:/home/joecool/bin/
        export PATH=$PATH:/home/joecool/bin/dbgl #DosBox Game Launcher
        if [ -z "$HOME/.rbenv" ] ; then
                export PATH="$HOME/.rbenv/bin:$PATH"
                export PATH="$HOME/.rbenv/shims:$PATH"
                source "$HOME/.rbenv/completions/rbenv.zsh"
        fi
        if [ -z "$HOME/.gem" ] ; then
                export PATH="$HOME/.gem/ruby/2.0.0/bin:$PATH"
        fi

#ALIASES
        #Pacman
        alias pacin='sudo pacman -S'
        alias pacins='sudo pacman -U'
        alias pactest='sudo pacman -S --asdeps'
        alias pacrm='sudo pacman -Rscn'
        alias pacupg='sudo pacman -Syu'
        alias pacrep='sudo pacman -Si'
        alias pacreps='sudo pacman -Ss'
        alias pacloc='sudo pacman -Qi'
        alias paclocs='sudo pacman -Qs'
        alias pacro="/usr/bin/pacman -Qtdq > /dev/null && sudo /usr/bin/pacman -Rs \$(/usr/bin/pacman -Qtdq | sed -e ':a;N;\$!ba;s/\n/ /g')" # '[r]emove [o]rphans' - recursively remove ALL orphaned packages
        #alias expacshow="expac "%n %N" -Q $(expac "%n %G" | grep -v ' base') | awk '$2 == "" {print $1}'" # Listing all packages that nothing else depends on
        #Ein/aushängen
        alias mntext='sudo mount -t ntfs-3g -o defaults UUID="A24A74BF4A749231" /media/Extern'
        alias umntext='sudo umount /media/Extern'
        #untar
        alias t='tar -xvzf'
        #Backups
        #System Backup
        alias backup-system='sudo ~/scripts/backup.sh /media/Extern/aaa/Backups/Arch-Backup'
        #Jazz Backup
        alias backup-jazz='rsync -P -r -a --delete /media/Extern/aaa/Museion/Jazz/ /media/Daten/Backup/Jazz-Backup/'
        #Dropbox Backup
        alias backup-dropbox='rsync -P -r -a --delete ~/Dropbox/ /media/Daten/Backup/Dropbox-Backup/'
        #suspend/hibernate
        alias suspend='sudo pm-suspend'
        alias hibernate='sudo pm-hibernate'
        #Restart
        alias dropbox-stop='sudo systemctl stop dropbox@joecool.service'
        alias dropbox-start='sudo systemctl start dropbox@joecool.service'
        #Remind
        alias r-calendar='remind -c+4mb1 ~/Dropbox/Markus/Remind/.reminders'
        alias r-reminders='remind -t14g ~/Dropbox/Markus/Remind/.reminders'
        #Keyboard Map
        alias neo2='setxkbmap lv && xmodmap ~/.Xmodmap/neo_de.xmodmap && xset -r 51'
        alias qwertz_custom='setxkbmap lv && xmodmap ~/.Xmodmap/neo_de_custom.xmodmap && xset -r 51' #qwertz mit Neo2-Ebene 3+
        alias qwertz='setxkbmap de && xset r 51'

        alias catalyst='sudo aticonfig --sync-video=on; sudo aticonfig --sync-vsync=on; sudo aticonfig --set-pcs-u32=DDX,EnableTearFreeDesktop,1'

#Python
        alias p='python3'
        PYTHONPATH=/home/joecool/lib/python
        EDITOR=vim
        export PYTHONPATH EDITOR

# Syntac-Hightlight/Override highlighter colors
#if [ -n "$(pacman -Qs zsh-syntax-highlighting)" ] ; then
if [ -z "/usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh" ] ; then
        source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh

        ZSH_HIGHLIGHT_STYLES[default]=none
        ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=red,bold
        ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=green
        ZSH_HIGHLIGHT_STYLES[alias]=none
        ZSH_HIGHLIGHT_STYLES[builtin]=none
        ZSH_HIGHLIGHT_STYLES[function]=none
        ZSH_HIGHLIGHT_STYLES[command]=none
        ZSH_HIGHLIGHT_STYLES[precommand]=none
        ZSH_HIGHLIGHT_STYLES[commandseparator]=none
        ZSH_HIGHLIGHT_STYLES[hashed-command]=none
        ZSH_HIGHLIGHT_STYLES[path]='none'
        ZSH_HIGHLIGHT_STYLES[globbing]=none
        ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue
        ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=none
        ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=none
        ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
        ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
        ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
        ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=cyan
        ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=cyan
        ZSH_HIGHLIGHT_STYLES[assign]=none
        ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets)
fi
