import unittest
import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()


class TestAPI(unittest.TestCase):
    base_url = os.getenv('DOMAIN')
    mock_doctor = json.load(open('./storage/mock_doctor.json'))
    mock_doctor_id = None
    mock_doctor_response = json.load(
        open('./storage/mock_doctor_response.json'))

    def add_doctor(self):
        endpoint = "/doctor"
        res = requests.post(self.base_url + endpoint, json=self.mock_doctor)
        res_json = res.json()

        self.mock_doctor_id = res_json['id']
        del res_json['id']

        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res_json, self.mock_doctor_response)

        print("add_doctor test completed")

    def get_all_doctors(self):
        endpoint = "/doctor"
        res = requests.get(self.base_url + endpoint)

        self.assertEqual(res.status_code, 200)

        print("get_all_doctors test completed")

    def get_doctor(self):
        endpoint = "/doctor/" + str(self.mock_doctor_id)
        res = requests.get(self.base_url + endpoint)

        res_json = res.json()
        del res_json['id']

        self.assertEqual(res.status_code, 200)
        self.assertDictEqual(res_json, self.mock_doctor_response)

        print("get_doctor test completed")


if __name__ == "__main__":
    tester = TestAPI()

    tester.add_doctor()
    tester.get_doctor()
    tester.get_all_doctors()
