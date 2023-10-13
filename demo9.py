import requests
import json
import matplotlib.pyplot as plt


# 获取天气数据
def get_weather_data():
    url = 'http://t.weather.itboy.net/api/weather/city/101280101'
    response = requests.get(url)
    weather_data = response.text
    return weather_data


# 解析天气数据
def parse_weather_data():
    weather_data = get_weather_data()
    weather_data = json.loads(weather_data)
    forecast_data = weather_data.get('data').get('forecast')
    dates = []
    highs = []
    lows = []
    for data in forecast_data:
        date = data.get('date')
        high = data.get('high')
        low = data.get('low')
        dates.append(date)
        highs.append(int(high[high.index(' ') + 1:-1]))
        lows.append(int(low[low.index(' ') + 1:-1]))
    return dates, highs, lows


# 绘制温度变化图
def draw_temperature_chart():
    dates, highs, lows = parse_weather_data()
    plt.plot(dates, highs, label='High')
    plt.plot(dates, lows, label='Low')
    plt.xlabel('Date')
    plt.ylabel('Temperature (℃)')
    plt.title('Weather Forecast')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    draw_temperature_chart()
