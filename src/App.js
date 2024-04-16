import Navbar from './Navbar';
import Home from './Home';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Portfolio from './Portfolio';
import NewStock from './NewStock';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="content">
          <Switch>
            <Route exact path="/">
              <Home />
            </Route>
            <Route exact path="/portfolio">
              <Portfolio />
            </Route>
            <Route exact path="/new-stock">
              <NewStock />
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
