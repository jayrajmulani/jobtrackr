from unittest.main import main
from flask import app
# from flask.typing import StatusCode
import unittest
import sys, os, inspect
import json

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from backend.app import app

class FlaskTest(unittest.TestCase):

    def testLogin(self):
        tester = app.test_client(self)
        response = tester.post("/login", json={"email": "rrangar@ncsu.edu", "password": "12345678"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        # print(statuscode)

    def testWrongLogin(self):
        tester = app.test_client(self)
        response = tester.post("/login", json={"email": "xyz@ncsu.edu", "password": "jytfyjtyj"})
        statuscode = response.status_code
        # User account not found
        self.assertEqual(statuscode, 400)
        # print(statuscode)

    def testRegister(self):
        tester = app.test_client(self)
        req = {}
        req["firstName"] = "Rahul"
        req["lastName"] = "RK"
        req["email"] = "rrangar@ncsu.edu"
        req["password"] = "12345678"
        req["confirmPassword"] = "12345678"
        urlToSend = "/register"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        if statuscode == 200:
            # New user created
            self.assertEqual(statuscode, 200)
        if statuscode == 400:
            # User already present
            self.assertEqual(statuscode, 400)

    def testdeletewrongApplication(self):
        tester = app.test_client(self)
        response = tester.post("/delete_application", json={"email": "xahah@ncsu.edu", "_id": "63800dfd2bf155063a7afbd9"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)


    def testViewApplication(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/view_applications?email={email}"
        response = tester.get(urlToSend)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def testViewQuestions(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/view_questions?email={email}"
        response = tester.get(urlToSend)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testdeletewrongQuestions(self):
        tester = app.test_client(self)
        response = tester.post("/delete_question", json={"email": "xahah@ncsu.edu", "_id": "63800dfd2bf155063a7afbd9"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)


    def testAddApplication(self):
        tester = app.test_client(self)
        req = {}
        req["companyName"] = "Edusetu"
        req["jobTitle"] = "Test"
        req["email"] = "dhrumilshah1234@gmail.com"
        req["jobId"] = "12345678"
        req["url"] = "www.google.com"
        req["status"] = "applied"
        urlToSend = "/add_application"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def testAddQuestion(self):
        tester = app.test_client(self)
        req = {}
        req["email"] = "dhrumilshah1234@gmail.com"
        req["question"] = "Why do you want to apply to this Job?"
        req["answer"] = "Because i want money and you are Hiring"
        urlToSend = "/add_question"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testModifyApplication(self):
        tester = app.test_client(self)
        req = {
            "companyName": "a",
            "jobTitle": "a",
            "jobId": "a",
            "description": "a",
            "url": "b",
            "date": "2022-12-28T03:33:43.737Z",
            "status": "inReview",
            "_id": "638eb81bff4164e60179bab2",
            "email": "a@a.com"
        }
        urlToSend = "/modify_application"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testModifyQuestion(self):
        tester = app.test_client(self)
        req = {
         "question": "Q1",
         "answer": "A1",
        "_id": "638bafe50012ef455196cc6e",
        "email": "dhrumilshah1234@gmail.com"
        }
        urlToSend = "/modify_question"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testWrongModifyQuestion(self):
        tester = app.test_client(self)
        req = {
         "question": "Q1",
         "answer": "A1",
        "_id": "IDONTEXIST",
        "email": "dhrumilshah1234@gmail.com"
        }
        urlToSend = "/modify_question"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        # Since the ID doesnt exist.
        self.assertEqual(statuscode, 400)

    def testWrongModifyApplication(self):
        tester = app.test_client(self)
        req = {
            "companyName": "k",
            "jobTitle": "jl",
            "jobId": "nln",
            "description": "lkn",
            "url": "lknl",
            "date": "2022-12-02T21:26:03.739Z",
            "status": "interview",
            "_id": "IDONTEXIST",
            "email": "dhrumilshah1234@gmail.com"
        }
        urlToSend = "/modify_application"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def testviewFiles(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/view_files?email={email}"
        response = tester.get(urlToSend)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testEmptyFiles(self):
        tester = app.test_client(self)
        email = "a@a.com"
        urlToSend = f"/view_files?email={email}"
        response = tester.get(urlToSend)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__=="__main__":
     unittest.main()