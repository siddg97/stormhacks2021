import { useState } from 'react';
import { useLocation, useHistory } from 'react-router-dom';
import Question from '../new-components/Question';
import { routes } from '../constants';
import styled from 'styled-components';

const Div = styled.div`
  display: flex;
  flex-flow: column;
  height: 100%;
  ${'' /* justify-content: center; */}
  align-items: center;
`;

const InterviewPage = () => {
  const history = useHistory();
  const { questions } = useLocation().state;

  const [idx, setIdx] = useState(0);
  const [answers, _] = useState([]);

  const setAnswer = (answer) => {
    answers[idx] = answer;
  };

  const handleQuestionDone = (answer) => {
    if (idx < questions.length) {
      setAnswer(answer);
    }

    if (idx < questions.length - 1) {
      setIdx(idx + 1);
    } else {
      console.log('interview done');
      history.push(routes.RESULTS);
    }
  };

  return (
    <Div>
      <div>
        <h2>{idx + 1}/{questions.length}</h2>
        <Question
          question={questions[idx]}
          questionNum={idx + 1}
          handleQuestionDone={handleQuestionDone}
          isLastQ={idx === questions.length - 1}
        />
      </div>
    </Div>
  );
};

export default InterviewPage;
