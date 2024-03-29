from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from datetime import datetime
from blog.models import Post


def index(request):
    posts = Post.query(Post.active == True).order(-Post.created_at).fetch()
    archive = build_archive()
    return render_to_response('index.html', {'posts': posts, 'archive': archive})


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post(title=title, body=body)
        post.put()

        post_id = post.id()
        title_for_url = post.title_for_url()
        year = post.created_at.year
        month = post.created_at.month
        redirect_uri = '/' + str(year) + '/' + str(month) + '/' + str(title_for_url) + '/' + str(post_id)

        return HttpResponseRedirect(redirect_uri)
    else:
        return render_to_response('create.html',
                                  {},
                                  context_instance=RequestContext(request))


def details(request, post_id):
    post = Post.get_by_id(int(post_id))
    archive = build_archive()

    if post.active:
        return render_to_response('details.html', {'post': post, 'archive': archive})
    else:
        return HttpResponseRedirect('/')


def edit(request, post_id):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post.get_by_id(int(post_id))
        post.title = title
        post.body = body
        post.updated_at = datetime.now()
        post.is_edited = True
        post.put()

        title_for_url = post.title_for_url()
        year = post.created_at.year
        month = post.created_at.month
        redirect_uri = '/' + str(year) + '/' + str(month) + '/' + str(title_for_url) + '/' + str(post_id)

        return HttpResponseRedirect(redirect_uri)
    else:
        post = Post.get_by_id(int(post_id))

        if post.active:
            return render_to_response('edit.html',
                                      {'post': post, 'post_id': post_id},
                                      context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')


def delete(request, post_id):
    if request.method == 'POST':
        post = Post.get_by_id(int(post_id))
        post.active = False
        post.put()

        return HttpResponseRedirect('/')
    else:
        post = Post.get_by_id(int(post_id))

        if post.active:
            return render_to_response('delete.html',
                                      {'post': post, 'post_id': post_id},
                                      context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect('/')


def archive_year(request, year):
    posts = Post.query(Post.active == True).order(-Post.created_at).fetch()
    posts_filtered = []

    for post in posts:
        if post.created_at.year == int(year):
            posts_filtered.append(post)

    archive = build_archive()
    return render_to_response('index.html', {'posts': posts_filtered, 'archive': archive})


def archive_month(request, year, month):
    posts = Post.query(Post.active == True).order(-Post.created_at).fetch()
    posts_filtered = []

    for post in posts:
        if post.created_at.year == int(year) and post.created_at.month == int(month):
            posts_filtered.append(post)

    archive = build_archive()
    return render_to_response('index.html', {'posts': posts_filtered, 'archive': archive})


def build_archive():
    posts = Post.query(Post.active == True).order(-Post.created_at).fetch()
    archive = {}

    for post in posts:
        year = post.created_at.year
        month = post.created_at.strftime('%m-%B')

        if year not in archive:
            archive[year] = []

        if month not in archive[year]:
            archive[year].append(month)

    return archive
