# Backend Local Development Setup

### Installation

Clone the repository (if you haven't already)

```
git clone https://github.com/jayrajmulani/se-group1-project2.git
```

Open a new terminal inside the backend directory.

`se-group1-project2\backend`

Create a virtual environment called `venv`

```
python -m venv venv
```

For Windows - Activate the virtual environment

```
venv\Scripts\activate.bat
```

For Mac OS - Activate the virtual environment

```
source venv/bin/activate
```

Install required packages for the Flask server

```
pip install -r requirements.txt
```

The flask server runs in [http://localhost:8000](http://localhost:8000)

### Start the server in development mode

Run the flask server.

```
python app.py
```

### Backend Test

Run this command to test the backend APIs

```
python backend\tests.py
```
