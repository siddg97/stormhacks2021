import { useState } from 'react';
import { ReactMic } from 'react-mic';

const AudioRecorder = ({ onFinish }) => {
  const [isRecording, setIsRecording] = useState(false);

  const handleRecord = () => setIsRecording(!isRecording);

  const handleStop = (recdAudio) => {
    console.log(recdAudio);
    onFinish(recdAudio);
  };

  return (
    <div>
      <ReactMic record={isRecording} onStop={handleStop} />
      <div>
        <button onClick={handleRecord}>
          {isRecording ? 'Stop Recording' : 'Start Recording'}
        </button>
      </div>
    </div>
  );
};

export default AudioRecorder;
