from locust import HttpUser, task, between, constant
import csv
import random

# Function to load user emails from the CSV file
def load_email_of_test_taker(file_path):
    user_emails = []
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            user_emails.append(row[1])
    return user_emails


credentials_list = load_email_of_test_taker('test-taker-id-pass.csv')

class WalnutEduTestUser(HttpUser):
    wait_time = constant(0.5)
    host = "https://uat.walnutedu.in"

    # @task
    # def code_flow(self):
    #     self.login()
    #     self.get_test_taker_profile()
    #     self.check_login_status()
    #     self.check_logout()

    def on_start(self):
        # Select a user ID when the task starts
        self.user_id = random.choice(credentials_list)
        self.login()

    @task
    def login(self):
        # Payload for login
        payload = {
            "usr": self.user_id,
            "pwd": "Walnut@12345"
        }

        # Perform the login request and handle response
        with self.client.post(
            "/api/method/walmiki_lms.walmiki_lms.doctype.test_taker.test_taker.test_taker_login",
            data=payload,
            catch_response=True
        ) as response:
            if response.status_code == 200 and "Set-Cookie" in response.headers:

                response.success()
                print("Login successful:", response.text)
            else:
                response.failure(f"Login failed: {response.status_code}")
                print("Error response:", response.text)

    # @task
    # def check_login_status(self):
    #
    #         with self.client.get(
    #             "/api/method/walmiki_lms.walmiki_lms.doctype.test_taker.test_taker.check_test_taker_logged_in",
    #             catch_response=True
    #         ) as response:
    #             if response.status_code == 200:
    #                 response.success()
    #                 print("Check login status successful:", response.text)
    #             else:
    #                 response.failure(f"Failed to check login status: {response.status_code}")
    #                 print("Error response:", response.text)

    # @task
    # def get_test_taker_profile(self):
    #         with self.client.get(
    #             "/api/method/walmiki_lms.walmiki_lms.doctype.test_taker.test_taker.get_test_taker_profile",
    #             catch_response=True
    #         ) as response:
    #             if response.status_code == 200:
    #                 response.success()
    #                 print("Test taker profile fetched successfully:", response.text)
    #             else:
    #                 response.failure(f"Failed to fetch test taker profile: {response.status_code}")
    #                 print("Error response:", response.text)


    # @task
    # def get_all_quizzes(self):
    #
    #         with self.client.get(
    #             "/api/method/walmiki_lms.walmiki_lms.doctype.walmiki_quiz.walmiki_quiz.get_all_quizzes",
    #             catch_response=True
    #         ) as response:
    #             if response.status_code == 200:
    #                 response.success()
    #                 print("Fetched quizzes successfully:", response.text)
    #             else:
    #                 response.failure(f"Failed to fetch quizzes: {response.status_code}")
    #                 print("Error response:", response.text)

    @task
    def check_logout(self):

            with self.client.get(
                "/api/method/logout",
                catch_response=True
            ) as response:
                if response.status_code == 200:
                    response.success()
                    print("Logout successful:", response.text)
                else:
                    response.failure(f"Failed to logout: {response.status_code}")
                    print("Error response:", response.text)

    # @task
    # def get_all_filters(self):
    #         with self.client.get(
    #             "/api/method/walmiki_lms.walmiki_lms.doctype.walmiki_quiz.walmiki_quiz.get_all_filters",
    #             catch_response=True
    #         ) as response:
    #             if response.status_code == 200:
    #                 response.success()
    #                 print("Fetched filters successfully:", response.text)
    #             else:
    #                 response.failure(f"Failed to get filters: {response.status_code}")
    #                 print("Error response:", response.text)

