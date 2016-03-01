# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:14:09 2016

@author: Utilisateur
"""

import time
import sys
import os
os.chdir('C:/Users/Utilisateur/Documents/GitHub/ProjetInfo2')
import Fonction
import numpy as np
 
pop_init=[Fonction.equipe(15,Fonction.list_player) for x in range(0,600)]
evol=Fonction.evolution(pop_init, Fonction.postes, Fonction.list_player, 0.1, 0.2, 0.2)
scores=[Fonction.talent(equipe) for equipe in evol]
best_team=evol[scores.index(max(scores))]  
print((max(scores),[joueur['nom'] for joueur in best_team]))

