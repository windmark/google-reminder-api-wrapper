from .reminder_api_base import ReminderApiBase
from .utils import create_date_object


class ReminderApi(ReminderApiBase):
    def __init__(self):
        super().__init__()

    def get(self, task_id='', clientAssignedId=''):
        # task_id = serverAssignedId to ensure backwards compatbility

        if not task_id and not clientAssignedId:
            raise ValueError("serverAssignedId and clientAssignedId can't both be empty")

        payload = {
            "taskId": [{}]
        }

        if task_id:
            payload['taskId'][0]['serverAssignedId'] = task_id

        if clientAssignedId:
            payload['taskId'][0]['clientAssignedId'] = clientAssignedId    

        
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

    def create(self, title, due_date='', clientAssignedId=''):
        if not title:
            raise ValueError("Title can't be empty when creating reminder")

        payload = {
            "taskList": {
                "systemListId": "TIMELY"
            },
            "task": {
                "title": title
            },
            "taskId": {}
        }

        if clientAssignedId:
            payload['taskId']['clientAssignedId'] = clientAssignedId

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
