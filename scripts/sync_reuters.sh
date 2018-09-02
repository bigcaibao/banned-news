#!/bin/bash
# author: gfw-breaker

channels="chinaNews CNAnalysesNews CNIntlBizNews CNTopGenNews vbc_homepagetopnews vbc_CN_columnist_all"

## create dirs
for channel in $channels ; do
	mkdir -p ../pages/$channel
done
	
## get feeds files
for channel in $channels ; do
	url="http://cn.reuters.com/rssFeed/$channel"
	wget -q $url -O $channel.xml
	echo "getting channel: $channel"
	python parse_reuters.py $channel
done


