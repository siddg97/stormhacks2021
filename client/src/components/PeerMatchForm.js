import { Form, FormGroup, FormControl, ControlLabel, HelpBlock, Button, ButtonToolbar } from 'rsuite';
import styled from 'styled-components';
import { InputPicker } from 'rsuite';

const Input = styled.input`
  ${'' /* width: 30px; */}
  ${'' /* height: 30px; */}
`;

const Label = styled.label`
  ${'' /* margin-right: 40px; */}
`;

const CheckboxForm = styled(Form)`
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid black;
  padding: 10px;
  width: 400px;
`;

const data = [
  {
    label: "Software Engineer",
    value: "Software Engineer",
  },
  {
    label: "UX Designer",
    value: "UX Designer",
  },
  {
    label: "DevOps Engineer",
    value: "DevOps Engineer",
  },
];

const PeerMatchForm = () => {
  return (
    <Form>
        <FormGroup>
          <ControlLabel>Full Name</ControlLabel>
          <FormControl/>
        </FormGroup>
        <FormGroup>
          <ControlLabel>Email</ControlLabel>
          <FormControl type="email" />
        </FormGroup>
        <FormGroup>
          <ControlLabel>Company</ControlLabel>
          <FormControl />
        </FormGroup>
        <FormGroup>
          <ControlLabel>Job Type</ControlLabel>
          <InputPicker data={data} style={{ width: 224 }} />
        </FormGroup>
        <FormGroup>
          <ControlLabel>Resume</ControlLabel>
          <Button>Upload Resume</Button>
        </FormGroup>
        <FormGroup>
          <ControlLabel>Question Categories</ControlLabel>
          <FormGroup>
            <CheckboxForm>
              <Label>General Questions</Label>
              <Input type="checkbox" />
            </CheckboxForm>
            <CheckboxForm>
              <Label>Soft Skill Questions</Label>
              <Input type="checkbox" />
            </CheckboxForm>
            <CheckboxForm>
              <Label>Hard Skill Questions</Label>
              <Input type="checkbox" />
            </CheckboxForm>
          </FormGroup>
        </FormGroup>
        <FormGroup>
          <ButtonToolbar>
            <Button appearance="primary">Submit</Button>
          </ButtonToolbar>
        </FormGroup>
      </Form>
  )
}

export default PeerMatchForm;