from locust import (
    HttpUser,
    task,
)


class FirstUser(HttpUser):
    @task
    def hello(self):
        self.client.get('/partner')

