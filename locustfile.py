import random
import time
from locust import HttpUser, task


def unique_str():
    return '{:.10f}.{}'.format(time.time(), random.randint(1000, 9999))


def unique_email():
    return 'e.' + unique_str() + '@gmail.com'


class test_login(HttpUser):

    # @task
    # def create_user(self):
    #     email = unique_email()
    #     password = 'abcdefghi'
    #     self.client.post("/api/users", json={
    #                 "user_name": email, "password": password})
    @task
    def genrate_token(self):
    #     # email = unique_email()
    #     # password = 'abcdefghi'
    #     # self.client.post("/api/users", json={
    #     #             "email": email, "password": password})
    #     # email1 = str(int(unique_str()) - 1) + '@gmail.com'
    #     # password1 = 'abcdefghi'
        self.client.post("/api/token", json={
                    "email": "test7@gmail.com", "password": "string"})