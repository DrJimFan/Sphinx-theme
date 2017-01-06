#!/bin/bash
# swap $1 $2 folders

swapdir() {
    mv $1 _tmpswap
    mv $2 $1
    mv _tmpswap $2
}

if [[ ! -d $1 ]]; then
    echo ABORT: $1 does not exist. Copy $1 folder first.
    exit 1
elif [[ ! -d $2 ]]; then
    echo ABORT: $2 does not exist. Copy $2 folder first.
    exit 1
fi
swapdir $1 $2
