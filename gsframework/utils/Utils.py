import requests
import datetime
import pytz
import json


class Utils():
    TASK_INIT = 0
    TASK_CHECK_FAIL = 1
    TASK_EXEC_FAIL = 2
    TASK_SUCCESS = 3
    TASK_NOT_EXEC = 4  #由于控制开关没开启,task虽然加入了任务列表,但并没有执行

    @staticmethod
    def send_message_via_http(stage, status, msg, msg_type, detail,
                                push_msg_url, http_timeout):
        message = Utils.get_send_message(stage, status, msg, msg_type, detail)
        headers = {'Content-Type': 'application/json'}
        url = push_msg_url
        print("sense http push msg url : " + url + " , body: " + message)
        try:
            r = requests.post(url,
                            data=message,
                            timeout=http_timeout,
                            headers=headers)
            print("sense http send success and response : " + r.text)
        except:
            print('sense http send failed')

    @staticmethod
    def get_send_message(stage, status, msg, msg_type, detail):
        """
        Generate a JSON-formatted message for sending to a Kafka topic.

        Parameters:
        - stage (str): The stage of the task (e.g., "Ffmpeg", "SfmMapping").
        - status (int): The numerical status code of the task (0 for "FINISHED", 1 for "RUNNING",
                    2 for "WARNING", and any other value for "ERROR").
        - msg (str): A short message describing the task status.
        - msg_type (str): The type of the message (e.g., "INFO", "ERROR", "WARNING").
        - detail (str): Additional details or information about the task.

        Returns:
        - str: A JSON-formatted string containing the task information for Kafka messaging.
        """


        dt = datetime.datetime.utcnow()  # <-- get time in UTC
        utc_dt = pytz.UTC.localize(dt)
        timestamp = utc_dt.isoformat()
        message = {
            "stage": stage, 
            "status": status,
            "msg": msg,
            "timestamp": timestamp,
            "msg_type": msg_type,
            "detail": detail,
        }
        return json.dumps(message)