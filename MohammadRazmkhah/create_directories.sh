#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 directory_path"
    exit 1
fi

directory_path=$1

if [ ! -d "$directory_path" ]; then
    mkdir -p "$directory_path"
fi

for (( i=1; i<=100; i++)); do
    name=$(echo $(( $i * $i )) | sed 'y/0123456789/۰۱۲۳۴۵۶۷۸۹/')
    mkdir -p "$directory_path/$name"
done
