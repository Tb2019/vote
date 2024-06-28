from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Vote
def index(request):
    if request.method == 'POST':
        selected_day = request.POST.get('day')
        vote = Vote.objects.get(day=selected_day)
        vote.votes += 1
        vote.save()
        return redirect('results')

    days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    return render(request, 'polls/index.html', {'days': days})

def results(request):
    votes = Vote.objects.all()
    return render(request, 'polls/results.html', {'votes': votes})
