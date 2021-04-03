import { useHistory } from 'react-router-dom';
import About from '../new-components/About';
import { routes } from '../constants';
import { ReactComponent as Logo } from '../logoWithTitle.svg';

const LandingPage = () => {
  const history = useHistory();

  const start = () => history.push(routes.SELECT_QUESTIONS);

  return (
    <div>
      <Logo />
      <h1>Prepare for interviews with AI</h1>
      <p>InterviewBuddy helps you prepare for interviews by using AI to provide insights from one way interviews.</p>
      <button onClick={start} type="button">Let's Start</button>
      {/* <About /> */}
    </div>
  );
};

export default LandingPage;
