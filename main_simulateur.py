#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script Python Example
import time
import sys
import simulator
import numpy as np

user_team1 = sys.argv[1]
user_team2 = sys.argv[2]

# Name of the databse containing the players' profiles
data_file = 'player_better_dataframe.pkl'

#Specify any number of players per team

if user_team1 == 'England':
	team1 = ['John Mallett']

if user_team1 == 'France':
	team1 = ['Morgan Sienawski']

if user_team1 == 'Scotland':
	team1 = ['Phil De Glanville']

if user_team1 == 'Wales':
	team1 = ['Gideon Koegelenberg']
	
if user_team1 == 'Rd':
	team1 = [['John Mallett','Morgan Sienawski','Phil De Glanville','John Mallett'][np.random.randint(0,3,1)]]
	
if user_team2 == 'England':
	team2 = ['John Mallett']

if user_team2 == 'France':
	team2 = ['Morgan Sienawski']

if user_team2 == 'Scotland':
	team2 = ['Phil De Glanville']

if user_team2 == 'Wales':
	team2 = ['Gideon Koegelenberg']
	
if user_team2 == 'Rd':
	team2 = [['John Mallett','Morgan Sienawski','Phil De Glanville','John Mallett'][np.random.randint(0,3,1)]]

# Any of these work
simulator.simul_get_caracs(data_file,team1,team2)
#~ simulator.simul_get_caracs(data_file,team1)
#~ simulator.simul_get_caracs(data_file,team2)
#~ simulator.simul_get_caracs(data_file)