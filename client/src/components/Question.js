import React from 'react';
import { useHistory } from 'react-router';
import RecordResponse from './RecordResponse';

const Question = ({ uid, qid, setQid, softQs, techQs, soft, tech, setResult }) => {
    const history = useHistory();
    let qs = [];
    if (soft) {
        qs = [...softQs];
    }
    if (tech) {
        qs = [...qs, ...techQs];
    }

    if (qid >= 5) {
        history.push('/results');
    }

    const randQ = qs[Math.floor(Math.random() * qs.length)];

    return (
        <div>
            <h1>{`Q${qid}: ${randQ}`}</h1>
            <RecordResponse uid={uid} qid={qid} setResult={setResult} />
            <br />
            <button onClick={() => setQid(qid + 1)}>Next</button>
        </div>
    );
};

export default Question;
