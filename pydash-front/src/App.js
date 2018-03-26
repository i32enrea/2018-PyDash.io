import React, { Component } from 'react';
import './App.css';
import Login from './login/Login';
import Dashboard from './dashboard/Dashboard';
import Overview from './overview/Overview';
import { Switch, Route } from 'react-router-dom'

class App extends Component {
  state = {
    loggedIn: false
  };

  handleChange = key => event => {
    this.setState({
      [key]: event.target.value
    });
  };

  render() {
    return (
      <div className="App">
        <Switch>
          <Route exact path='/' component={Dashboard} />
          <Route path='/login' component={Login} />
          <Route path='/overview' component={Overview} />
        </Switch>
      </div>
    );
  }
}

export default App;
