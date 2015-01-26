# ZSH - Konfigurationen

#Präambel
        export EDITOR="vim"
        export MOZ_DISABLE_PANGO=1
        HISTFILE=~/.zsh_histfile
        HISTSIZE=1000
        SAVEHIST=1000
        unsetopt beep
        bindkey -v
        zstyle :compinstall filename '/home/joecool/.zshrc'
        autoload -U compinit && compinit #Autocomplete

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

#Environmental Variables, PATH
        #export PATH=${PATH}:"$HOME/bin"
        #export PATH=${PATH}:"$HOME/.local/bin"
        #export DIFFPROG=$DIFFPROG:/usr/bin/meld
        #export BROWSER=$BROWSER/usr/bin/firefox
        #Xdg user directories:
        #[[ -z $XDG_CONFIG_HOME ]] && export XDG_CONFIG_HOME="$HOME/.config" && export XDG_DATA_HOME="$HOME/.local/share" && export XDG_CACHE_HOME="$HOME/.cache" && XDG_DOWNLOAD_DIR="$HOME/Downloads" && XDG_DOCUMENTS_DIR="$HOME/Dokumente"
        #Privoxy for Surf:
        #http_proxy=http://127.0.0.1:8118/
        #HTTP_PROXY=$http_proxy
        #export http_proxy HTTP_PROXY

#Start Keychain for SSH-Agent & GPG-Agent
if [[ -z $(pidof ssh-agent) && -z $(pidof gpg-agent) ]]; then #don't show on zsh start
        eval $(keychain --eval)
        ssh-add -l >/dev/null || alias ssh='ssh-add -l >/dev/null || ssh-add && unalias ssh; ssh' 
fi
export GPG_TTY=$(tty)
export GPG_AGENT_INFO=$HOME/.gnupg/S.gpg-agent

#ALIASES
        #Pacman
        alias pacin='sudo pacmatic -S'
        alias pacins='sudo pacmatic -U'
        alias pactest='sudo pacmatic -S --asdeps'
        alias pacrm='sudo pacman -Rscn'
        alias pacupg='sudo pacmatic -Syu'
        alias pacrep='sudo pacman -Si'
        alias pacreps='sudo pacman -Ss'
        alias pacloc='sudo pacman -Qi'
        alias paclocs='sudo pacman -Qs'
        alias pacro="/usr/bin/pacman -Qtdq > /dev/null && sudo /usr/bin/pacman -Rs \$(/usr/bin/pacman -Qtdq | sed -e ':a;N;\$!ba;s/\n/ /g')" # '[r]emove [o]rphans' - recursively remove ALL orphaned packages
        alias paclocatefiles="locate -e --regex '\.pac(new|orig|save)$'" #Find .pac* files (.pacnew,pacsave,pacorig)
        #Ein/aushängen
        alias mntext='sudo mount -t ntfs-3g -o defaults UUID="A24A74BF4A749231" /media/Extern'
        alias umntext='sudo umount /media/Extern'
        #untar tar.gz
        alias t='tar -xvzf'
        #suspend/hibernate/shutdown
        alias suspend='sudo systemctl suspend'
        alias shutdown='sudo shutdown -h 0'
        alias hibernate='sudo pm-hibernate'
        #Remind
        alias calendar='remind -c+4mb1 ~/Dokumente/Remind/.reminders'
        alias r-reminders='remind -t14g ~/Dokumente/Remind/.reminders'
        alias calendar-print='remind -p ~/Dokumente/Remind/.reminders| rem2ps > remind.ps | lpr remind.ps'
        #Keyboard Map
        alias neo2='setxkbmap lv && xmodmap ~/.Xmodmap/neo_de.xmodmap && xset -r 51'
        alias qwertz_custom='setxkbmap lv && xmodmap ~/.Xmodmap/neo_de_custom.xmodmap && xset -r 51' #qwertz mit Neo2-Ebene 3+
        alias qwertz='setxkbmap de && xset r 51'
        #Diversers
        alias raspberrypi='ssh root@192.168.0.165 -l pi'
        alias resolution='xrandr -s 1680x1050'
        alias screenshot='import -window root screenshot.jpg'
        alias pdfjoin_norotate='pdfjoin --rotateoversize false'
        alias audio_restart='pulseaudio --kill && jack_control stop && jack_control start && pulseaudio --start'
        alias ksp='cd / && LC_ALL=C ni ./media/Daten/Installationen/Spiele/KSP/KSP.x86_64' #Kerbal

#Python
        alias p='python3'
        PYTHONPATH=/home/joecool/lib/python:/home/joecool/.local/lib/ #:/opt/sage/local/lib/python/site-packages/
        EDITOR=vim
        export PYTHONPATH EDITOR

# Syntax-Hightlight/Override highlighter colors
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

#Java Font-Rendering
export _JAVA_OPTIONS='-Dawt.useSystemAAFontSettings=on -Dswing.aatext=true -Dswing.defaultlaf=com.sun.java.swing.plaf.gtk.GTKLookAndFeel'
