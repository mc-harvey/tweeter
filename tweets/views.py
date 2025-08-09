# tweets/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TweetForm
from .models import Tweet

def tweet_list(request):
    tweets = Tweet.objects.select_related('user').order_by('-created_at')
    return render(request, 'list.html', {'tweets': tweets})  # or 'tweets/list.html' if using app templates

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user      # auto-attach current user
            tweet.save()
            return redirect('tweet_list')  # make sure your URL name matches
    else:
        form = TweetForm()
    return render(request, 'form.html', {'form': form})
