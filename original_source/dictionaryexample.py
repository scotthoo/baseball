wars = {'deGrom': 8.8, 'Scherzer': 7.2, 'Verlander': 6.8, 'Corbin': 6.3, 'Cole': 6.3}

print(wars)

wars.pop('Scherzer')

print(wars)

wars['Snell'] = 4.6

print(wars)

wars['Verlander'] *= 10

print(wars)

print(wars['Verlander'])

for item in wars.items():
	print(item)


	