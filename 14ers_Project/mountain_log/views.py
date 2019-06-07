from django.shortcuts import render
from .models import Mountain

# Create your views here.


def index(request):
    """The home page for the 14ers database"""
    return render(request, 'mountain_log/index.html')


def mountains(request):
    """Shows all mountains"""
    mountains = Mountain.objects.order_by('date_added')
    context = {'mountains': mountains}
    return render(request, 'mountain_log/mountains.html', context)


def mountain(request, topic_id):
    """Shows all the entries for a single topic"""
    topic = Mountain.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'mountain': mountain, 'entries': entries}
    return render(request, 'learning_log/mountain.html', context)
