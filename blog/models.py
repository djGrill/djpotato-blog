from google.appengine.ext import ndb


class Post(ndb.Model):
    title = ndb.StringProperty(required=True)
    body = ndb.StringProperty(required=True)
    created_at = ndb.DateProperty(auto_now_add=True)
    updated_at = ndb.DateProperty(auto_now_add=True)
    active = ndb.BooleanProperty(required=True)

    def __unicode__(self):
        return self.title
