import axios from 'axios';

export const setQuestions = async (questions) => {
  const body = JSON.stringify({ questions });
  const { data } = await axios.post('/api/questions', body);
  return data;
};

export const submitAnswer = async (file, questionID) => {
  const formData = new FormData();
  formData.append('audio', file);
  formData.append('name', 'testname');

  const { data } = await axios.post(`/api/questions/${questionID}/answer`, formData);
  return data;
}

export const getResult = async (pollURL) => {
  const { data } = await axios.get(pollURL);
  return data;
}