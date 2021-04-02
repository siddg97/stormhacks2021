import { useState } from 'react';

const QuestionsForm = ({ handleSubmit }) => {
  const NUM_QUESTIONS = 5;

  const [questions, _] = useState([...Array(NUM_QUESTIONS).fill('')]);
  const [emptyInputs, setEmptyInputs] = useState(new Set());

  const getEmptyInputs = () => questions.reduce((acc, val, idx) => {
    if (val === '') {
      acc.add(idx);
    }
    return acc;
  }, new Set());

  const submit = (event) => {
    event.preventDefault();

    setEmptyInputs(getEmptyInputs());

    if (!emptyInputs.size) {
      handleSubmit(questions);
    }
  };

  const handleChange = (idx) => (event) => {
    questions[idx] = event.target.value;
  };

  return (
    <form>
      {questions.map((_, idx) => (
        <div>
          <label htmlFor={`question${idx}`}>Question {idx + 1}</label>
          <input
            id={`question${idx}`}
            style={{ border: emptyInputs.has(idx) ? '2px solid red' : undefined }}
            onChange={handleChange(idx)}
            type="text"
          />
        </div>
      ))}
      <input onClick={submit} type="submit" value="Let's Practice!" />
    </form>
  );
};

export default QuestionsForm;
