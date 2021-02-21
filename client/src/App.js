import styled from 'styled-components';
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from 'react-router-dom';
import LandingPage from './components/LandingPage';
import ScanJobPage from './components/ScanJobPage';
import QuestionsPage from './components/QuestionsPage'
import QuestionChoicePage from './components/QuestionChoicePage'
import IntervieweeTipsPage from './components/IntervieweeTipsPage'
import InterviewerTipsPage from './components/InterviewerTipsPage'
import ResultsPage from './components/ResultsPage'
import InterviewPage from './components/InterviewPage'
import PeerMatchPage from './components/PeerMatchPage'
import Navbar from './components/Navbar';
import ProgressBar from './components/ProgressBar';
import './App.css';
import 'rsuite/dist/styles/rsuite-default.css';

const Body = styled.div`
  max-width: 1500px;
  margin: 60px auto;
`;

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Body>
          <Switch>
            <Route path="/scan">
              <ScanJobPage />
            </Route>
            <Route path="/questions">
              <QuestionsPage />
            </Route>
            <Route path="/choosequestions">
              <QuestionChoicePage />
            </Route>
            <Route path="/">
              <ProgressBar />
            </Route>
          </Switch>
        </Body>
      </div>
    </Router>
  );
}

export default App;
