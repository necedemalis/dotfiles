#!/bin/bash

per=`cat Info.txt | grep Personnel | sed -e 's:^Personnel\:\ ::g' | sed -e 's:\.\ [^a-zA-Z]*$::g'`
id3tag --comment="$per" *.mp3
