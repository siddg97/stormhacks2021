import { useHistory } from 'react-router-dom';
import styled from 'styled-components';
import { Button } from 'rsuite';

const Placeholder = styled.div`
  background-color: lightblue;
  height: 500px;
  width: 650px;
`;

const About = styled.div`
  margin: 60px auto;
  text-align: center;
  max-width: 500px;
`;

const Intro = styled.div`
  display: flex;
  justify-content: space-evenly;
  margin: 60px;
`;

const IntroSection = styled.div`
  margin: auto 30px;
`;

const Header1 = styled.h1`
`;

const Header2 = styled.h2`
`;

const Text = styled.p`
  margin-top: 40px;
  margin-bottom: 40px;
`;

const Image = styled.div`
  height: 100px;
  width: 100px;
  background-color: lightblue;
  margin: 10px;
`;

const ImageContainer = styled.div`
  display: flex;
`

const LandingPage = () => {
  const history = useHistory();

  const start = () => {
    history.push('/scan');
  };

  return (
    <>
      <Intro>
        <IntroSection>
          <Placeholder />
        </IntroSection>

        <IntroSection>
          <Header1>Prepare for interviews with AI</Header1>
          <Text>LOGO helps you prepare for interviews by using AI to create relevant questions and provide mock interviews.</Text>
          <Button onClick={start}>Let's Start</Button>
        </IntroSection>
      </Intro>

      <About>
        <Header2>About Us</Header2>
        <Text>LOGO was created because as college students, we recognized the need for smarter tools to prepare for interviews. Using AI, we are able to read job descriptions and formulate relevant questions. Then usinmg those questions, we can conduct mock interviews, either by matching you with another person using our matching algorithm or by our Interviewer Bot. Then, we provide feedback and insights using AI.</Text>
        <ImageContainer>
          <Image />
          <Image />
          <Image />
          <Image />
        </ImageContainer>
      </About>
    </>
  );
};

export default LandingPage;