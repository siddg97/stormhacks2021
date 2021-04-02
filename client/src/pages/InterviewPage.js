import { useState } from 'react';
import Question from '../new-components/Question';

const InterviewPage = ({ questions }) => {
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
    }
  };

  return (
    <div>
      <div>{idx + 1}/{questions.length}</div>
      <Question
        question={questions[idx]}
        questionNum={idx + 1}
        handleQuestionDone={handleQuestionDone}
      />
    </div>
  );
};

export default InterviewPage;
