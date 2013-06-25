# ZSH - Konfigurationen
        HISTFILE=~/.zsh_histfile
        HISTSIZE=1000
        SAVEHIST=1000
        unsetopt beep
        bindkey -v
        zstyle :compinstall filename '/home/joecool/.zshrc'
        autoload -U compinit && compinit

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
        PROMPT="%{$fg[red]%}%n %{$fg_no_bold[yellow]%}%~ %{$fg[red]%}$ %{$reset_color%} "
        RPROMPT=""

#Add $PATH
        export PATH=$PATH:/home/joecool/bin/
        export PATH=$PATH:/home/joecool/bin/dbgl #DosBox Game Launcher
        export PATH=$PATH:/home/joecool/Dokumente/Nand2Tetris/nand2tetris/tools/
        export PATH="$HOME/.rbenv/bin:$PATH"
        export PATH="$HOME/.rbenv/shims:$PATH"
        source "$HOME/.rbenv/completions/rbenv.zsh"
        export PATH="$HOME/.gem/ruby/2.0.0/bin:$PATH"

#ALIASES
        #Pacman
        alias pacin='sudo pacman -S'
        alias pacins='sudo pacman -U'
        alias pacrm='sudo pacman -Rscn'
        alias pacupg='sudo pacman -Syu'
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
        alias pulseaudio-restart='sudo pulseaudio -k && sudo pulseaudio -D'
        alias dropbox-restart='dropboxd -k && dropboxd '
        #Remind
        alias r-calendar='remind -c+4mb1 ~/Dropbox/Markus/Remind/.reminders'
        alias r-reminders='remind -t14g ~/Dropbox/Markus/Remind/.reminders'
        alias svim='HOME=/home/joecool && sudo vim -u ~/.vimrc'
        alias neo2='setxkbmap lv && xmodmap ~/Downloads/neo_de.xmodmap && xset -r 51'
        alias qwertz='setxkbmap de && xset r 51'
#Python
        alias p='python3'
        PYTHONPATH=/home/joecool/lib/python
        EDITOR=vim
        export PYTHONPATH EDITOR
