class Temperature:
    def __init__(self) -> None:
        pass


    def convertFahrenheit( celsius):
        #self.celsius = celsius
        fahrenheit = ((celsius/5)*9)+32
        return fahrenheit
    
    def convertCelcius( fahrenheit):
       # self.fahrenheit = fahrenheit
        celcius = ((fahrenheit-32)*5)/9
        return celcius
    print(convertCelcius(220))
