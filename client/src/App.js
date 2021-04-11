import styled from 'styled-components';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import InterviewPage from './pages/InterviewPage';
import SelectQuestionPage from './pages/SelectQuestionPage';
import ResultsPage from './pages/ResultsPage';
import { QueryClient, QueryClientProvider } from 'react-query';
import { ReactQueryDevtools } from 'react-query/devtools';
import { useEffect, useState } from 'react';
import { routes } from './constants';
import GlobalStyle from './styles';
import Navbar from './new-components/Navbar';

const queryClient = new QueryClient();

const Body = styled.div`
    ${'' /* max-width: 1500px; */}
    ${'' /* margin: 60px auto; */}
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
                <GlobalStyle />
                <div className='App'>
                    <Navbar />
                    <Body>
                        <Switch>
                            <Route path={routes.INTERVIEW}>
                                <InterviewPage />
                            </Route>
                            <Route path={routes.RESULTS}>
                                <ResultsPage />
                            </Route>
                            <Route path={routes.SELECT_QUESTIONS}>
                                <SelectQuestionPage />
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
