import { useQuery } from 'react-query';
import axios from 'axios';

const processRecording = async (blob, uid) => {
    const formData = new FormData();
    formData.append('audio', blob);

    await axios.post(`/api/submit-answer/${uid}`, formData, { timeout: 300000 });
};

export const useProcessAudio = ({ blobState, qid, uid, options }) => {
    return useQuery(`process-audio-${qid}`, () => processRecording(blobState, uid), {
        retry: 0,
        enabled: false,
        refetchOnWindowFocus: false,
        ...options,
    });
};

const getQuestions = async (description) => {
    const body = { jobdesc: JSON.stringify(description) };
    const { data } = await axios.post('/api/gen-questions', body);
    return data;
};

export const useGetQuestions = ({ description, options }) => {
    return useQuery(`get-questions`, () => getQuestions(description), {
        retry: 0,
        enabled: false,
        refetchOnWindowFocus: false,
        ...options,
    });
};

const setQuestions = async (questions) => {
    const body = JSON.stringify({ questions });
    const { data } = await axios.post('/api/questions', body);
    return data;
};

export const useSetQuestions = (questions) => {
    const {
        isLoading, isError, data, error,
    } = useQuery('questionIDs', () => setQuestions(questions));

    return { isLoading, isError, error, questionIDs: data && data['questions'] };
};

export const submitAnswer = async (file, questionID) => {
    const formData = new FormData();
    formData.append('audio', file);
    formData.append('name', 'testname');

    const { data } = await axios.post(`/api/questions/${questionID}/answer`, formData);
    return data;
}
