#!/usr/bin/python
# coding: utf-8

import sys
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

channel = sys.argv[1]
xml_file = channel + '.xml'

tree = ET.parse(xml_file)
root = tree.getroot()
index_page = ''


def get_content(url):
	response = requests.get(url)
	text = response.text.encode('utf-8')
	parser = BeautifulSoup(text, 'html.parser')
	clear_pholders(parser)
	body = get_body(parser)
	if body != None:
		pub_time = get_time(parser)
		body = pub_time + '<br/>\n' + body
		return body
	else:
		return None
	

def clear_pholders(parser):
	# remove scripts
	pholders = parser.find_all('script')
	for pholder in pholders:
		pholder.clear()
	# remove media
	pholders = parser.find_all('div', attrs = {'class': 'media-pholder'})
	for pholder in pholders:
		pholder.decompose()
	

def get_time(parser):
	time_div = parser.find_all('div', attrs = {'class': 'published'})[0]
	return time_div.prettify().encode('utf-8')


def get_body(parser):
	article = parser.find('div', id = 'article-content')
	if article != None:
		return article.contents[1].prettify().encode('utf-8')
	return None


def get_name(link):
	fname = link.split('/')[-1]
	return fname.split('.')[0]


def write_page(name, title, link, content):
	body = '### ' + title
	body += "\n------------------------\n\n" + content
	body += "\n原文链接：" + link + "\n"
	body += "\n\n------------------------\n" + "#### [禁闻聚合首页](https://github.com/gfw-breaker/banned-news/blob/master/README.md) &nbsp;|&nbsp;  [一键翻墙软件](https://github.com/gfw-breaker/nogfw/blob/master/README.md)"
	f_name = '../pages/' + channel + '/' +  name + '.md'
	fh = open(f_name, 'w')
	fh.write(body)
	fh.close()


for child in root[0]:
	if child.tag != 'item':
		continue
	link = child.find('link').text
	title = child.find('title').text.encode('utf-8')
	name = get_name(link)
	content = get_content(link)
	if content != None:
		write_page(name, title, link, content)
		index_page += '#### [' + title + '](' + '../pages/' + channel + '/' + name + '.md) \n\n'


index_file = open('../indexes/' + channel + '.md', 'w')
index_file.write(index_page)
index_file.close()


