arr = []
weather_report = {}
with open('nyc-weather.csv', 'r') as handle:
    for line in handle:
        items = line.split(',')
        day = items[0]
        try:
            temperature = int(items[1])
            arr.append(temperature)
            weather_report[day] = temperature
        except:
            print('Invalid temperature. Ignore this row')

print(arr)

avg_first_week = sum(arr[:7]) / 7
print(avg_first_week)

print(max(arr[:10]))

print(weather_report)
print(weather_report['Jan 9'])
print(weather_report['Jan 4'])
