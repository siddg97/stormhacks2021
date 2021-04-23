import { useState } from 'react';
import { ReactMic } from 'react-mic';
import styled from 'styled-components';

const Div = styled.div`
`;

const StyledMic = styled(ReactMic)`
`;

const RecordButton = styled.button`
  background-color: ${props => props.isRecording ? "red" : "green"}
`;

const ButtonsDiv = styled.div`
  display: flex;
  justify-content: space-evenly;
`;

const AudioRecorder = ({ onFinish }) => {
  const [isRecording, setIsRecording] = useState(false);

  const handleRecord = () => setIsRecording(!isRecording);

  const handleStop = (recdAudio) => {
    console.log(recdAudio);
    onFinish(recdAudio);
  };

  const playRecording = () => {
    console.log('playing recording');
  };

  return (
    <Div>
      <StyledMic record={isRecording} onStop={handleStop} />
      <ButtonsDiv>
        <RecordButton onClick={handleRecord} isRecording={isRecording}>
          {isRecording ? 'Stop Recording' : 'Start Recording'}
        </RecordButton>
        <button onClick={playRecording}>Play recording</button>
      </ButtonsDiv>
    </Div>
  );
};

export default AudioRecorder;
