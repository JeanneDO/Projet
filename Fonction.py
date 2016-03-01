# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:11:11 2016

@author: Jeanne
"""

import csv
from random import randint, random

###############################################################################
                                #OUVERTURE BASE#
###############################################################################


player_list=[]
count=0
count2=0
list_player=[]

with open('C:/Users/Utilisateur/Desktop/ENSAE_3A/projet_info/players_total.csv', 'r') as csvfile:
    player_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in player_reader:
        count+=1            
        if count==829:
            head_row=row
        else:
            continue

with open('C:/Users/Utilisateur/Desktop/ENSAE_3A/projet_info/players_total.csv', 'r') as csvfile:
    player_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in player_reader:
        count2+=1
        if count2 in range(2,828):
            dic={}
            count3=0
            for value in row:
                count3+=1
                dic[head_row[count3-1].replace('"','')]=row[count3-1].replace('"','')
        else:
            continue
        list_player.append(dic)

###############################################################################
                                #LISTES JOUEURS#
###############################################################################


postes=['Première Ligne','Première Ligne','Première Ligne','Deuxième Ligne','Deuxième Ligne','Troisième Ligne','Troisième Ligne','Troisième Ligne','Demi mélée','Demi ouverture','3/4 centre','3/4 centre','3/4 aile','3/4 aile','Arrière']
postes_pack=['Première Ligne','Première Ligne','Première Ligne','Deuxième Ligne','Deuxième Ligne','Troisième Ligne','Troisième Ligne','Troisième Ligne']
postes_arrières=['Demi mélée','Demi ouverture','3/4 centre','3/4 centre','3/4 aile','3/4 aile','Arrière']

liste_buteurs=[]
for player in list_player:
    if player['dummy buteur']=='1':
        liste_buteurs.append(player)

for player in list_player:
    player['jeu_au_pied']=0
    pied=player['Pourcentage ballons joués pied']
    if pied!='.':
        pied=float(pied)
        if pied>=20:
            player['jeu_au_pied']=1
            
for player in list_player:
    player['dummy jeune']=0
    age=player['âge']
    if age!='.':
        age=float(pied)
        if age<25:
            player['dummy jeune']=1
            
liste_pied=[]
for player in list_player:
    if player['jeu_au_pied']==1:
        liste_pied.append(player)

liste_jeunes=[]
i=0
for player in list_player:
    i+=1
    age=player['âge']
    if age!='.' and age!='':
        age=float(age)
        if age<25:
            liste_jeunes.append(player)
  
french_players=[]
for player in list_player:
    if player not in french_players:
        if player['Lieu_de_naissance']=='France':
            french_players.append(player)
    if player not in french_players:
        if player['nom']=='SCOTT_SPEDDING':
            french_players.append(player)
        if player['nom']=='SEBASTIEN_VAHAAMAHINA':
            french_players.append(player)
        if player['nom']=='DANIEL_KOTZE':
            french_players.append(player)            
        if player['nom']=='RORY_KOCKOTT':
            french_players.append(player)
        if player['nom']=='UINI_ATONIO':
            french_players.append(player)
        if player['nom']=='WESLEY_FOFANA':
            french_players.append(player)
        if player['nom']=='BERNARD_LE_ROUX':
            french_players.append(player)
        if player['nom']=='SERU_NOA_NAKAITACI':
            french_players.append(player)     
        if player['nom']=='FRANCOIS_VAN_DER_MERWE':
            french_players.append(player)


print([player['nom'] for player in french_players])
len(french_players)    

###############################################################################
                                #CRITERES EQUIPES#
###############################################################################

def equipe(count,liste):
    equipe=[]
    buteurs=[]
    pieds=[]
    jeunes=[]
    for poste in postes:
        candidats=[]   
        for joueur in liste:
            if joueur['Type de poste']==poste and joueur not in equipe:
                candidats.append(joueur)     
        i=randint(0,len(candidats)-1)
        player=candidats[i]
        equipe.append(player)
        if player in liste_buteurs:
            buteurs.append(player) 
        if player in liste_pied:
            pieds.append(player) 
        if player in liste_jeunes:
            jeunes.append(player)        
    while buteurs==[]:
        i=randint(0, len(equipe)-1)
#        buteur=liste_buteurs[i]
        for buteur in liste_buteurs:
            if equipe[i]['Type de poste']==buteur['Type de poste']:
                equipe[i]=buteur
                buteurs.append(buteur)
    while pieds==[]:
        i=randint(0, len(equipe)-1)
#        pied=liste_pied[i]
        for pied in liste_pied:
            if player['Type de poste']==pied['Type de poste'] and equipe[i]['dummy buteur']==pied['dummy buteur'] :
                equipe[i]=pied
                pieds.append(pied)
    count=4-len(jeunes)
    if count>0:
        while len(jeunes)<4 :
            i=randint(0, len(equipe)-1)
#            vieux_to_replace=equipe[i]
            for jeune in liste_jeunes:
                if equipe[i]['Type de poste']==jeune['Type de poste'] and equipe[i]['jeu_au_pied']==jeune['jeu_au_pied'] and equipe[i]['dummy buteur']==jeune['dummy buteur'] and equipe[i] not in liste_jeunes and jeune not in equipe:
                    equipe[i]=jeune
                    jeunes.append(jeune)
    return equipe

test=equipe(15,list_player)

print([joueur['nom'] for joueur in test])
print([joueur['âge'] for joueur in test])
print([joueur['dummy buteur'] for joueur in test])
print([joueur['jeu_au_pied'] for joueur in test])
print([joueur['Type de poste'] for joueur in test])
 
###############################################################################
                                #FONCTION TALENT#
###############################################################################

meters=[joueur['Mètres_parcourus'].replace('.','0') for joueur in list_player]
meters=[int(meter) for meter in meters]
max_meters=int(max(meters))

Plaquages=[joueur['Pourcentage Plaquages réussis'].replace('.','0') for joueur in list_player]
Plaquages=[int(Plaquage) for Plaquage in Plaquages]
max_Plaquages=int(max(Plaquages))

T_Plaquages=[joueur['Total_plaquages'].replace('.','0') for joueur in list_player]
T_Plaquages=[int(T_Plaquage) for T_Plaquage in T_Plaquages]
max_T_Plaquages=int(max(T_Plaquages))

Essais=[joueur['Essais'].replace('.','0') for joueur in list_player]
Essais=[int(Essai) for Essai in Essais]
max_Essais=int(max(Essais))

Franchissements=[joueur['Franchissements'].replace('.','0') for joueur in list_player]
Franchissements=[int(Franchissement) for Franchissement in Franchissements]
max_Franchissements=int(max(Franchissements))

matchs=[joueur['Total Match'].replace('.','0') for joueur in list_player]
matchs=[int(match) for match in matchs]
max_matchs=int(max(matchs))

points=[joueur['Total Points'].replace('.','0') for joueur in list_player]
points=[int(point) for point in points]
max_points=int(max(points))

poids=[joueur['Poids'].replace('.','0') for joueur in list_player]
poids=[int(poid) for poid in poids]
max_poids=int(max(poids))

tps_jeu=[joueur['Temps_de_jeu_effectif'].replace('.','0') for joueur in list_player]
tps_jeu=[int(tps_j) for tps_j in tps_jeu]
max_tps_jeu=int(max(tps_jeu))

offload=[joueur['Offload'].replace('.','0') for joueur in list_player]
offload=[int(off) for off in offload]
max_offload=int(max(offload))

Oyonnax=[]
for player in list_player:
    if player['Club_actuel_14']=='Oyonnax':
        Oyonnax.append(player)

Oy=equipe(15,Oyonnax)

def complicite(equipe):
    complicite=0
    for i in range(0,14):
        for j in range(i+1,15):
            if equipe[i]['Club_actuel_14']==equipe[j]['Club_actuel_14'] or equipe[i]['Club_actuel_15']==equipe[j]['Club_actuel_15']:
                complicite+=1
    return complicite
        
complicite(Oy)   
       
def talent(equipe):
    score_points=0
    score_Plaquages=0
    score_T_Plaquages=0
    score_Essais=0
    score_meters=0
    score_matchs=0
    score_poids=0
    score_tps_jeu=0
    score_offloads=0
    score_Franchissements=0
#    list_points=[]
    for joueur in equipe:

        points_j=joueur['Total Points'].replace('.','0')
        points=float(points_j) if '.' in points_j else int(points_j)
        score_points=score_points+points
        
        Plaquages_j=joueur['Pourcentage Plaquages réussis'].replace('.','0')
        Plaquages=float(Plaquages_j) if '.' in Plaquages_j else int(Plaquages_j)
        score_Plaquages=score_Plaquages+Plaquages

        T_Plaquages_j=joueur['Total_plaquages'].replace('.','0')
        T_Plaquages=float(T_Plaquages_j) if '.' in T_Plaquages_j else int(T_Plaquages_j)
        score_T_Plaquages=score_T_Plaquages+T_Plaquages
        
        meters_j=joueur['Mètres_parcourus'].replace('.','0')
        meters=float(meters_j) if '.' in meters_j else int(meters_j)
        score_meters=score_meters+meters        

        matchs_j=joueur['Total Match'].replace('.','0')
        matchs=float(matchs_j) if '.' in matchs_j else int(matchs_j)
        score_matchs=score_matchs+matchs 
        
        tps_jeu_j=joueur['Temps_de_jeu_effectif'].replace('.','0')
        tps_jeu=float(tps_jeu_j) if '.' in tps_jeu_j else int(tps_jeu_j)
        score_tps_jeu=score_tps_jeu+tps_jeu         
 
        Essais_j=joueur['Essais'].replace('.','0')
        Essais=float(Essais_j) if '.' in Essais_j else int(Essais_j)
        score_Essais=score_Essais+Essais         
       
        offloads_j=joueur['Offload'].replace('.','0')
        offloads=float(offloads_j) if '.' in offloads_j else int(offloads_j)
        score_offloads=score_offloads+offloads       

        Franchissements_j=joueur['Franchissements'].replace('.','0')
        Franchissements=float(Franchissements_j) if '.' in Franchissements_j else int(Franchissements_j)
        score_Franchissements=score_Franchissements+Franchissements        
                
        poids_j=joueur['Poids'].replace('.','0')
        poids=float(poids_j) if '.' in poids_j else int(poids_j)
        if joueur['Type de poste'] in postes_pack:
            score_poids=score_poids+poids 
        
    score_total=complicite(equipe)/105+score_T_Plaquages/15/max_T_Plaquages+score_Plaquages/15/max_Plaquages+score_Essais/15/max_Essais+score_Franchissements/15/max_Franchissements+score_offloads/15/max_offload+score_tps_jeu/15/max_tps_jeu+score_points/15/max_points+score_meters/max_meters/15+score_matchs/15/max_matchs+score_poids/8/max_poids
    
    return score_total

talent(equipe(15,list_player))

###############################################################################
                                #GENETIC ALGORITHM#
###############################################################################

def evolution(pop_init, postes, liste, retain, random_select, mutate):
    graded=[ (talent(equipe), equipe) for equipe in pop_init]
    graded = [ equipe[1] for equipe in sorted(graded, key=lambda tup: tup[0], reverse=True)]
    ret=retain
    ret_length=len(graded)*ret
    retain_length = int(ret_length)
    parents = graded[:retain_length]
#    result=parents
    for equipe in graded[retain_length:]:
        if random_select > random():
            parents.append(equipe)
                          
    for equipe in parents:
        if mutate > random():
            player_to_mutate = randint(0, len(equipe)-1)
            poste=equipe[player_to_mutate]['Type de poste']
            jeune=equipe[player_to_mutate]['dummy jeune']
#            buteur=equipe[player_to_mutate]['dummy buteur']
            candidats=[]
            for joueur in liste:
                if joueur['Type de poste']==poste and joueur['dummy jeune']==jeune and joueur not in equipe:
                    candidats.append(joueur)  
            if len(candidats)!=0:
                equipe[player_to_mutate] = candidats[randint(0,len(candidats)-1)]
    
    parents_length = len(parents)
    parents_graded=[ (talent(equipe), equipe) for equipe in parents]
    parents_graded = [ equipe[1] for equipe in sorted(parents_graded, key=lambda tup: tup[0], reverse=True)]
    desired_length = len(pop_init) - parents_length
    children = []
    while len(children) < desired_length:
        parents_length = len(parents)
        male = randint(0, parents_length-1)
        #male = 0
        female = randint(0, parents_length-1)
        #female = 1
        if male != female:
            male = parents[male]
            female = parents[female]
            postes_male=[]
            while len(postes_male) < 9:
                i=randint(0,14)
                if i not in postes_male:
                    postes_male.append(i)            
#            half = 8
#            postes_male=[joueur['Type de poste'] for joueur in male[:half]]
            joueurs_male=[]
            jeunes_child=[]
            for index in postes_male:
                joueurs_male.append((male[index],index))
                if male[index] in liste_jeunes:
                    jeunes_child.append((male[index],index))
            jeunes_c=[joueur_male[0] for joueur_male in jeunes_child]
            j_m=[joueur_male[0] for joueur_male in joueurs_male]
            joueurs_female=[]
            for index in range(0,15):
                j_f=[joueur_female[0] for joueur_female in joueurs_female]
                if index not in postes_male:
                    candidats=[]
                    for joueur in female:
                        if joueur['Type de poste']==female[index]['Type de poste'] and joueur!=female[index] and joueur not in j_f and joueur not in j_m :
                            candidats.append(joueur)
#                    count=0
                    if female[index] not in j_m and female[index] not in j_f:
                        joueurs_female.append((female[index],index))   
                        if female[index] in liste_jeunes:
                            jeunes_c.append(female[index])
                            jeunes_child.append((female[index],index))
                    else:
                        if len(candidats)!=0:
                            i=randint(0,len(candidats)-1)
                            joueurs_female.append((candidats[i],index))
                            if candidats[i] in liste_jeunes:
                                jeunes_c.append(candidats[i])
                                jeunes_child.append((candidats[i],index))
                            
                        else:
                            if male[index] not in j_f:
                                joueurs_female.append((male[index],index))
                                if male[index] in liste_jeunes:
                                    jeunes_c.append(male[index])
                                    jeunes_child.append((male[index],index)) 
                            else: 
                                candidats2=[]
                                for joueur in liste:
                                    if joueur not in j_f and joueur not in j_m and joueur['Type de poste']==female[index]['Type de poste']:
                                        candidats2.append(joueur)
                                candidat2=candidats2[randint(0,len(candidats2)-1)]
                                joueurs_female.append((candidat2,index))
                                if candidat2 in liste_jeunes:
                                    jeunes_c.append(candidat2)
                                    jeunes_child.append((candidat2,index))
                j_f=[joueur_female[0] for joueur_female in joueurs_female]
#                index_f=[joueur_female[1] for joueur_female in joueurs_female]
            for index in postes_male:
                if female[index] in liste_jeunes and len(jeunes_child)<4 and female[index] not in j_m and female[index] not in j_f:
                    for i in range(0,len(joueurs_male)-1) :
                        if joueurs_male[i][0]['Type de poste']==female[index]['Type de poste'] and joueurs_male[i][0] not in liste_jeunes and joueurs_male[i][0] not in j_f and female[index] not in j_m:
                            joueur_to_remove=joueurs_male[i]
                            joueurs_male.remove(joueur_to_remove)
                            joueurs_male.append((female[index],index))
                            jeunes_child.append((female[index],index)) 
                            j_m=[joueur_male[0] for joueur_male in joueurs_male]

            child = joueurs_male + joueurs_female
            child= [ joueur[0] for joueur in sorted(child, key=lambda tup: tup[1])]
            children.append(child)
            parents.append(child)
            parents=[ (talent(equipe), equipe) for equipe in parents]
            parents = [ equipe[1] for equipe in sorted(parents, key=lambda tup: tup[0], reverse=True)]
            parents=parents[:retain_length]
#    parents.extend(children) 
    return parents

###############################################################################
                                    #TEST#
###############################################################################

pop_init=[equipe(15,list_player) for x in range(0,600)]
evol=evolution(pop_init, postes, list_player, 0.1, 0.2, 0.2)
scores=[talent(equipe) for equipe in evol]
best_team=evol[scores.index(max(scores))]
print((max(scores),[joueur['nom'] for joueur in best_team]))
print([joueur['Type de poste'] for joueur in best_team])
print([joueur['âge'] for joueur in best_team])
print([joueur['dummy buteur'] for joueur in best_team])
print([joueur['jeu_au_pied'] for joueur in best_team])
print([joueur['Club_actuel_15'] for joueur in best_team])

scoresB=[talent(equipe) for equipe in pop_init]
maxi=max(scoresB)
index=scoresB.index(maxi)
print(maxi, [joueur['nom'] for joueur in pop_init[index]])
print(maxi, [joueur['âge'] for joueur in pop_init[index]])

###############################################################################
                        #DEUXIEME GENERATION#
###############################################################################

pop2=[]
for i in range(0,200):
    pop_init=[equipe(15,french_players) for x in range(0,600)]
    evol=evolution(pop_init, postes, french_players, 0.1, 0.2, 0.2)
    scores=[talent(equipe) for equipe in evol]
    best_team=evol[scores.index(max(scores))]
    pop2.append(best_team)
    print(i)

evol2=evolution(pop2, postes, french_players, 0.1, 0.2, 0.2)
scores2=[talent(equipe) for equipe in evol2]
best_team2=evol2[scores2.index(max(scores2))]
print((max(scores2),[joueur['nom'] for joueur in best_team2]))
print([joueur['Type de poste'] for joueur in best_team2])
print([joueur['âge'] for joueur in best_team2])
print([joueur['dummy buteur'] for joueur in best_team2])
print([joueur['jeu_au_pied'] for joueur in best_team2])

scoresB=[talent(equipe) for equipe in pop2]
maxi=max(scoresB)
index=scoresB.index(maxi)
print(maxi, [joueur['nom'] for joueur in pop2[index]])
print(maxi, [joueur['âge'] for joueur in pop2[index]])

remember=(5.802426511511985, ['UINI_ATONIO', 'JEFFERSON_POIROT', 'ANTHONY_ETRILLARD', 'ARNAUD_MELA', 'FRANCOIS_VAN_DER_MERWE', 'KEVIN_GOURDON', 'CAMILLE_GERONDEAU', 'CHARLES_OLLIVON', 'MAXIME_MACHENAUD', 'JONATHAN_WISNIEWSKI', 'HENRY_CHAVANCY', 'JONATHAN_DANTY', 'VINCENT_CLERC', 'REMY_GROSSO', 'GAETAN_GERMAIN'])
remember2=(5.834733765746882, ['BRICE_MACH', 'JEFFERSON_POIROT', 'ANTHONY_ETRILLARD', 'ROMAIN_TAOFIFENUA', 'FRANCOIS_VAN_DER_MERWE', 'CHARLES_OLLIVON', 'KEVIN_GOURDON', 'CAMILLE_GERONDEAU', 'MAXIME_MACHENAUD', 'JONATHAN_WISNIEWSKI', 'HENRY_CHAVANCY', 'JONATHAN_DANTY', 'VINCENT_CLERC', 'REMY_GROSSO', 'GAETAN_GERMAIN'])

###############################################################################
                            #DEBUGGAGE#
###############################################################################

retain=0.2
random_select=0.05
mutate=0.5
liste=list_player
        
def equipe(count,liste):
    equipe=[]
    buteurs=[]
    pieds=[]
    jeunes=[]
    for poste in postes:
        candidats=[]   
        for joueur in liste:
            if joueur['Type de poste']==poste and joueur not in equipe:
                candidats.append(joueur)     
        i=randint(0,len(candidats)-1)
        player=candidats[i]
        equipe.append(player)
        if player in liste_buteurs:
            buteurs.append(player) 
        if player in liste_pied:
            pieds.append(player) 
        if player in liste_jeunes:
            jeunes.append(player)        
    if buteurs==[]:
        i=randint(0, len(liste_buteurs)-1)
        buteur=liste_buteurs[i]
        for player in equipe:
            if player['Type de poste']==buteur['Type de poste']:
                equipe.remove(player)
                equipe.append(buteur)
                buteurs.append(buteur)
    if pieds==[]:
        i=randint(0, len(liste_pied)-1)
        pied=liste_pied[i]
        for player in equipe:
            if player['Type de poste']==pied['Type de poste']:
                equipe.remove(player)
                equipe.append(pied)
                pieds.append(pied)
    while len(jeunes)<4:
        i=randint(0, len(liste_jeunes)-1)
        jeune=liste_jeunes[i]
        for player in equipe:
            if player['Type de poste']==jeune['Type de poste'] and player['jeu_au_pied']==jeune['jeu_au_pied'] and player['dummy buteur']==jeune['dummy buteur'] and player not in liste_jeunes:
                equipe.remove(player)
                equipe.append(jeune)
                jeunes.append(jeune)
    return equipe

pop_init=[equipe(15,list_player) for x in range(0,20)]

graded=[ (talent(equipe), equipe) for equipe in pop_init]
graded = [ equipe[1] for equipe in sorted(graded, key=lambda tup: tup[0], reverse=True)]
ret=retain
ret_length=len(graded)*ret
retain_length = int(ret_length)
parents = graded[:retain_length]
#    result=parents
for equipe in graded[retain_length:]:
    if random_select > random():
        parents.append(equipe)
                      
for equipe in parents:
    if mutate > random():
        player_to_mutate = randint(0, len(equipe)-1)
        print(player_to_mutate)
        poste=equipe[player_to_mutate]['Type de poste']
        jeune=equipe[player_to_mutate]['dummy jeune']
        buteur=equipe[player_to_mutate]['dummy buteur']
        candidats=[]
        for joueur in liste:
            if joueur['Type de poste']==poste and joueur['dummy jeune']==jeune and joueur not in equipe:
                candidats.append(joueur)  
        if len(candidats)!=0:
            equipe[player_to_mutate] = candidats[randint(0,len(candidats)-1)]
        print([joueur['Type de poste'] for joueur in equipe])

parents_length = len(parents)
parents_graded=[ (talent(equipe), equipe) for equipe in parents]
parents_graded = [ equipe[1] for equipe in sorted(parents_graded, key=lambda tup: tup[0], reverse=True)]
desired_length = len(pop_init) - parents_length
children = []
while len(children) < desired_length:
    parents_length = len(parents)
    male = randint(0, parents_length-1)
    #male = 0
    female = randint(0, parents_length-1)
    #female = 1
    if male != female:
        male = parents[male]
        female = parents[female]
        postes_male=[]
        while len(postes_male) < 9:
            i=randint(0,14)
            if i not in postes_male:
                postes_male.append(i)            
#            half = 8
#            postes_male=[joueur['Type de poste'] for joueur in male[:half]]
        joueurs_male=[]
        jeunes_child=[]
        for index in postes_male:
            joueurs_male.append((male[index],index))
            if male[index] in liste_jeunes:
                jeunes_child.append((male[index],index))
        jeunes_c=[joueur_male[0] for joueur_male in jeunes_child]
        j_m=[joueur_male[0] for joueur_male in joueurs_male]
        joueurs_female=[]
        for index in range(0,15):
            print(male[index]['Type de poste'],female[index]['Type de poste'])
            j_f=[joueur_female[0] for joueur_female in joueurs_female]
            if index not in postes_male:
                candidats=[]
                for joueur in female:
                    if joueur['Type de poste']==female[index]['Type de poste'] and joueur!=female[index] and joueur not in j_f and joueur not in j_m :
                        candidats.append(joueur)
#                    count=0
                if female[index] not in j_m and female[index] not in j_f:
                    joueurs_female.append((female[index],index))   
                    if female[index] in liste_jeunes:
                        jeunes_c.append(female[index])
                        jeunes_child.append((female[index],index))
                else:
#                        while count < 1:
#                        for candidat in candidats:
#                            if candidat not in joueurs_male and candidat not in joueurs_female:
                    if len(candidats)!=0:
                        i=randint(0,len(candidats)-1)
                        joueurs_female.append((candidats[i],index))
                        if candidats[i] in liste_jeunes:
                            jeunes_c.append(candidats[i])
                            jeunes_child.append((candidats[i],index))
                        
                    else:
                        joueurs_female.append((male[index],index))
                        if male[index] in liste_jeunes:
                            jeunes_c.append(male[index])
                            jeunes_child.append((male[index],index)) 
#                j_f=[joueur_female[0] for joueur_female in joueurs_female]
#                index_f=[joueur_female[1] for joueur_female in joueurs_female]
        print([joueur[0]['Type de poste'] for joueur in joueurs_male])
        print([joueur[0]['Type de poste'] for joueur in joueurs_female])
        for index in postes_male:
            if female[index] in liste_jeunes and len(jeunes_child)<4 and female[index] not in j_m:
                for i in range(0,len(joueurs_male)-1) :
                    if joueurs_male[i][0]['Type de poste']==female[index]['Type de poste'] and joueurs_male[i][0] not in liste_jeunes:
                        joueur_to_remove=joueurs_male[i]
                        joueurs_male.remove(joueur_to_remove)
                        joueurs_male.append((female[index],index))
                        jeunes_child.append((female[index],index))                  
#                                    count=count+1
#                            else:
#                                continue
#                                    
                                                    
#            postes_female=[poste for poste in postes if poste not in postes_male] 
#            for poste in postes_male:   
#                postes_f=postes_female.remove(poste)
#                postes_female=postes_f
#            female2=[joueur for joueur in female if joueur['Type de poste'] in postes_female]
#            for joueur in female:   
#                for poste in postes_female:
#                    if joueur['Type de poste']==poste:     
#                        female2=female2.append(joueur)
        print([joueur[0]['Type de poste'] for joueur in joueurs_male])
        print([joueur[0]['Type de poste'] for joueur in joueurs_female])        
        child = joueurs_male + joueurs_female
        test=  [ joueur[1] for joueur in sorted(child, key=lambda tup: tup[1])]
        child= [ joueur[0] for joueur in sorted(child, key=lambda tup: tup[1])]
        children.append(child)
        parents.append(child)
        parents=[ (talent(equipe), equipe) for equipe in parents]
        parents = [ equipe[1] for equipe in sorted(parents, key=lambda tup: tup[0], reverse=True)]
        parents=parents[:retain_length]
#    parents.extend(children) 

scores=[talent(equipe) for equipe in parents]
best_team=parents[scores.index(max(scores))]
print((max(scores),[joueur['nom'] for joueur in best_team]))

print([joueur['Club_actuel_15'] for joueur in best_team])
print([joueur['dummy buteur'] for joueur in best_team])
print([joueur['jeu_au_pied'] for joueur in best_team])
print([joueur['Type de poste'] for joueur in best_team])
print([joueur['âge'] for joueur in best_team])
