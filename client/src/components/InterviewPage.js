import { useState } from 'react';
import { Input, Button } from 'rsuite';
import Question from './Question';
import styled from 'styled-components';

const ButtonContainer = styled.div`
  display: flex;
  justify-content: space-between;
`

const Placeholder = styled.div`
  background-color: lightblue;
  width: 500px;
  height: 500px;
`;

const StyledInput = styled(Input)`
  margin: 20px auto;
  max-width: 800px;
`;

const Container = styled.div`
  display: flex;
`;
const InterviewPage = () => {
  const [notes, setNotes] = useState("");

  const handleInputChange = (text) => {
    setNotes(text);
  };

  return (
    <div>
      {/* Interviewee */}
      {/* <Question
        questionNumber={'1'}
        question={'Tell me about yourself'}
      />
      <ButtonContainer>
        <div>
            <Button>Start recording</Button>
            <Button>Stop recording</Button>
            <Button>Rerecord</Button>
        </div>
        <div>
          <Button>Next Question</Button>
        </div>
      </ButtonContainer> */}

      {/* Interviewer */}
      <div>
        <Container>
          <Placeholder />
          <div>
            <Question
              questionNumber={'1'}
              question={'Tell me about yourself'}
            />
            <StyledInput onChange={handleInputChange} componentClass="textarea" rows={20} placeholder="Paste job description here" />
          </div>
        </Container>
        <Button>Next Question</Button>
      </div>


    </div>
  );
}

export default InterviewPage;