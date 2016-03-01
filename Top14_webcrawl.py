# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:24:46 2016

@author: Jeanne
"""


###############################################################################
                                #IMPORTATION#
###############################################################################

import bs4
from lxml import html
import requests
import string
import _pickle as pickle
from bs4 import BeautifulSoup
import csv

###############################################################################
                            #LINKS AND PLAYER IDs#
###############################################################################

url_root=[]
url_root.append('http://www.lnr.fr/rugby-top-14/joueurs-rugby-top-14')       
for i in range(1,28):
    url_root.append('http://www.lnr.fr/rugby-top-14/joueurs-rugby-top-14?page='+str(i))

player_list=[]

for url in url_root:
    page = requests.get(url) 
    html=page.content
    parsed_html = BeautifulSoup(html)
    section=parsed_html.body.find('section', attrs={'class':'block block-lnr-custom block-lnr-custom-players-list'})
    ul_section=section.find('ul')
    for a in ul_section.findAll('a'):
        player_list.append([a['data-item-id'],a['href']])

season_list=[['2014-2015','14535'],['2015-2016','18505']]
     
###############################################################################
                                #INFO#
###############################################################################
 
i=0
url_root='http://www.lnr.fr'
result={}

for season in season_list:
    player_dic={}
    for player in player_list: 
        i+=1
        dic={}
        player_id=player[0]
        player_page=player[1]
        url_player=url_root+player_page
        url_stats=url_root+'/ajax_player_stats_detail?player='+player_id+'&compet_type=1&=undefined&season='+season[1]+'&_filter_current_tab_id=panel-filter-season&ajax-target-selector=%23player_stats_detail_block#season='+season[1]
        page = requests.get(url_player)
        stat_page=requests.get(url_stats)
        html=page.content
        stat_html=stat_page.content
        parsed_html = BeautifulSoup(html)
        stat_parsed_html = BeautifulSoup(stat_html)
        body=parsed_html.body
        stat_body=stat_parsed_html.body
    #    try:
        dic['nom']=body.find('h1',attrs={'id':'page-title'}).text
        dic[body.find('span',attrs={'class':'title'}).text]=body.find('span',attrs={'class':'text'}).text
        info1=body.find('ul',attrs={'class':'infos-list small-bold'})
        try:
            for item in info1.findAll('li'):
                dic[item.find('span',attrs={'class':'title'}).text]=item.find('span',attrs={'class':'text'}).text 
            info2=stat_body.find('ul',attrs={'class':'fluid-block-grid-3 team-stats'})
            if info2 is not None :
                for item in info2.findAll('li'):   
                    dic[item.find('span',attrs={'class':'title'}).text]=item.find('span',attrs={'class':'text'}).text
#            info3=body.find('ul',attrs={'class':'number-list small-block-grid-2'})
#            if info3 is not None :
#                for item in info3.findAll('li'):   
#                    dic[item.find('span',attrs={'class':'title'}).text]=item.find('span',attrs={'class':'text'}).text
        except:
            continue
        player_dic[dic['nom']]=dic
      #  print(i)
    print('one season down')
    result[season[0]]=player_dic
    
###############################################################################
                                #LIST OF VARIABLES#
###############################################################################

data_list=[]
for season in season_list:
    for player in result[season[0]]:
        for label in result[season[0]][player]:
            if label not in data_list:
                data_list.append(label)

###############################################################################
                #MISSING VARIABLES ADDED TO PLAYERS#
###############################################################################

test=result
for season in season_list:
    for player in test[season[0]]:
        for label in data_list:
            if label not in test[season[0]][player]:
                test[season[0]][player][label]=bytes('NULL', 'utf-8')


###############################################################################
                                #EXPORT 14-15#
###############################################################################

season14_15=[]
for player in test['2014-2015']:
    dic={}
    for label in test['2014-2015'][player]:
        dic[label.replace(" ","_")]=test['2014-2015'][player][label].replace(" ","_")
    season14_15.append(dic)

keys = season14_15[0].keys()

with open('C:/Users/Utilisateur/Desktop/ENSAE_3A/projet_info/14_15top14.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(season14_15)

###############################################################################
                                #EXPORT 15-16#
###############################################################################

season15_16=[]
for player in test['2015-2016']:
    dic={}
    for label in test['2015-2016'][player]:
        dic[label.replace(" ","_")]=test['2015-2016'][player][label].replace(" ","_")
    season15_16.append(dic)

keys = season15_16[0].keys()

with open('C:/Users/Utilisateur/Desktop/ENSAE_3A/projet_info/15_16top14.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, clean_keys)
    dict_writer.writeheader()
    dict_writer.writerows(season15_16)

