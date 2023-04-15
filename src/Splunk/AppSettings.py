import datetime
import os
import toml

class AppSettings:
    """
        public class AppSettings
            public AppSettings()
            public bool SplunkEnvironment => !string.IsNullOrWhiteSpace(SplunkHome) &&
            public string SplunkHome { get; set; }
            public string SplunkSessionKey { get; set; }
            public string SplunkUsername { get; set; }
            public string SplunkPassword { get; set; }
            public string SplunkApiUrl = "https://localhost:8089";
            public string EventsApiUrl { get; set; } = "https://api.bitwarden.com";
            public string IdentityUrl { get; set; } = "https://identity.bitwarden.com";
            public DateTime EventsStartDate { get; set; } = DateTime.UtcNow.AddYears(-1);
    """

    def __init__(self):
        self.SplunkHome = os.getenv("SPLUNK_HOME")
        self.SplunkSessionKey = os.getenv("SPLUNK_SESSION_KEY")
        self.SplunkUsername = os.getenv("SPLUNK_USERNAME")
        self.SplunkPassword = os.getenv("SPLUNK_PASSWORD")
        self.SplunkApiUrl = os.getenv(
            "SPLUNK_API_URL", "https://localhost:8089")
        self.EventsApiUrl = os.getenv(
            "EVENTS_API_URL", "https://api.bitwarden.com")
        self.IdentityUrl = os.getenv(
            "IDENTITY_URL", "https://identity.bitwarden.com")
        self.EventsStartDate = datetime.datetime.utcnow(
        ) + datetime.timedelta(days=-365)  # 1 year ago

    @property
    def SplunkEnvironment(self):
        return self.SplunkHome is not None and self.SplunkSessionKey is not None

    @staticmethod
    def load():
        appSettings = AppSettings()
        appSettings.loadFromFile()
        return appSettings

    def loadFromFile(self):
        if self.SplunkEnvironment:
            appSettingsFile = os.path.join(
                self.SplunkHome,
                "etc",
                "apps",
                "bitwarden_events",
                "local",
                "script.conf")
            try:
                with open(appSettingsFile, "r") as file:
                    appSettings = toml.load(file)
            except FileNotFoundError:
                print(f"AppSettings: {appSettingsFile} not found")

            config = appSettings['config']
            if 'splunkApiUrl' in config:
                self.SplunkApiUrl = config['splunkApiUrl']
            if 'splunkUsername' in config:
                self.SplunkUsername = config['splunkUsername']
            if 'splunkPassword' in config:
                self.SplunkPassword = config['splunkPassword']
            if 'startDate' in config:
                self.EventsStartDate = datetime.datetime.strptime(
                    config['startDate'], "%Y-%m-%d")
            if 'apiUrl' in config:
                self.EventsApiUrl = config['apiUrl']
            if 'identityUrl' in config:
                self.IdentityUrl = config['identityUrl']
        else:
            input(f"Splunk Username: {self.SplunkUsername}")
            input(f"Splunk Password: {self.SplunkPassword}")

        return self

    def __str__(self):
        return f"""AppSettings: {{ SplunkHome: {self.SplunkHome}, SplunkSessionKey: {self.SplunkSessionKey}, SplunkUsername: {self.SplunkUsername}, SplunkPassword: {self.SplunkPassword}, SplunkApiUrl: {self.SplunkApiUrl}, EventsApiUrl: {self.EventsApiUrl}, IdentityUrl: {self.IdentityUrl}, EventsStartDate: {self.EventsStartDate} }}"""
