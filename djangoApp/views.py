from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.template import Context, loader
from django.http import HttpResponse
from django.db.models import Count
@login_required
def dashboard(request):
    backlogs = ProductBacklog.objects.all()
    teams = Team.objects.all()
    return render(None,'dashboard.html', {'backlogs': backlogs, 'teams': teams})
@login_required
def backlog(request, backlog_id):
    backlog = get_object_or_404(ProductBacklog, pk=backlog_id)
    stories = UserStory.objects.filter(product_backlog=backlog)
    return render(None,'backlog.html', {'backlog': backlog, 'stories': stories})
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def liste(request):
    teams = Team.objects.all()
    backlogs = ProductBacklog.objects.all()
    return render(None,'liste.html', {'backlogs': backlogs, 'teams': teams})
def statistique(request):
    lm={}
    lp={}
    a=Team.objects.only("name")
    t=Team.objects.all()
    for s in t:
        p=Project.objects.filter(team=s)
        lp[s] =p.count
    for s in a:
        teams = Team.objects.get(name=s)
        countMb= teams.members.all().count()
        lm[s] = countMb
    return render(None,'statistique.html', { 'lm': lm ,'t':t,'lp':lp})