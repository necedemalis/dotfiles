#run systemd as user instance
#/usr/lib/sytemd/systemd --user

#Keyboard Map
setxkbmap lv && xmodmap ~/.Xmodmap/neo_de_custom.xmodmap && xset -r 51
#setxkbmap de -variant nodeadkeys

#Urxvt Daemon
urxvtd -q -f -o

#Pulseaudio & Timidity
pactl load-module module-x11-xsmp
jack_control start
pulseaudio --start
#timidity -iA -Os &
timidity -iA -B2,8 -Os -EFreverb=0 &

#mpd
#[ ! -s ~/.mpd/pid ] && mpd ~/.mpd/mpd.conf
mpd ~/.mpd/mpd.conf
#mpdscribble
pidof mpdscribble >& /dev/null
if [ $? -ne 0 ]; then
 mpdscribble &
fi

#Feh
sh ~/.fehbg &

#fluxbox
exec startfluxbox
