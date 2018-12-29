from struct import *
from decimal import Decimal 
import csv

class Player:
	def __init__(self, name, team, wins, losses, starts, ip, k9, bb9, hr9, war):
		self.name = name
		self.team = team
		self.wins = wins
		self.losses = losses
		self.starts = starts
		self.ip = ip
		self.k9 = k9
		self.bb9 = bb9
		self.hr9 = hr9
		self.war = war


players = []

warMap = {}

with open('leaderboard.csv') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0
	for row in csv_reader:
		#print row
		if line_count == 0:
			line_count += 1
		else:
			name = row[0]
			team = row[1]
			wins = row[2]
			losses = row[3]
			starts = row[6]
			ip = row[7]
			k9 = row[8]
			bb9 = row[9]
			hr9 = row[10]
			war = row[18]

			player = Player(name, team, wins, losses, starts, ip, k9, bb9, hr9, war)
			players.append(player)

			line_count += 1



for p in players:
	warMap[p.name] = p.war

#print(warMap)



pitcher = raw_input('Please enter a pitcher\'s name: ')

#print(pitcher)

if pitcher in warMap:
	print(pitcher + "\'s WAR was: " + str(warMap[pitcher]))
else:
	print("Error: Pitcher not in database!")

