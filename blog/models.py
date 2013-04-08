from google.appengine.ext import db
from django.template.defaultfilters import slugify


class Post(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now_add=True)
    is_edited = db.BooleanProperty(default=False)
    active = db.BooleanProperty(default=True)

    def __unicode__(self):
        return self.title

    def id(self):
        return self.key().id()

    def title_for_url(self):
        return slugify(self.title)

    def created_at_formatted(self):
        return self.created_at.strftime('%B %d, %Y')
