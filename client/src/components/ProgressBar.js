import { Steps } from 'rsuite';

const ProgressBar = () => {
  return (
    <Steps current={0}>
    <Steps.Item description="Scan" />
    <Steps.Item description="Results" />
    <Steps.Item description="Question Select" />
    <Steps.Item description="Instruction & Tips" />
    <Steps.Item description="Mock Interview" />
    <Steps.Item description="Feedback" />
  </Steps>
  );
};

export default ProgressBar;