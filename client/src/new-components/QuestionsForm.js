import { useState } from 'react';
import styled from 'styled-components';
import { QUESTION_BANK } from '../constants';

const Label = styled.label`
  color: var(--color-primary);
  font-weight: bold;
  padding-bottom: 5px;
`;

const Form = styled.form`
  background-color: rgba(196, 196, 196, 0.7);
  padding: 10px;
  border-radius: 3px;
  margin-bottom: 10px;
`;

const Input = styled.input`
  border: 2px solid white;
  background: white;
  border-radius: 3px;
  box-sizing: border-box;
  flex-grow: 1;
`;

const QuestionDiv = styled.div`
  padding: 8px;
  display: flex;
  flex-direction: column;
`;

const Button = styled.button`
  margin: 30px auto 0 auto;
  display: block;
`;

const QuestionsForm = ({ handleSubmit }) => {
  const NUM_QUESTIONS = 5;

  const getRandomQs = () => {
    return [...QUESTION_BANK].sort(() => 0.5 - Math.random()).slice(0, NUM_QUESTIONS);
  }

  const [questions, setQuestions] = useState([...Array(NUM_QUESTIONS).fill('')]);
  const [sampleQs, _] = useState(getRandomQs());

  const submit = (event) => {
    event.preventDefault();

    const qs = questions.map((q, idx) => q === '' ? sampleQs[idx] : q)
    handleSubmit(qs);
  };

  const handleChange = (idx) => (event) => {
    questions[idx] = event.target.value;
    setQuestions([...questions]);
  };

  return (
    <div>
      <Form id="questions">
        {questions.map((_, idx) => (
          <QuestionDiv>
            <Label htmlFor={`question${idx}`}>Question {idx + 1}</Label>
            <Input
              id={`question${idx}`}
              onChange={handleChange(idx)}
              type="text"
              placeholder={sampleQs[idx]}
            />
          </QuestionDiv>
        ))}
      </Form>

      <Button onClick={submit} form="questions">Let's Practice!</Button>
    </div>
  );
};

export default QuestionsForm;
