from log_manager import LogManager
from secret_keys import SecretKeys
from dropbox_manager import DropboxManager
from schedule import Schedule
import time
import os


class CatPi:

    log_man = LogManager()

    def __init__(self):
        self.dropbox_man = DropboxManager(SecretKeys.dropbox_access_token)
        self.schedule = Schedule()

    @log_man.log_event_decorator('Loading from file', 'INFO')
    def load(self, file_name):
        try:
            data = self.dropbox_man.download_file_to_data(file_name)
            self.schedule.load_events_from_data(data)
            if self.schedule.has_events():
                return 'Events successfully loaded from JSON!'
            else:
                return 'No events were loaded'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    @log_man.log_event_decorator('Evaluating events', 'INFO')
    def evaluate(self):
        try:
            if self.schedule.has_events():
                self.schedule.evaluate_events()
                return 'Events evaluated successfully!'
            else:
                return 'There were no events to evaluate'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    @log_man.log_event_decorator('Writing changes to file', 'INFO')
    def save(self, file_name):
        try:
            if self.schedule.has_events():
                data = self.schedule.serialize_to_json()
                self.dropbox_man.upload_data_to_file(file_name, data)
                return 'Changes were saved successfully!'
        except Exception as e:
            return 'An error occurred: ' + str(e)

    def run(self, file_name):
        self.load(file_name)
        self.evaluate()
        self.save(file_name)