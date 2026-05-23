#!/usr/bin/env bash

echo "正在解压 relations.pkl.gz..."

python unzip_relations.py

echo "启动应用..."

gunicorn app:app
