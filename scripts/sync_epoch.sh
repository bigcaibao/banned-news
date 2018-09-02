#!/bin/bash
# author: gfw-breaker

channels="nsc412 nsc413 nsc418 nsc423 nsc422 nsc993"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="http://www.epochtimes.com/gb/$channel.xml"
	wget -q $url
	sed -i 's/content:encoded/content/g' $channel.xml
	sed -i 's#<h2>#<h4>#g' $channel.xml
	sed -i 's#</h2>#</h4>#g' $channel.xml
	echo "getting channel: $channel"
	python parse_epoch.py $channel
done


