from django.shortcuts import render
import requests


# Create your views here.
def home(request):
	response = requests.get('https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=0c0407608aca4f85a238762f6056c5a1')
	gedata = response.json()
	#return gedata 
	return render(request, 'newsapi/home.html',{
			'gedata': gedata,
			#'title': gedata.articles[0].title
			#'description':gedata.articles[0].description,
		 })

