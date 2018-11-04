import requests
import bs4
import array
from heapq import heappush, heappop, heapify

def splice(a):
	res = ""
	for i in range(0,len(a)):
		if a[i] != '$' and a[i] != ',':
			res = res + a[i]
	return res
def main():
	res = requests.get('https://questionnaire-148920.appspot.com/swe/data.html')
	alpha = bs4.BeautifulSoup(res.text, 'lxml')
	SalaryString= alpha.find_all("td", class_="player-salary")
	HighestSalaries = [0] * 125
	for i in range(0,len(SalaryString)):
		if len(SalaryString[i]) != 0:  
			if SalaryString[i].text[0] == '$':
				temp = int(splice(SalaryString[i].text))
				if temp > HighestSalaries[0]:
					heappop(HighestSalaries)
					heappush(HighestSalaries,temp)
	result = 0
	for i in range (0,125):
		result = result + HighestSalaries[i]
	result = result / 125
	print("The qualifying offer value is: $", result)
	return 0
if __name__ == '__main__':
	main()
