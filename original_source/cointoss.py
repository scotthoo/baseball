import random

sampleSize = 1000
costOfLoss = -1.1
prizeOfWin = 1
bankroll = 100
wins = 0
losses = 0
earnings = 0


for i in range(sampleSize):
	flip = random.randint(0,1)
	if (flip):
		bankroll += prizeOfWin
		wins += 1
		earnings += prizeOfWin
	else:
		bankroll += costOfLoss
		losses += 1
		earnings += costOfLoss

roi = earnings / (1.1*sampleSize)
fundROI = earnings/bankroll


print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Earnings: " + str(earnings))
print("ROI: " + str(roi))
print("Fund ROI: " + str(fundROI))
