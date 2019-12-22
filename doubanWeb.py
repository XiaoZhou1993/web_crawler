# !/usr/bin/env python3
# -*- coding : utf-8 -*-

import json
import requests
from bs4 import BeautifulSoup

targetUrl = "https://movie.douban.com/top250"
# targetUrl = "https://fcww17.com/"

def downloadPage(url):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}
    data = requests.get(url, headers=headers).content
    return data

def parseHtml(inputHtml):
    soup = BeautifulSoup(inputHtml)

    movieListOfSoup = soup.find('ol', attrs = {'class': 'grid_view'})

    movieNameList = []

    for movie_li in movieListOfSoup.find_all('li'):
        detail = movie_li.find('div', attrs = {'class': 'hd'})
        movieName = detail.find('span', attrs = {'class': 'title'}).getText()
        movieNameList.append(movieName)

    nextPage = soup.find('span', attrs = {'class': 'next'}).find('a')

    if nextPage:
        return movieNameList, targetUrl + nextPage['href']
    return movieNameList, None

def main():
    nextPageUrl = targetUrl
    while nextPageUrl:
        htmlData = downloadPage(nextPageUrl)
        movieNameList, nextPageUrl = parseHtml(htmlData)
        for movieName in movieNameList:
            print(movieName)


if __name__ == '__main__':
    main()