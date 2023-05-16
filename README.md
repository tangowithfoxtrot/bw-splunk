## Setup
```bash
pip install -r requirements.txt
```

### Run
```bash
src/Splunk/Program.py cli
```

## Models & classes
### Application
- `AppSettings.py`: load vars from `.env` for local development; loading from `script.conf` in SplunkEnvironment is untested

### Bitwarden
- `EventRequestModel.py`: `/public/events` object
- `EventResponseModel.py`: `/public/events` object
- `EventLogModel.py`: EventResponseModel.py + GroupName, MemberName, MemberEmail, ActingUserName & ActingUserEmail; not implemented
- `ListResponseModel.py`: not implemented
- `MemberResponseModel.py`: `/public/member` object; not implemented
- `GroupResponseModel.py`: `/public/groups` object; not implemented
- `BitwardenApi.py`: Implements the above classes to interact with Bitwarden

### Splunk
- `EventsApiKeyModel.py`: retrieve Bitwarden API key at `/servicesNS/nobody/bitwarden_event_logs/storage/passwords/bitwarden_event_logs_realm:api_key/`; key is in the form of `<org_client_id>_<org_client_secret>`
- `EventsApiCollectionModel.py`: set/update `last_log_date` at `servicesNS/nobody/bitwarden_event_logs/storage/collections/data/eventsapi`
- `SplunkApi.py`: Implements the above classes to interact with Splunk

## TODO
1. Finish implementing Bitwarden models.
2. Finish `BitwardenApi.py` and `Program.py`.
3. Package application to test running from an actual Splunk environment.

## References
- [Bitwarden Splunk Integration (C#)](https://github.com/bitwarden/splunk)
- [Bitwarden API](https://bitwarden.com/help/article/api/)
- [Splunk API Documentation](https://docs.splunk.com/Documentation/Splunk/9.0.4/RESTREF/RESTprolog)
- [Splunk SDK for Python](https://dev.splunk.com/enterprise/docs/devtools/python/sdk-python/)
