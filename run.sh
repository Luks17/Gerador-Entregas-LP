#!/bin/bash

dir=./env
venv=./env/bin


if [ ! -d "$dir"  ]; then
	python -m venv env
	# muda o diretorio do ambiente se detectar que o script esta sendo usado em windows
	if [ ! -d "$venv" ]; then
		venv=./env/Scripts
	fi
	$venv/pip install -r requirements.txt
fi

$venv/python index.py

