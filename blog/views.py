from django.template import RequestContext, Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Post


def index(request):
    t = loader.get_template('index.html')
    c = Context({
        'number': 7,
    })

    return HttpResponse(t.render(c))


def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']

        post = Post(title=title,
                    body=body)
        print post.put()

        return HttpResponseRedirect('/')
    else:
        return render_to_response('create.html',
                                  {},
                                  context_instance=RequestContext(request))
