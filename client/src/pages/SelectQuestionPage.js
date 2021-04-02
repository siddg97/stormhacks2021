
import { useHistory } from 'react-router-dom';
import QuestionsForm from '../new-components/QuestionsForm';
import { SELECT_QUESTIONS_INSTRUCTIONS, SELECT_QUESTIONS_INFO, routes } from '../constants';

const QuestionSelectPage = () => {
  const history = useHistory();

  const submit = (questions) => {
    history.push({
      pathname: routes.INTERVIEW,
      state: { questions },
    });
  };

  return (
    <div>
      <h1>Instructions</h1>
      <p>{SELECT_QUESTIONS_INSTRUCTIONS}</p>

      <h1>Select Your Questions</h1>
      <p>{SELECT_QUESTIONS_INFO}</p>
      <QuestionsForm handleSubmit={submit} />
    </div>
  );
};

export default QuestionSelectPage;
