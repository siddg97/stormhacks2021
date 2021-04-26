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

const RecordButton = styled.button`
  background-color: ${props => props.isRecording ? "red" : "green"}
`;

const Question = ({ question, questionNum, submitAnswer, isLastQ }) => {
  const [answer, setAnswer] = useState(null);
  const [isRecording, setIsRecording] = useState(false);

  const handleNext = () => {
    submitAnswer(answer);
  };

  const playRecording = () => {
    console.log('playing recording');
  };

  const handleRecord = () => setIsRecording(!isRecording);

  const handleStop = (recdAudio) => {
    setAnswer(recdAudio);
  };

  return (
    <Div>
      <h1>Q{questionNum}: {question}</h1>
      <StyledBot />
      <AudioRecorder handleRecord={handleRecord} handleStop={handleStop} isRecording={isRecording}/>
      <RecordButton onClick={handleRecord} isRecording={isRecording}>
        {isRecording ? 'Stop Recording' : 'Start Recording'}
      </RecordButton>
      <button onClick={playRecording} disabled={isRecording || !answer}>
        Play recording
      </button>
      <button onClick={handleNext} disabled={isRecording || !answer}>
        {isLastQ ? 'Finish' : 'Next'}
      </button>
    </Div>
  )
};

export default Question;
