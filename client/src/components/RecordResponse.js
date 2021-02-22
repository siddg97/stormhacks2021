import React, { useState } from 'react';
import { useProcessAudio } from '../hooks';
import { ReactMic } from 'react-mic';

const RecordResponse = ({ uid, qid, setResult }) => {
    const [blob, setBlob] = useState(null);
    const [isRecording, setIsRecording] = useState(false);

    const handleRecord = () => setIsRecording(!isRecording);
    const handleStop = (recdAudio) => setBlob(recdAudio);

    const handleSubmit = () => {
        refetch();
    };

    const options = {
        onSuccess: (data) => {
            console.log({ data });
        },
        onError: (err) => {
            console.log(err);
        },
    };

    console.log({ blob });

    const { status, refetch } = useProcessAudio({
        blobState: blob?.blob ? blob.blob : null,
        qid,
        uid,
        options,
    });

    if (status === 'error') {
        return 'Something went wrong. Check console';
    }

    if (status === 'loading') {
        return 'Loading........';
    }

    return (
        <div>
            <ReactMic record={isRecording} onStop={handleStop} />
            <br />
            <br />
            <button onClick={handleRecord}>Record</button>
            <button onClick={handleSubmit}>Submit</button>
        </div>
    );
};

export default RecordResponse;
