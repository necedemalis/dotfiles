# Print the current date.

TMUX_POWERLINE_SEG_REMIND_FORMAT_DEFAULT=""

generate_segmentrc() {
	read -d '' rccontents  << EORC
# date(1) format for the date. If you don't, for some reason, like ISO 8601 format you might want to have "%D" or "%m/%d/%Y".
export TMUX_POWERLINE_SEG_REMIND_FORMAT="${TMUX_POWERLINE_SEG_REMIND_FORMAT_DEFAULT}"
EORC
	echo "$rccontents"
}

__process_settings() {
	if [ -z "$TMUX_POWERLINE_SEG_REMIND_FORMAT" ]; then
		export TMUX_POWERLINE_SEG_REMIND_FORMAT="${TMUX_POWERLINE_SEG_REMIND_FORMAT_DEFAULT}"
	fi
}

run_segment() {
        __process_settings
        test_var=`remind -t14g ~/Dokumente/Remind/.reminders | awk '/No\ reminders/ {print "True"}'`
        if [ $test_var == "True" ]; then
                echo ""
        else
                ereig=`remind -t14g ~/Dokumente/Remind/.reminders | awk 'NR == 3 {print}'`
                ereig_dat=`remind -n ~/Dokumente/Remind/.reminders | grep "$ereig" | sed 's/\//\ /g' | awk '{print $3 "." $2 ":"}'`
                echo "$ereig_dat" "$ereig"
                #echo $(remind -n ~/Dropbox/Markus/Remind/.reminders | grep "$(echo -n $rem_var | cut -c 49-54)" | cut -c 6-10 && echo $(echo -n $rem_var | cut -c 49-70))
        fi
        return 0
}
