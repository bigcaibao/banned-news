#!/bin/bash
# author: gfw-breaker

channels="zyyyoeqqvi zivymejqv_ zg_yre_rvq z__yoerrvp zvyyieoqvp z_yyqerqvo"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="https://www.voachinese.com/api/$channel"
	wget -q $url -O $channel.xml
	echo "getting channel: $channel"
	python parse_voa.py $channel
done


