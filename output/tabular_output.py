
def tabular_output(data, postcode):
	print('\n' + postcode, 'has a total of', length, 'crimes. \n')


	county_names = ['Devon', 'Somerset', 'Narnia']
	temperature = [5, 8, 11]
	wind_speed = [16.0, 5.0, 3.0]
	humidity = [40.0, 50.0, 12.0]
	air_pressure = [1018.1, 1008.7, 995.6]

	telemetry = ['County', 'Temperature', 'Wind Speed', 'Humidity', 'Air Pressure']
	data = [telemetry] + list(zip(county_names, temperature, wind_speed, humidity, air_pressure))

	for i, d in enumerate(data):
		line = '|'.join(str(x).ljust(15) for x in d)
		print(line)
	if i == 0:
		print('-' * len(line))