#run systemd as user instance
exec /usr/lib/sytemd/systemd --user &

#Keyboard Map
setxkbmap lv && xmodmap ~/.Xmodmap/neo_de_custom.xmodmap && xset -r 51
#setxkbmap de -variant nodeadkeys

#Pulseaudio
pulseaudio --start
#mpd
[ ! -s ~/.mpd/pid ] && mpd ~/.mpd/mpd.conf
#mpdscribble
pidof mpdscribble >& /dev/null
if [ $? -ne 0 ]; then
 mpdscribble &
fi

exec startfluxbox

#case $1 in
#dwm)
#        exec dwm 
#        ;;
#fluxbox)
#        exec startfluxbox
#        ;;
#esac
