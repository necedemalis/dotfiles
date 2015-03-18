#!/bin/bash
############################
# This script creates symlinks from the home directory to any desired dotfiles in ~/dotfiles
# Install first!!:
# mpd,mutt,vifm,remind,wyrd,zsh,tmux,tmux-powerline,latex,ncmpcpp
############################

dir=~/dotfiles                    # dotfiles directory
files="ncmpcpp taskrc texmf tmux.conf tmux-powerlinerc tmuxinator vimrc vim vimperatorrc wyrdrc Xmodmap Xresources zshrc"    # list of files/folders to symlink in homedir


for file in $files; do
            echo "Creating symlink to $file in home directory."
            ln -s $dir/$file ~/.$file
done

ln -s ~/dotfiles/bin/ ~/
ln -s ~/dotfiles/dwb/ ~/.config/
ln -s ~/dotfiles/mpd.conf ~/.mpd
ln -s ~/dotfiles/muttrc ~/.mutt/muttrc
ln -s ~/dotfiles/tmux-powerline/mytheme.sh ~/.tmux-powerline/themes/
ln -s ~/dotfiles/tmux-powerline/remind.sh ~/.tmux-powerline/segments/
ln -s ~/dotfiles/vifmrc ~/.vifm/vifmrc
