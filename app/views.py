from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .news import getNews
from .newsanalysis import newsSenti
from .stockdetails import stockDetails
from .realtimeGraphData import realTimeData
from .indicators import fetchindicators
from mlModels.lstm import lstmpredict

@login_required(login_url="/login/")
def index(request):
    
    news = getNews()
    senti = newsSenti(news)
    details = stockDetails()
    livegraphdata = realTimeData()
    indicator = fetchindicators()
    lstm = lstmpredict(livegraphdata)

    context = {}
    context['segment'] = 'index'
    context['news'] = news
    context['newssenti'] = senti
    context['stockdata'] = details
    context['realtimeGraphData'] = livegraphdata
    context['indicator'] = indicator
    context['lstm'] = lstm

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))