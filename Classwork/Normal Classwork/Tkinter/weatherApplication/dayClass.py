class Day:
    def __init__(self, dayDate: str, temp: str, humidity: str, wind: str, rain: str) -> None:
        self.dayDate = dayDate
        try:
            self.temp: int = int(temp)
            self.humidity: int = int(humidity)
            self.wind: int = int(wind)
            self.rain: int = int(rain)
        except:
            raise Exception('One or more values (Temp, Humidity, Wind, Rain) is not a number.')
        
        # Humidity = Percent
        if self.humidity > 100 or self.humidity < 1:
            raise Exception('Humidity Cannot Be Below 1 or Above 100')