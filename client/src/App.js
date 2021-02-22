import styled from 'styled-components';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LandingPage from './components/LandingPage';
import ScanJobPage from './components/ScanJobPage';
import QuestionsPage from './components/QuestionsPage';
import QuestionChoicePage from './components/QuestionChoicePage';
import IntervieweeTipsPage from './components/IntervieweeTipsPage';
import InterviewerTipsPage from './components/InterviewerTipsPage';
import ResultsPage from './components/ResultsPage';
import InterviewPage from './components/InterviewPage';
import PeerMatchPage from './components/PeerMatchPage';
import Navbar from './components/Navbar';
import ProgressBar from './components/ProgressBar';
import './App.css';
import 'rsuite/dist/styles/rsuite-default.css';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';
import { useEffect, useState } from 'react';
import Question from './components/Question';

const queryClient = new QueryClient();

const Body = styled.div`
    max-width: 1500px;
    margin: 60px auto;
`;

function App() {
    const [uid, setUid] = useState('');
    const [softQs, setSoftQs] = useState([]);
    const [techQs, setTechQs] = useState([]);
    const [results, setResults] = useState([]);
    const [choseGen, setChoseGen] = useState(false);
    const [choseSoft, setChoseSoft] = useState(false);
    const [choseTech, setChoseTech] = useState(false);
    const [qid, setQid] = useState(1);
    const [currQ, setCurrQ] = useState(1);

    useEffect(() => {
        if (currQ < 5) {
            setCurrQ(currQ + 1);
        }
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [qid]);

    console.log({ uid });
    console.log({ softQs });
    console.log({ techQs });

    return (
        <QueryClientProvider client={queryClient}>
            <Router>
                <div className='App'>
                    <Navbar />
                    <Body>
                        <Switch>
                            <Route
                                path='/scan'
                                render={() => (
                                    <ScanJobPage
                                        setUid={setUid}
                                        setSq={setSoftQs}
                                        setTq={setTechQs}
                                    />
                                )}
                            />
                            <Route
                                path='/questions'
                                render={() => (
                                    <QuestionsPage
                                        softQs={softQs}
                                        techQs={techQs}
                                        uid={uid}
                                    />
                                )}
                            />
                            <Route
                                path='/choosequestions'
                                render={() => (
                                    <QuestionChoicePage
                                        setGen={setChoseGen}
                                        setSoft={setChoseSoft}
                                        setTech={setChoseTech}
                                    />
                                )}
                            />
                            <Route
                                path='/question'
                                render={() => (
                                    <Question
                                        uid={uid}
                                        qid={currQ}
                                        setQid={setQid}
                                        softQs={softQs}
                                        techQs={techQs}
                                        soft={choseSoft}
                                        tech={choseTech}
                                    />
                                )}
                            />
                            <Route path='/results'>
                                <div>Results go here...</div>
                            </Route>
                            <Route path='/'>
                                <LandingPage />
                            </Route>
                        </Switch>
                    </Body>
                </div>
            </Router>
            <ReactQueryDevtools initialIsOpen={false} />
        </QueryClientProvider>
    );
}

export default App;
