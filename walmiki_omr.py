from locust import HttpUser, task, constant

class WalnutBackendAPITest(HttpUser):
    wait_time = constant(2)
    host =  "https://uat.walnutedu.in/api/resource/Quiz%20Attempt"
    headers = {
        'Content-type':'application/json',
        'Authorization': "token ad40422ad5ef9e7:543e26795de5ab2"
    }

    @task
    def get_quiz_attempt(self):
        with self.client.get("/237lt7bdc2",
            headers= self.headers,
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                print(response.json())
                print("fetched data from quiz id successfully")
                return
            else:
                print("something went wrong", response.status_code)
                return

    @task
    def post_data_to_quiz(self):
        with self.client.put("/237lt7bdc2",
                             headers=self.headers,
                             catch_response=True,
                             ) as response:
            if response.status_code == 200:
                print(response.json())
                print("Putted data successfully")
                return
            else:
                print("something went wrong", response.status_code)
                return