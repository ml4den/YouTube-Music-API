# YouTube Music API
A quick API for interacting with likes on YouTube Music

## Endpoint /likes
### GET
Returns a JSON object of liked songs.

Required header: `X-API-KEY`
### POST
Accepts a JSON object of a song to search for and like.

```
{
  "track": "Like a Rolling Stone",
  "artist": "Bob Dylan"
}
```

Required header: `X-API-KEY`
