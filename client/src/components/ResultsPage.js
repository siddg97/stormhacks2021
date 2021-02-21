import Statistic from './Statistic';
import EmailForm from './EmailForm';
import styled from 'styled-components';

const StatsContainer = styled.div`
  display: flex;
`;

const ResultsPage = () => {
  return (
    <div>
      <h1>Results</h1>
      <StatsContainer>
        <Statistic
          value={'80%'}
          title={'Amount of eye contact'}
          description={'Amount of eye contact Try to maintain an 80% eye contact rate. It is natural to break contact as you speak so 100% is not expected.'}
        />
        <Statistic
          value={'90%'}
          title={'Enunciation of words'}
          description={'Take your time to properly enunciate each word, sometimes your interviewer may misunderstand you. This is especially exasperated by online interviews.'}
        />
        <Statistic
          value={'100wpm'}
          title={'Words per minute'}
          description={'Try to aim for your natural talking speed, conversational speed is around 130 to 150 words per minute.'}
        />
        <Statistic
          value={'11 per min'}
          title={'Frequency of filler words'}
          description={'Be mindful of how many filler words you use such as “um” and “ahs”'}
        />


      </StatsContainer>
      <h1>Peer Feedback</h1>
      <p>Here is the peer feedback based on your answers to questions. </p>
      <p>
        Q1: Tell me about yourself<br />
        Notes: aaaaaaaaaaaaaaaaaa<br />
        Q2:<br />
        Notes:<br />
      </p>
      <EmailForm />
    </div>
  )
};

export default ResultsPage;