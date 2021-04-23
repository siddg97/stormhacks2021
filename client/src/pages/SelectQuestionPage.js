import { useHistory } from 'react-router-dom';
import styled from 'styled-components';
import QuestionsForm from '../new-components/QuestionsForm';
import { SELECT_QUESTIONS_INSTRUCTIONS, SELECT_QUESTIONS_INFO, routes } from '../constants';

const Div = styled.div`
  max-width: 700px;
  margin: 0 auto
`;

const FormWrapper = styled.div`
  max-width: 700px;
  width: 100%;
  margin: 10px;
`;

const Header = styled.h1`
  text-align: center;
`;

const QuestionSelectPage = () => {
  const history = useHistory();

  const submit = (questions) => {
    history.push({
      pathname: routes.INTERVIEW,
      state: { questions },
    });
  };

  return (
    <Div>
      <Header>Instructions</Header>
      <ol>
        <li>Input the 5 questions you want InterviewBuddy to ask you</li>
        <li>Ensure your mic is working and your audio is on</li>
        <li>Press "Let's Practice!" to start the interview with our interview bot</li>
        <li>Record your answer by pressing "Start Recording" and press "Stop Recording" when you're done</li>
        <li>Either play back the recording, rerecord your answer, or press "Next" to continue</li>
      </ol>

      <Header>Select Questions</Header>
      <FormWrapper>
        <QuestionsForm handleSubmit={submit} />
      </FormWrapper>
    </Div>
  );
};

export default QuestionSelectPage;
