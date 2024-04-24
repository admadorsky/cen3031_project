import Navbar from './Navbar';
import Home from './Home';
import Login from './Login';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Portfolio from './Portfolio';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className='content'>
          <Switch>
            <Route exact path="/">
              <Login />
            </Route>
            <Route exact path="/home">
              <Home />
            </Route>
            <Route exact path="/portfolio">
              <Portfolio />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
