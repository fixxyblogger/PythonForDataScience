from locust import HttpUser, TaskSet, task, between


class IrisPredict(TaskSet):
    @task
    def GetRoot(self):
        self.client.get('/')


class IrisLoadTest(HttpUser):
    tasks = [IrisPredict]
    host = 'http://127.0.0.1:8000'
    stop_timeout = 20
    wait_time = between(1, 5)
