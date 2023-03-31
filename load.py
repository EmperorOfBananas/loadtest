from locust import HttpUser, between, task, SequentialTaskSet
import json

class MicroUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    @task
    def launch(self):
        with self.client.post('/auth/login', data=json.dumps({'username': 'Test9', 'password': 'TestPass01$'}),
                        headers={},
                        name='Test 0',
                        catch_response=True
        ) as response:
            if response.status_code is 200:
                print(response.status_code)
                response.success()
            else:
                response.failure('failed')