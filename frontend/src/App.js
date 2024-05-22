import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import JobPreferences from './components/JobPreferences';
import ResumeUpload from './components/ResumeUpload';
import JobApplications from './components/JobApplications';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/preferences" component={JobPreferences} />
        <Route path="/upload" component={ResumeUpload} />
        <Route path="/applications" component={JobApplications} />
      </Switch>
    </Router>
  );
}

export default App;
