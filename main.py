from flask import Flask, request
from threading import Thread
from flask_restful import reqparse, abort, Api, Resource
from ytmusicapi import YTMusic
import os, json

app = Flask('')
api = Api(app)

parser = reqparse.RequestParser()

# Look only in the POST body form data
parser.add_argument('name', type=str, location='form')

# Look only in the querystring
parser.add_argument('task', type=str, help='Please provide a valid task id')

# From the request headers
parser.add_argument('X-API-KEY', type=str, location='headers', required=True)

# Look in multiple locations
parser.add_argument('text', location=['headers', 'values', 'json'])


def authenticated(api_key):
  if api_key == os.getenv("THIS_API_KEY_1"):
    return True

class Index(Resource):
  def get(self):
    if next(x for x in ytmusic.get_library_playlists() if x["playlistId"] == 'LM' )['playlistId'] == 'LM':
      return {"alive": "yes"}
    else:
      return {"alive": "no"}

class Likes(Resource):
  def get(self):
    args = parser.parse_args()
    if not authenticated(api_key=args['X-API-KEY']):
      abort(401)
    return ytmusic.get_playlist(playlistId="LM")
  def post(self):
    args = parser.parse_args()
    if not authenticated(api_key=args['X-API-KEY']):
      abort(401)
    
    json_message = json.loads(request.data)

    try:
      track = json_message['track']
    except:
      abort(400)
    
    try:
      artist = json_message['artist']
    except:
      abort(400)

    if type(track) == str and type(artist) == str:
      search_results = ytmusic.search(track + " - " + artist)
      try:
        like = ytmusic.rate_song(videoId=search_results[0]['videoId'], rating='LIKE')
      except:
        abort(500)
      
      if like['actions'][0]['addToToastAction']['item']['notificationActionRenderer']['responseText']['runs'][0]['text'] == 'Added to your likes':
        return {"status": "added to likes"}
    
    else:
      abort(400)


class Poster(Resource):
  def post(self):
    args = parser.parse_args()
    if not authenticated(api_key=args['X-API-KEY']):
      abort(401)
    return args
  

#creating api endpoint
api.add_resource(Index, '/')
api.add_resource(Likes, '/likes')
api.add_resource(Poster, '/poster')

def run():
  app.run(host='0.0.0.0',port=7210)

t = Thread(target=run)
# other code
ytmusic = YTMusic(os.getenv("YTMUSIC_COOKIE_JSON"))
t.start()