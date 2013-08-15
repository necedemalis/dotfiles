#!/bin/sh

if [ $# -lt 1 ]; then 
    echo "No destination defined. Usage: $0 destination" >&2
    exit 1
elif [ $# -gt 1 ]; then
    echo "Too many arguments. Usage: $0 destination" >&2
    exit 1
fi

START=$(date +%s)
rsync -aAXv --delete /* $1 --exclude={/dev/*,/proc/*,/sys/*,/tmp/*,/run/*,/mnt/*,/media/*,/lost+found,/home/*/.gvfs,/var/lib/pacman/sync/*,/var/log/journal/*,/home/joecool/Downloads,/home/joecool/Dokumente,/home/joecool/builds,/home/joecool/Dropbox,/home/joecool/Musik,/home/joecool/.PlayOnLinux,/home/joecool/PlayOnLinux\'s\ virtual\ drives,/home/joecool/Studium,/home/joecool/.vifm/Trash,/home/joecool/.wine,/swapfile}
FINISH=$(date +%s)
echo "total time: $(( ($FINISH-$START) / 60 )) minutes, $(( ($FINISH-$START) % 60 )) seconds"

touch $1/"Backup from $(date '+%A, %d %B %Y, %T')"
