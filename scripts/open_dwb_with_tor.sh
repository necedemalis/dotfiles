#!/bin/bash

if test -z `pidof dwb` ; then
        usewithtor dwb
else
        dwb
fi