from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TweetModel, TweetComment
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    user = request.user.is_authenticated

    if user:
        return redirect('/tweet')
    else:
        return redirect('/sign-in')

def tweet(request):

    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html',{'tweet':all_tweet})
        else:
            return redirect('/sign-in')

    elif request.method == 'POST':
        user = request.user
        my_tweet = TweetModel()
        my_tweet.author = user
        my_tweet.content = request.POST.get('my-content','')
        my_tweet.save()    
        return redirect('/tweet')

@login_required
def delete_tweet(request, id):
    my_tweet = TweetModel.objects.get(id = id)
    my_tweet.delete()
    return redirect('/tweet')


def tweet_detail(request, id):
    if request.method == 'GET':
        tweet_message = TweetModel.objects.get(id = id)
        all_comment = TweetComment.objects.all().order_by('-created_at')
        return render(request, 'tweet/tweet_detail.html',{'tweet':tweet_message, 'comment':all_comment})
    
    elif request.method == 'POST':
        
        current_tweet = TweetModel.objects.get(id=id)
        comment = request.POST.get('comment','')

        my_comment = TweetComment()
        my_comment.author = request.user
        my_comment.comment = comment
        my_comment.tweet = current_tweet
        my_comment.save()
        return redirect('/tweet/tweet_detail/'+str(id))


@login_required
def delete_comment(request, id):
    my_comment = TweetComment.objects.get(id = id)
    comment_id = my_comment.tweet_id
    my_comment.delete()
    return redirect('/tweet/tweet_detail/'+str(comment_id))




    
    
    


        