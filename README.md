# YouTube Music API
A quick API for interacting with likes on YouTube Music. Meant for personal use only.

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

## YouTube Authentication
### Obtaining the Headers
To [authenticate YTMusic](https://ytmusicapi.readthedocs.io/en/latest/setup.html) you first need to obtain some headers from YouTube Music.

1. Sign in to https://music.youtube.com/
2. Open Developer Tools and select the Network tab.
3. Navigate to Library in your YouTube Music account.
4. Find an authenticated POST request. Filtering for `browse?key=` is a good option.
5. Copy the relevant request headers to the JSON template shown in the next section.

### Headers JSON
The `YTMUSIC_COOKIE_JSON` environment variable must contain JSON in the following format:

```
{
  "Accept": "*/*",
  "Accept-Language": "en-US,en;q=0.5",
  "Content-Type": "application/json",
  "Cookie": "your value here",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0",
  "X-Goog-AuthUser": "your value here",
  "X-Goog-Visitor-Id": "your value here",
  "origin": "https://music.youtube.com"
}
```

`Cookie` and `X-Goog-AuthUser` most commonly change between authentication sessions.
