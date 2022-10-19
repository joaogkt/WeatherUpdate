import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

#objeto da classe ToastNotifier
n = ToastNotifier()

#Função para obter dados da url fornecida
def getdata(url):
    r = requests.get(url)
    return r.text

#Passando a url para a função getdata e convertendo os dados do codigo para html
htmldata = getdata(
    "https://weather.com/en-IN/weather/today/l/b45444ee720cf31c2252c39970e94267942d8cd3fdb995b6166b35dfc521b4c3")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

#Filtrando os dados necessarios
current_temp = soup.find_all("span",
                             class_="CurrentConditions--tempValue--3a50n")
chances_rain = soup.find_all("div",
                             class_="CurrentConditions--phraseValue--2Z18W")
#Transformando em String
temp = (str(current_temp))
temp_rain = str(chances_rain)

#Exibindo na tela
result = "Current temperature: " + temp[82:84] + "ºC in Brasília" + "\n" +  "Current weather: " + temp_rain[75:-7]
n.show_toast("Weather update", result, duration=8)
