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
                             class_="CurrentConditions--tempValue--MHmYY")
clima = soup.find_all("div",
                             class_="CurrentConditions--phraseValue--mZC_p")

day = soup.find_all("div",
                    class_="CurrentConditions--tempHiLoValue--3T1DG")

#Transformando em String
temp = (str(current_temp))
temp_clima = str(clima)
tem_day = str(day)

#Exibindo na tela
result = "Current temperature: " + temp[82:84] + "ºC in Brasília" + "\n" +  "Current weather: " + temp_clima[75:-7] + "\n" + "Day: " + tem_day[103: 105] + "ºC     Night: " + tem_day[191:193] + 'ºC'
n.show_toast("Weather update", result, duration=10)
