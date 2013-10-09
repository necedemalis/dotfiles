#run systemd as user instance
#/usr/lib/sytemd/systemd --user

#Keyboard Map
setxkbmap lv && xmodmap ~/.Xmodmap/neo_de_custom.xmodmap && xset -r 51
#setxkbmap de -variant nodeadkeys

#Pulseaudio
pactl load-module module-x11-xsmp
pulseaudio --start

#mpd
#[ ! -s ~/.mpd/pid ] && mpd ~/.mpd/mpd.conf
mpd ~/.mpd/mpd.conf &
#mpdscribble
pidof mpdscribble >& /dev/null
if [ $? -ne 0 ]; then
 mpdscribble &
fi

#fluxbox
exec startfluxbox

