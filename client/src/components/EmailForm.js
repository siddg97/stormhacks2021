import { useState } from 'react';
import { Form, FormGroup, FormControl, Button } from 'rsuite';
import styled from 'styled-components';

/**
 * TODO:
 * -  Validate email input
 */

const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const StyledFormControl = styled(FormControl)`
  width: 300px;
`;

const StyledForm = styled(Form)`
  margin: 10px;
`;

const EmailForm = () => {
  const [input, setInput] = useState('');

  const handleInputChange = (text) => {
    setInput(text);
  }

  const sendEmail = () => {
    console.log(`sending email to ${input}`);
  }

  return (
    <Container>
      <h5>Send a copy of the questions to your email</h5>
      <StyledForm layout="inline">
        <FormGroup>
          <StyledFormControl onChange={handleInputChange} type="email" placeholder={'Enter email here'} />
        </FormGroup>
        <Button onClick={sendEmail}>Email Me</Button>
      </StyledForm>
    </Container>
  );
};

export default EmailForm;