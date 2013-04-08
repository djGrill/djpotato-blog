from google.appengine.ext import ndb
from django.template.defaultfilters import slugify


class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    body = ndb.TextProperty(required=True)
    created_at = ndb.DateTimeProperty(auto_now_add=True)
    updated_at = ndb.DateTimeProperty(auto_now_add=True)
    is_edited = ndb.BooleanProperty(default=False)
    active = ndb.BooleanProperty(default=True)

    def __unicode__(self):
        return self.title

    def id(self):
        return self.key.id()

    def title_for_url(self):
        return slugify(self.title)

    def created_at_formatted(self):
        return self.created_at.strftime('%B %d, %Y')
