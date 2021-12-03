import  requests 
from  bs4  import  BeautifulSoup
from requests.models import ContentDecodingError

from constants import SINOPTIK_URL

page = requests.get(SINOPTIK_URL)
soup = BeautifulSoup(page.content, 'html.parser')
todays_temperature = soup.find('p' , attrs = {'class': 'today-temp'} )
todays_description  = soup.find('div' , attrs = {'class': 'description'})
print(todays_temperature)
print(todays_description)
if todays_temperature is not None and todays_description is not None :
       print( todays_temperature.get_text())
       print( todays_description.get_text())
    
    