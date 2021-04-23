import React, { useState } from 'react';
import AudioRecorder from './AudioRecorder';
import { ReactComponent as Bot } from '../svg/bot.svg';
import styled from 'styled-components';

const StyledBot = styled(Bot)`
  width: 300px;
  height: 300px;
  align-self: center;
  padding: 30px;
`;

const Div = styled.div`
  display: flex;
  flex-direction: column;
`;

const Question = ({ question, questionNum, handleQuestionDone, isLastQ }) => {
  const [answer, setAnswer] = useState(null);

  const handleNext = () => {
    handleQuestionDone(answer);
  };

  return (
    <Div>
      <h1>Q{questionNum}: {question}</h1>
      <StyledBot />
      <AudioRecorder onFinish={setAnswer}/>
      <div>
        <button onClick={handleNext}>{isLastQ ? 'Finish' : 'Next'}</button>
      </div>
    </Div>
  )
};

export default Question;
