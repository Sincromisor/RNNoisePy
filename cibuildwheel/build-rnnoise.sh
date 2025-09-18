#!/bin/bash

set -x
set -e

# dnfが存在するか確認し、ある場合はlibtoolとwgetをインストール
if command -v dnf > /dev/null 2>&1; then
    echo "dnf found, using dnf to install dependencies."
    dnf -y install libtool wget
elif command -v apk > /dev/null 2>&1; then
    echo "apk found, using apk to install dependencies."
    apk add --no-cache libtool wget py3-pip
else
    echo "No supported package manager found (dnf or apk)."
    exit 1
fi

cd "$(dirname "$0")/../rnnoise"
./autogen.sh
CFLAGS='-march=x86-64-v3' ./configure
make clean
make
cp -a .libs/librnnoise.so* ../src/rnnoisepy/lib/
find ../src/rnnoisepy

echo "RNNoise build complete."
