Made for Google's API `YouTube Data API v3`

### Environment Variables
`YOUTUBE_API_KEY`: your api key for `YouTube Data API v3`, get from https://console.developers.google.com/
`YOUTUBE_CHANNEL_ID`: channel id of channel you want to retrieve videos from. google how to get id of channels by @

### Quota
should probably not run into a quota limit, since the api allows 10,000 queries per day,
and a SEARCH uses 100 queries. Running a check once an hour will only use 2,400 queries,
which could be further optimized if you want. Can probably do a simpler request and do more heavy lifting
on the python side, but should be fine for most usages, even if you want to combine searches with
other actions.