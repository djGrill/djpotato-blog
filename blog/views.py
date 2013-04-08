from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.models import Post


def index(request):
    posts = Post.all().order('-created_at')
    return render_to_response('index.html', {'posts': posts})


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post(title=title, body=body)
        post.put()

        post_id = post.key().id()
        title_for_url = post.title_for_url()
        year = post.created_at.year
        month = post.created_at.month

        return HttpResponseRedirect('/' + str(year) + '/' + str(month) + '/' + str(title_for_url) + '/' + str(post_id))
    else:
        return render_to_response('create.html',
                                  {},
                                  context_instance=RequestContext(request))


def details(request, post_id):
    post = Post.get_by_id(int(post_id))
    return render_to_response('details.html', {'post': post})


def edit(request, post_id):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post.get_by_id(int(post_id))
        post.title = title
        post.body = body
        post.is_edited = True
        post.put()

        title_for_url = post.title_for_url()
        year = post.created_at.year
        month = post.created_at.month

        return HttpResponseRedirect('/' + str(year) + '/' + str(month) + '/' + str(title_for_url) + '/' + str(post_id))
    else:
        post = Post.get_by_id(int(post_id))

        return render_to_response('edit.html',
                                  {'post': post, 'post_id': post_id},
                                  context_instance=RequestContext(request))


def archive_year(request, year):
    posts = Post.all().order('-created_at')
    posts_filtered = []

    for post in posts:
        if post.created_at.year == int(year):
            posts_filtered.append(post)

    return render_to_response('index.html', {'posts': posts_filtered})


def archive_month(request, year, month):
    posts = Post.all().order('-created_at')
    posts_filtered = []

    for post in posts:
        if post.created_at.year == int(year) and post.created_at.month == int(month):
            posts_filtered.append(post)

    return render_to_response('index.html', {'posts': posts_filtered})
