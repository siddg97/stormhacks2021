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

const AudioRecorder = ({ handleStop, isRecording }) => {
  return (
    <Div>
      <StyledMic record={isRecording} onStop={handleStop} />
    </Div>
  );
};

export default AudioRecorder;
