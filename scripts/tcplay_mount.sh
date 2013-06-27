#!/bin/bash

if [ -z $1 ] ; then
        echo "usage: tcplay-mount [command]"

        echo "Valid commands are:"
        echo " -m, --mount"
        echo "        Mounts a TrueCrypt container."
        echo " -u, --umount"
        echo "        Unmounts a TrueCrypt container."
elif [ -n $1 ] ; then
        eingabe=$1
fi

case $eingabe in 
        "-m"|"--mount") cd /media/Daten/Backup/
                sudo losetup /dev/loop0 Backup-Neu
                sudo tcplay -m Backup-Neu -d /dev/loop0

                sudo mount -o  nosuid,uid=1000,gid=100 /dev/mapper/Backup-Neu /media/Truecrypt
                cd - &>/dev/null;;

        "-u"|"--umount") cd /media/Daten/Backup/
                sudo umount /media/Truecrypt
                sudo dmsetup remove Backup-Neu
                sudo losetup -d /dev/loop0
                cd - &>/dev/null;;

        "-h"|"--help") echo "usage: tcplay-mount [command]"

                echo "Valid commands are:"
                echo " -m, --mount"
                echo "        Mounts a TrueCrypt container."
                echo " -u, --umount"
                echo "        Unmounts a TrueCrypt container.";;

        *) echo "Dies ist kein gültiger Befehl.";;
esac
