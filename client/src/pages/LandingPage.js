import { useHistory } from 'react-router-dom';
import About from '../new-components/About';
import styled from 'styled-components';
import { routes } from '../constants';
import { ReactComponent as Logo } from '../logoWithTitle.svg';
import { StyledButton } from '../styles';

const Div = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const LandingDiv = styled.div`
  box-sizing: border-box;
  max-width: 450px;
  padding: 50px 0;
`;

const AboutDiv = styled.div`
  max-width: 600px;
  padding: 50px;
`;

const Button = styled(StyledButton)`
  width: 100%;
  margin: 10px 0;
`;

const Text = styled.p`
  padding: 10px 0;
`;

const Header = styled.h1`
  font-size: 2.8em;
`;

const LandingPage = () => {
  const history = useHistory();

  const start = () => history.push(routes.SELECT_QUESTIONS);

  return (
    <Div>
      <LandingDiv>
        <Logo />
        <Header>Prepare for interviews with AI</Header>
        <Text>InterviewBuddy helps you prepare for interviews by using AI to provide insights from one way interviews.</Text>
        <Button onClick={start} type="button">Let's Start</Button>
      </LandingDiv>
      <AboutDiv>
        <About />
      </AboutDiv>
    </Div>
  );
};

export default LandingPage;
