import { Button } from 'rsuite';

const InterviewerTipsPage = () => {
  const handleButtonClick = () => {
    console.log('click');
  }

  return (
    <div>
      <h1>Interviewer Instructions</h1>
      <p>Here is how you will play the role of interviewer</p>
      <p>Ensure your camera and mic is ready before starting. Once you are ready, press “I’m Ready” at the bottom, you will be redirected to join a room with your peer interviewee. The system will give you questions to ask the interviewee or you can ask your own! Take notes when the interviewee is answering the question. Note that each question has its own seperate notes  so make sure to finish writing before pressing “next question”.</p>
      <p>After all questions are asked, the roles are swapped!</p>

      <h1>Summary of Interviewee</h1>
      <p>Using smmry we have created guides.</p>
      <p>Resume Summary: summary goes here...</p>
      <p>Job Description Summary: summary goes here...</p>

      <h1>Tips</h1>
      <p>Here are some tips to play the perfect interviewer</p>
      <ul>
        <li>Nod and smile periodically to the interviewee</li>
        <li>Maintain eye contact with the camera, pretend they are the eyes of the interviewee!</li>
      </ul>

      <Button onClick={handleButtonClick}>I'm Ready</Button>
    </div>
  );
};

export default InterviewerTipsPage;