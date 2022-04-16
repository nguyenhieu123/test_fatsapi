from locust import HttpUser, task


class test_login(HttpUser):

    # @task
    # def create_user(self):
    #     email = unique_email()
    #     password = 'abcdefghi'
    #     self.client.post("/api/users", json={
    #                 "user_name": email, "password": password})
    @task
    def genrate_token(self):
        self.client.post("/api/token", json={
                    "email": "test7@gmail.com", "password": "string"})