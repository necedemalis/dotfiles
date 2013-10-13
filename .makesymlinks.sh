#!/bin/bash
############################
# .make.sh
# This script creates symlinks from the home directory to any desired dotfiles in ~/dotfiles
############################

dir=~/dotfiles                    # dotfiles directory
files="vimrc vim zshrc wyrdrc tmux.conf tmux-powerlinerc tmux-powerline tmuxinator Xmodmap texmf ncmpcpp hnb"    # list of files/folders to symlink in homedir

for file in $files; do
    #if [ file -f == "vifmrc" ] ; then
            #echo "Creating symlink to $file in home directory."
            #ln -s $dir/$file ~/.vifm/$file
    #else
            echo "Creating symlink to $file in home directory."
            ln -s $dir/$file ~/.$file
    #fi
done

ln -s ~/dotfiles/vifmrc ~/.vifm/vifmrc
ln -s ~/dotfiles/dwb/ ~/.config/
ln -s ~/dotfiles/mpd.conf ~/.mpd
ln -s ~/dotfiles/bin/ ~/
ln -s ~/dotfiles/lib/ ~/
ln -s ~/dotfiles/scripts/ ~/
