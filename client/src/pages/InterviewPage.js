import { useState, useEffect } from 'react';
import { useLocation, useHistory } from 'react-router-dom';
import Question from '../new-components/Question';
import { routes } from '../constants';
import styled from 'styled-components';
import { useSetQuestions } from '../hooks';
import { submitAnswer } from '../api';
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
  const [pollURLs, setPollURLs] = useState([]);

  const { questions: textQuestions } = useLocation().state;

  useEffect(() => {
    if (pollURLs.length === textQuestions.length) {
      history.push({
        pathname: routes.RESULTS,
        state: { pollURLs }
      });
    }
  }, [pollURLs, textQuestions, history]);

  const mutation = useMutation(file => submitAnswer(file, questions[idx].id));

  const { isLoading, isError, questionIDs, error } = useSetQuestions(textQuestions);
  if (isLoading) return <span>Loading...</span>
  if (isError)   return <span>Error: {error.message}</span>

  const questions = textQuestions.map((text, idx) => ({
    id: questionIDs[idx],
    text,
  }));

  if (mutation.isLoading && idx === textQuestions.length - 1) {
    return <span>Loading...</span>
  }

  const handleQuestionDone = (answer) => {
    if (idx < questions.length) {
      const blob = answer ? answer.blob : null;
      const file = new File([blob], `${questions[idx].id}.webm`)

      mutation.mutate(file, {
        onSuccess: (data) => {
          console.log(data);
          pollURLs[idx] = data.poll_url;
          setPollURLs([...pollURLs]);
        },
        onError: (error) => console.log('onError: ', error),
      });
    }

    if (idx < questions.length - 1) {
      setIdx(idx + 1);
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
