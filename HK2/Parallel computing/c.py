import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()
r = requests.get('https://nhaphoc.dlu.edu.vn/tra-cuu', verify=False)
xl = BeautifulSoup(r.text, 'html.parser')
data = xl.find_all('mat-row', {'class': 'mat-row cdk-row ng-star-inserted'})
print(data)
