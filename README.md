# API wrapper for Google Reminder

This is a work in progress to create an API wrapper for handling Google Reminders via code. Due to missing official
documentation of the API, this should be considered unstable and not deployed to any production systems.

The current commands are implemented
* list
* create
* delete

Not implemented commands
* update


## API
The following internal API at Google is what Google Calendar is using to interact with the Reminders,
`https://reminders-pa.clients6.google.com/v1internalOP/reminders/`. For some reason, Inbox seems to
use another API, but the way of Google Calendar is used here.

### Authorization
Currently, the Google session is still based on fixed cookies and authorization keys in the HTTP header.
```$xslt
SID = 'xxxxxxxxxxxxxxxxx'
HSID = 'xxxxxxxxxxxxxxxxx'
SSID = 'xxxxxxxxxxxxxxxxx'
APISID = 'xxxxxxxxxxxxxxxxx'
SAPISID = 'xxxxxxxxxxxxxxxxx'
authorization = 'xxxxxxxxxxxxxxxxx'
key = 'xxxxxxxxxxxxxxxxx'
```

:warning: Note: The credential keys need to be set as environment variables for the requests to work. This is
a work in progress and will in the future be integrated with the Google sessions API.


#### Finding Credentials
Credentials can be found by doing the following
1. Go to Google Calendar, https://calendar.google.com and make sure the "Reminder" calendar is marked.
2. Open the "Network" tab of the Chrome Developer Tool and search for `reminders / list`
3. In the "Header" sub-tab, find the required headers in the "Request Header"


### Request Structure
The following is the main structure of the request sent to the Reminders API
`https://reminders-pa.clients6.google.com/v1internalOP/reminders/<COMMAND>`.

where <COMMAND> is one of the following
* list
* update
* create
* delete

Header
```
{
    'x-origin': 'https://calendar.google.com',
    'content-type': 'application/json',
    'authorization': <SESSION AUTHORIZATION>,
    'key': <SESSION KEY>,
    'cookie': <SESSION COOKIES>
}
```

The Google Calendar is using this API with `application/json+protobuf` in the data payload, but due to readability problems
this wrapper has reverse-engineered parts of the schema to normal JSON field names.



## Backstory
Due to popular demand as seen in the following Google Issue Tracker thread, https://issuetracker.google.com/issues/36760283,
I decided to give it a try.

The  is based on the following comment, https://issuetracker.google.com/issues/36760283#comment193,
```$xslt
There is an undocumented API, which is used for example by Google Calendar. Maybe someone with the skills and time can write a user friendly wrapper or service for it ;-)
https://reminders-pa.clients6.google.com/v1internalOP/reminders/list?key=XXX

Commands are: list, get, create, update, delete

Some more details for "list" in Japanese: https://qiita.com/futa/items/c7a04c7b0be35508a626
```