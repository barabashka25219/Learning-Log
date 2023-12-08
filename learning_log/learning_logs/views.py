from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from users.models import Userinfo

def get_profile(view_func):
    def _get_profile(request, **kwargs):
        if request.user.is_authenticated:
            profile = Userinfo.objects.get(user=request.user.id)
        else:
            profile = {}

        return view_func(request, profile=profile, **kwargs)
    
    return _get_profile
         

@get_profile
def index(request, profile):
    context = {
        'user_info': profile,
    }

    return render(request, 'learning_logs/index.html', context)


@login_required
@get_profile
def topics(request, profile):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {
        'topics': topics,
        'user_info': profile,
    }
    return render(request, 'learning_logs/topics.html', context)


@login_required
@get_profile
def topic(request, profile, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.user != topic.owner:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic, 
        'entries': entries,
        'user_info': profile,
    }
    return render(request, 'learning_logs/topic.html', context)


@login_required
@get_profile
def new_topic(request, profile):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
        
    context = {
        'form': form,
        'user_info': profile,
    }
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
@get_profile
def new_entry(request, profile, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if request.user != topic.owner:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {
        'topic': topic, 
        'form': form,
        'user_info': profile,
    }
        
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
@get_profile
def edit_entry(request, profile, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id

    if request.user != topic.owner:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            form.save()
            return redirect("learning_logs:topic", topic_id=topic_id)
        
    context = {
        'form': form, 
        'entry_id': entry_id,
        'user_info': profile
    }
        
    return render(request, 'learning_logs/edit_entry.html', context=context)


@login_required
def remove_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    topic_id = topic.id

    if request.user == topic.owner:
        entry.delete()
    else:
        raise Http404
    
    return redirect("learning_logs:topic", topic_id=topic_id)


@login_required
def remove_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.user == topic.owner:
        topic.delete()
    else:
        raise Http404
    
    return redirect("learning_logs:topics")