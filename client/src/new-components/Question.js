import React, { useState } from 'react';
import AudioRecorder from './AudioRecorder';

const Question = ({ question, questionNum, handleQuestionDone }) => {
  const [answer, setAnswer] = useState(null);

  const playRecording = () => {
    console.log('playing recording');
  };

  const handleNext = () => {
    handleQuestionDone(answer);
  };

  return (
    <div>
      <div>Q{questionNum}: {question}</div>
      <AudioRecorder onFinish={setAnswer}/>
      <div>
        <button onClick={playRecording}>Play recording</button>
        <button onClick={handleNext}>Next</button>
      </div>
    </div>
  )
};

export default Question;
