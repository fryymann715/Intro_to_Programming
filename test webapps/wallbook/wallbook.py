import cgi
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import webapp2

# We're going to use string substitution to render our HTML
HTML_TEMPLATE = """<!DOCTYPE html>
<head>
  <meta charset="utf-8">
  <title>Wall Book Example</title>
</head>
<body>
  <form action="/sign?%s" method="post">
    <div><textarea name="content" rows="3" cols="60"></textarea></div>
    <div><input type="submit" value="Post Comment"></div>
  </form>
  <hr>
  <form>Wall:
    <input value="%s" name="wall_name">
    <input type="submit" value="Switch">
  </form>
  <br>
  Logged in as: <strong>%s</strong><br>
  <a href="%s">%s</a>
  <!-- user comments start here -->
  %s
</body>
</html>
"""

DEFAULT_WALL = 'Public'

# We set a parent key on the 'Post' to ensure that they are all
# in the same entity group. Queries across the single entity group
# will be consistent.  However, the write rate should be limited to
# ~1/second.

def wall_key(wall_name=DEFAULT_WALL):
  """Constructs a Datastore key for a Wall entity.

  We use wall_name as the key.
  """
  return ndb.Key('Wall', wall_name)

# These are the objects that will represent our Author and our Post. We're using
# Object Oriented Programming to create objects in order to put them in Google's
# Database. These objects inherit Googles ndb.Model class.
class Author(ndb.Model):
  """Sub model for representing an author."""
  identity = ndb.StringProperty(indexed=True)
  name = ndb.StringProperty(indexed=False)
  email = ndb.StringProperty(indexed=False)

class Post(ndb.Model):
  """A main model for representing an individual post entry."""
  author = ndb.StructuredProperty(Author)
  content = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)


class MainPage(webapp2.RequestHandler):
  def get(self):
    wall_name = self.request.get('wall_name',DEFAULT_WALL)
    if wall_name == DEFAULT_WALL.lower(): wall_name = DEFAULT_WALL

    # Ancestor Queries, as shown here, are strongly consistent
    # with the High Replication Datastore. Queries that span
    # entity groups are eventually consistent. If we omitted the
    # ancestor from this query there would be a slight chance that
    # Greeting that had just been written would not show up in a
    # query.

    # [START query]
    posts_query = Post.query(ancestor = wall_key(wall_name)).order(-Post.date)

    # The function fetch() returns all posts that satisfy our query. The function returns a list of
    # post objects
    posts =  posts_query.fetch()
    # [END query]

    # If a person is logged into Google's Services
    user = users.get_current_user()
    if user:
        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'
        user_name = user.nickname()
    else:
        url = users.create_login_url(self.request.uri)
        url_linktext = 'Login'
        user_name = 'Anonymous Poster'

    # Create our posts html
    posts_html = ''
    for post in posts:

      # Check if the current signed in user matches with the author's identity from this particular
      # post. Newline character '\n' tells the computer to print a newline when the browser is
      # is rendering our HTML
      if user and user.user_id() == post.author.identity:
        posts_html += '<div><h3>(You) ' + post.author.name + '</h3>\n'
      else:
        posts_html += '<div><h3>' + post.author.name + '</h3>\n'

      posts_html += 'wrote: <blockquote>' + cgi.escape(post.content) + '</blockquote>\n'
      posts_html += '</div>\n'

    sign_query_params = urllib.urlencode({'wall_name': wall_name})

    # Render our page
    rendered_HTML = HTML_TEMPLATE % (sign_query_params, cgi.escape(wall_name), user_name,
                                    url, url_linktext, posts_html)

    # Write Out Page here
    self.response.out.write(rendered_HTML)

class PostWall(webapp2.RequestHandler):
  def post(self):
    # We set the same parent key on the 'Post' to ensure each
    # Post is in the same entity group. Queries across the
    # single entity group will be consistent. However, the write
    # rate to a single entity group should be limited to
    # ~1/second.
    wall_name = self.request.get('wall_name',DEFAULT_WALL)
    post = Post(parent=wall_key(wall_name))

    # When the person is making the post, check to see whether the person
    # is logged into Google
    if users.get_current_user():
      post.author = Author(
            identity=users.get_current_user().user_id(),
            name=users.get_current_user().nickname(),
            email=users.get_current_user().email())
    else:
      post.author = Author(
            name='anonymous@anonymous.com',
            email='anonymous@anonymous.com')


    # Get the content from our request parameters, in this case, the message
    # is in the parameter 'content'
    post.content = self.request.get('content')

    # Write to the Google Database
    post.put()

    # Do other things here such as a page redirect
    self.redirect('/?wall_name=' + wall_name)

app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/sign', PostWall),
], debug=True)