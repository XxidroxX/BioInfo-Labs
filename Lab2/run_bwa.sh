#!/bin/bash
echo "#### My Program ####"
if [ "$#" -ne 4 ]; then
    echo "Illegal number of parameters"
fi
eval "bwa mem $1 $2 $3 > $4"
echo "Ended"