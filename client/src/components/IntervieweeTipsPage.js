import { Button } from 'rsuite';

const IntervieweeTipsPage = () => {
  const handleButtonClick = () => {
    console.log('click');
  }

  return (
    <div>
      <h1>Interviewee Instructions</h1>
      <p>Here is how the mock interview will be conducted.</p>
      <p>Ensure your camera and mic is ready before starting. Once you are ready, press “I’m Ready” at the bottom, you will be redirected to join a room with our interview bot. The interviewer will ask 5 questions, each randomly selected from the pool of available questions. Questions will be narrated so make sure your audio works! After you complete your answer, press the “Next Question” button. After all questions are asked, the interview bot will provide useful insights such as:</p>
      <ul>
        <li>Amount of eye contact</li>
        <li>Enunciation of words</li>
        <li>Words per minute</li>
        <li>Frequency of filler words</li>
      </ul>
      <h1>Tips</h1>
      <p>Here are some tips before you begin to become a interview rockstar!</p>
      <ul>
        <li>When answering questions follow the STAR method, describe the situation, task, action, and result of your acomplishments.</li>
        <li>Maintain eye contact with the camera, pretend they are the eyes of the interviewer! </li>
        <li>Take your time to enunciate your words</li>
        <li>Pace yourself, try not to talk too fast</li>
        <li>Be mindful of your use of filler words like “ums” “ahs” </li>
      </ul>
      <Button onClick={handleButtonClick}>I'm Ready</Button>
    </div>
  );
};

export default IntervieweeTipsPage;