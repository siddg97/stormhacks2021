import { useState } from 'react';
import { useLocation, useHistory } from 'react-router-dom';
import Question from '../new-components/Question';
import { routes } from '../constants';
import styled from 'styled-components';
import { useSetQuestions, useSubmitAnswer, submitAnswer } from '../hooks';
import { useMutation } from 'react-query';

const Div = styled.div`
  display: flex;
  flex-flow: column;
  height: 100%;
  align-items: center;
`;

const InterviewPage = () => {
  const history = useHistory();

  const [idx, setIdx] = useState(0);
  const [answers, _] = useState([]);

  const textQuestions = ['t1', 't2', 't3', 't4', 't5'];
  // const { textQuestions } = useLocation().state;

  const mutation = useMutation(file => submitAnswer(file, questions[idx].id), {
    onSuccess: (data) => console.log('onSuccess: ', data),
    onError: (error) => console.log('onError: ', error),
  });

  const { isLoading, isError, questionIDs, error } = useSetQuestions(textQuestions);
  if (isLoading) return <span>Loading...</span>
  if (isError)   return <span>Error: {error.message}</span>

  const questions = textQuestions.map((text, idx) => ({
    id: questionIDs[idx],
    text,
  }));

  const handleQuestionDone = (answer) => {
    if (idx < questions.length) {
      answers[idx] = answer;

      const blob = answer ? answer.blob : null;
      const file = new File([blob], `${questions[idx].id}.webm`)
      mutation.mutate(file);
    }

    if (idx < questions.length - 1) {
      setIdx(idx + 1);
    } else {
      history.push(routes.RESULTS);
    }
  };

  return (
    <Div>
      <div>
        <h2>{idx + 1}/{questions.length}</h2>
        <Question
          question={questions[idx].text}
          questionNum={idx + 1}
          handleQuestionDone={handleQuestionDone}
          isLastQ={idx === questions.length - 1}
        />
      </div>
    </Div>
  );
};

export default InterviewPage;
