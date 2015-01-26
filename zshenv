export PATH=${PATH}:"$HOME/bin"
export PATH=${PATH}:"$HOME/.local/bin"
export DIFFPROG=$DIFFPROG:/usr/bin/meld
export BROWSER=$BROWSER/usr/bin/firefox

#Xdg user directories:
[[ -z $XDG_CONFIG_HOME ]] && export XDG_CONFIG_HOME="$HOME/.config" && export XDG_DATA_HOME="$HOME/.local/share" && export XDG_CACHE_HOME="$HOME/.cache" && XDG_DOWNLOAD_DIR="$HOME/Downloads" && XDG_DOCUMENTS_DIR="$HOME/Dokumente"

#Privoxy for Surf:
http_proxy=http://127.0.0.1:8118/
HTTP_PROXY=$http_proxy
export http_proxy HTTP_PROXY

