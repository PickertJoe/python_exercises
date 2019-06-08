from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.


def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Shows all topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Shows all the entries for a single topic"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Allows the user to enter new information into the website"""
    if request.method != 'POST':
        # Occurs when no data is submitted, creates a blank form
        # Tests whether the request is 'GET' or 'POST'
        form = TopicForm()

    else:
        # Processes submitted data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """Allows the user to make a new entry for an existing topic"""

    # Grabs the appropriate topic using the provided topic id
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Creating a blank form when do data is submitted
        form = EntryForm()

    else:
        # POST data submitted, moving on to processing
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Allows the user to edit a previous entry for an existing topic"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # Response to the initial request, fills the form with the entry in question
        form = EntryForm(instance=entry)

    else:
        # Post data submitted, moving on to processing
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
