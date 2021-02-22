import styled from 'styled-components';

const Form = styled.form`
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid black;
  padding: 20px;
  width: 550px;
`;

const Input = styled.input`
  width: 30px;
  height: 30px;
`;

const Label = styled.label`
  margin-right: 40px;
`;

const QuestionChoice = ({ title, description, onChecked }) => {
  return (
    <Form>
      <Label>
        <h5>{title}</h5>
        <p>{description}</p>
      </Label>
      <Input type="checkbox" onClick={onChecked} />
    </Form>
  );
};

export default QuestionChoice;