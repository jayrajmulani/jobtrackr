## Install NPM dependencies

```
cd se-group1-project2/ui
npm install
```

### Development Mode

In the ui folder of project directory, you can run:

```
npm start
```

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

### Production Optimised Build

```
yarn build
```

Builds the app for production to the `build` folder.\
It bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

# Directory Structure

<pre>
. 
├── package-lock.json
├── package.json
├── public
│   ├── favicon.ico
│   └──index.html
└── src
    ├── App.jsx
    ├── App.scss
    ├── Components
    │   ├── AddApplication
    │   │   ├── AddApplication.jsx
    │   │   └── EditApplication.jsx
    │   ├── AddQuestion
    │   │   ├── AddQuestion.jsx
    │   │   └── EditQuestion
    │   ├── LandingPage
    │   │   ├── LandingPage.jsx
    │   │   └──LandingPage.scss
    │   ├── LoginPage
    │   │   ├── LoginPage.jsx
    │   │   └──LoginPage.scss
    │   ├── ManageFiles
    │   │   └── ManageFiles.jsx
    │   ├── Profile
    │   │   ├── Profile.jsx
    │   │   └── Profile.scss    
    │   ├── QA
    │   │   ├── QA.jsx
    │   │   └── QA.scss    
    │   ├── QuestionAnswers
    │   │   └── QuestionAnswers.jsx
    │   ├── RegisterPage
    │   │   ├── RegisterPage.jsx
    │   │   └── RegisterPage.scss    
    │   └── SavedJobs
    │       ├── AddSavedJob.jsx
    │       ├── EditSavedJob.jsx
    │       ├── SavedJob.jsx
    │       └── SavedJob.scss
    ├── config.js
    ├── index.js
    ├── index.scss    
    ├── logo.svg
    ├── reportWebVitals.js
    └── setupTests.js
</pre>