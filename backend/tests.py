from unittest.main import main
import bcrypt
from bson import ObjectId
from flask import app
import unittest
import sys, os, inspect
import json

from pymongo import MongoClient

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from backend.app import app
db1 = os.getenv('MONGO_DB_CONNECTION')
db2 = "?retryWrites=true&w=majority"
db = db1 + db2
client = MongoClient(db, tlsAllowInvalidCertificates=True)
db = client.get_database(os.getenv('DATABASE_TYPE'))
UserRecords = db.register
Applications = db.Applications
UserProfiles = db.Profiles
Questions = db.QA
Files = db.file

class FlaskTest(unittest.TestCase):
    
    def setUp(self):
        # Insert test data here
        hashed = bcrypt.hashpw(
                "12345678".encode("utf-8"), bcrypt.gensalt())
        user_input = {"name": "dhrumil", "email": "dhrumilshah1234@gmail.com", "password": hashed}
        UserRecords.insert_one(user_input)
        application = {
                "_id": ObjectId("638eb81bff4164e60179bab2"),
                "email": "dhrumilshah1234@gmail.com",
                "companyName": "Lexis Nexis",
                "jobTitle": "Software Engineer",
                "jobId": "12345",
                "description": "Not much",
                "url": "https://www.google.com",
                "date": None,
                "status": "Accepted",
                "image": None
            }
        Questions.insert_one({"email": "dhrumilshah1234@gmail.com", "_id": ObjectId("638bafe50012ef455196cc6e"),
                               "question": "aa", "answer": "bb"})
        Applications.insert_one(application)
        UserRecords.delete_one({"email": "rrangar@ncsu.edu"})
    
    def tearDown(self):
        # Clear the mock data after each test
        UserRecords.delete_one({"name": "dhrumil", "email": "dhrumilshah1234@gmail.com"})
        Applications.delete_one({"_id": ObjectId("638eb81bff4164e60179bab2"),
                "email": "dhrumilshah1234@gmail.com"})
        Applications.delete_many({"email": "dhrumilshah1234@gmail.com"})
        Questions.delete_many({"email": "dhrumilshah1234@gmail.com"})


    def testLogin(self):
        tester = app.test_client(self)
        response = tester.post("/login", json={"email": "dhrumilshah1234@gmail.com", "password": "12345678"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testWrongLogin(self):
        tester = app.test_client(self)
        response = tester.post("/login", json={"email": "xyz@ncsu.edu", "password": "jytfyjtyj"})
        statuscode = response.status_code
        # User account not found
        self.assertEqual(statuscode, 400)

    def testWrongLoginPassword(self):
        tester = app.test_client(self)
        response = tester.post("/login", json={"email": "dhrumilshah1234@gmail.com", "password": "jytfyjtyj"})
        statuscode = response.status_code
        # User password not correct
        self.assertEqual(statuscode, 400)

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
        # New user created
        self.assertEqual(statuscode, 200)
    
    def testWrongRegisterExistingEmail(self):
        tester = app.test_client(self)
        req = {}
        req["firstName"] = "Rahul"
        req["lastName"] = "RK"
        req["email"] = "dhrumilshah1234@gmail.com"
        req["password"] = "12345678"
        req["confirmPassword"] = "12345678"
        urlToSend = "/register"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def testWrongRegisterNoMatchingPasswor(self):
        tester = app.test_client(self)
        req = {}
        req["firstName"] = "Rahul"
        req["lastName"] = "RK"
        req["email"] = "rrangar@ncsu.edu"
        req["password"] = "12345678"
        req["confirmPassword"] = "123456789"
        urlToSend = "/register"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def testdeletewrongApplication(self):
        tester = app.test_client(self)
        response = tester.post("/delete_application", json={"email": "dhrumilshah1234@gmail.com", "_id": "63800dfd2bf155063a7afbd9"})
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
        response = tester.post("/delete_question", json={"email": "dhrumilshah1234@gmail.com", "_id": "63800dfd2bf155063a7afbd9"})
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
            "email": "dhrumilshah1234@gmail.com",
            "image": ""
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

    def testWrongEmailModifyQuestion(self):
        tester = app.test_client(self)
        req = {
         "question": "Q1",
         "answer": "A1",
        "_id": "638bafe50012ef455196cc6e",
        "email": "a@a.com"
        }
        urlToSend = "/modify_question"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

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

    def testModifyApplicationNoDate(self):
        tester = app.test_client(self)
        req = {
            "companyName": "Qorvo",
            "jobTitle": "Software Engineer",
            "jobId": "122881",
            "description": "lkn",
            "url": "",
            "date": None,
            "status": "interview",
            "_id": "638eb81bff4164e60179bab2",
            "email": "dhrumilshah1234@gmail.com",
            "image": "www.google.com"
        }
        urlToSend = "/modify_application"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testWrongModifyApplicationMissingImage(self):
        tester = app.test_client(self)
        req = {
            "companyName": "Qorvo",
            "jobTitle": "Software Engineer",
            "jobId": "122881",
            "description": "lkn",
            "url": "",
            "date": "2022-12-02T21:26:03.739Z",
            "status": "interview",
            "_id": "638eb81bff4164e60179bab2",
            "email": "dhrumilshah1234@gmail.com",
        }
        urlToSend = "/modify_application"
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)

    def testWrongModifyApplicationStatusAndURL(self):
        tester = app.test_client(self)
        req = {
            "companyName": "k",
            "jobTitle": "jl",
            "jobId": "nln",
            "description": "lkn",
            "url": "lknl",
            "date": "2022-12-02T21:26:03.739Z",
            "status": "a",
            "_id": "638eb81bff4164e60179bab2",
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

    def testGenerateCoverLetter(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/generate_cv"
        req = {
            "email": email,
            "file": "",
            "context": "I want to be good at programaming",
            "job_desc": "We want embedded engineers."
        }
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testGenerateCoverLetterWithoutFile(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/generate_cv"
        req = {
            "email": email,
            "context": "I want to be good at programaming",
            "job_desc": "We want embedded engineers."
        }
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def testResumeSuggestions(self):
        tester = app.test_client(self)
        email = "dhrumilshah1234@gmail.com"
        urlToSend = f"/resume_suggest"
        req = {
            "email": email,
            "file": "",
            "job_desc": "We want embedded engineers."
        }
        response = tester.post(urlToSend, json = req)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__=="__main__":
     unittest.main()