#run systemd as user instance
exec /usr/lib/sytemd/systemd --user &

#Keyboard Map
setxkbmap de neo -option
#setxkbmap de -variant nodeadkeys

#Pulseaudio
pulseaudio --start

exec startfluxbox

#case $1 in
#dwm)
#        exec dwm 
#        ;;
#fluxbox)
#        exec startfluxbox
#        ;;
#esac
