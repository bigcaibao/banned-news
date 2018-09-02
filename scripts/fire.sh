#!/bin/bash
# author: gfw-breaker

folder=$(dirname $0)
cd $folder

## pull
mkdir -p ../indexes
mkdir -p ../pages
rm *.xml
git pull

## sync
for sf in $(ls sync_*.sh); do
	bash $sf
done

## add to git
git add ../indexes/*
git add ../pages/*

ts=$(date "+-%m月-%d日-%H时-%M分" | sed 's/-0//g' | sed 's/-//g')
git commit -a -m "同步于: $ts"
git push


