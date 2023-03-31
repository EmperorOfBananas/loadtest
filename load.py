from locust import HttpUser, between, task, SequentialTaskSet
import json
from app.forms import LoginForm

class MicroUser(HttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:5000"

    @task
    def login(self):
        form = LoginForm()
        form.username.data = 'Test'
        form.username.data = 'TestPass01$'
        response = self.client.post('/auth/login', data=form.data, follow_redirects=True)
        assert response.status_code == 200
        '''
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
                '''