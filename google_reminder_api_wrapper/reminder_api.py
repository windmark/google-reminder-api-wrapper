from .reminder_api_base import ReminderApiBase
from .utils import create_date_object


class ReminderApi(ReminderApiBase):
    def __init__(self):
        super().__init__()

    def get(self, task_id):
        payload = {
            "taskId": [{
                "serverAssignedId": str(task_id)
            }]
        }
        return self.request('get', payload)

    def list(self):
        # TODO: Change in payload to change what filter, ex to show already done

        # {
        #     "5": 0, // Reminder status (0: Incomplete only / 1: including completion)
        #     "6": 10 // limit, but not called that
        #     "2": Data to be acquired about the tasks
        #     "16": Range specification (end date and time)
        #     "24": Range specification (end date and time)
        #     "25": Range specification (start date and time)
        # }

        return self.request('list', '')

    def create(self, title, due_date=''):
        if not title:
            raise ValueError("Title can't be empty when creating reminder")

        payload = {
            "taskList": {
                "systemListId": "TIMELY"
            },
            "task": {
                "title": title
            }
        }

        if due_date:
            payload['task']['dueDate'] = create_date_object(due_date)

        res = self.request('create', payload)
        return res['taskId']['serverAssignedId']

    def delete(self, task_id):
        payload = {
            "taskId": [{
                "serverAssignedId": str(task_id)
            }]
        }
        self.request('delete', payload)
