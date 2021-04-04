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
      <p>{SELECT_QUESTIONS_INSTRUCTIONS}</p>

      <Header>Select Your Questions</Header>
      <p>{SELECT_QUESTIONS_INFO}</p>
      <FormWrapper>
        <QuestionsForm handleSubmit={submit} />
      </FormWrapper>
    </Div>
  );
};

export default QuestionSelectPage;
