#!/bin/bash

echo "PC wakes up at $1 tomorrow morning."
wakeuptime=`date -d "$1am tomorrow" +%s`
sudo sh -c "echo 0 > /sys/class/rtc/rtc0/wakealarm"
sudo sh -c "echo $wakeuptime > /sys/class/rtc/rtc0/wakealarm"
sudo suspend
