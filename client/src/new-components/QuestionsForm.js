import { useState } from 'react';
import styled from 'styled-components';
import { StyledButton as Button } from '../styles';

const Label = styled.label`
  color: var(--color-primary);
  font-weight: bold;
  padding-right: 40px;
`;

const Form = styled.form`
  background-color: rgba(196, 196, 196, 0.7);
  padding: 8px;
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
`;

const StyledButton = styled(Button)`
  margin: 30px auto 0 auto;
  display: block;
`;

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

    const invalidInputs = getEmptyInputs();
    if (!invalidInputs) {
      handleSubmit(questions);
    } else {
      setEmptyInputs(invalidInputs);
    }
  };

  const handleChange = (idx) => (event) => {
    questions[idx] = event.target.value;
  };

  return (
    <div>
      <Form id="questions">
        {questions.map((_, idx) => (
          <QuestionDiv>
            <Label htmlFor={`question${idx}`}>Question {idx + 1}</Label>
            <Input
              id={`question${idx}`}
              style={{ border: emptyInputs.has(idx) ? '2px solid red' : undefined }}
              onChange={handleChange(idx)}
              type="text"
            />
          </QuestionDiv>
        ))}
      </Form>
      <StyledButton onClick={submit} form="questions">Let's Practice!</StyledButton>
    </div>
  );
};

export default QuestionsForm;
