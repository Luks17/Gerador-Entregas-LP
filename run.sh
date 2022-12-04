#!/bin/bash

pwd=$(pwd)
dir=$pwd/env
venv=$pwd/env/bin
output=$pwd/output


if [ ! -d "$dir"  ]; then
	python -m venv env
	# muda o diretorio do ambiente se detectar que o script esta sendo usado em windows
	if [ ! -d "$venv" ]; then
		venv=./env/Scripts
	fi
	$venv/pip install -r requirements.txt
fi

if [ -d "$output" ]; then
	rm -rf $output
fi

$venv/python index.py

