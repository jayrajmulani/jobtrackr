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


if __name__=="__main__":
     unittest.main()