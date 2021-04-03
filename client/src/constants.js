export const routes = Object.freeze({
  SELECT_QUESTIONS: '/questions',
  INTERVIEW: '/interview',
});

export const SELECT_QUESTIONS_INSTRUCTIONS = `
First, input the 5 questions you want InterviewBuddy to ask you. Once you are ready, press “Let’s Practice” at the bottom, you will be redirected to join a room with our interview bot. Ensure your mic is working before starting.

The interviewer will ask 5 questions, questions will be narrated so make sure your audio works!

To start your reponse, press “Start Recording” then “Stop Recording” when finished, either choose to rerecord, or go to the next question when prompted.
After all questions are asked, the interview bot will provide useful insights such as:
- Amount of eye contact
- Enunciation of words
- Words per minute
- Frequency of filler words
`;

export const SELECT_QUESTIONS_INFO = `
Only the category of questions you select will be asked to you during the mock interview. A random question will be pulled from the customized pool
`;

export const ABOUT_TEXT = `Due to the coronavirus a lot of college students are having difficulty finding a job, whether that be an internship or a full-time position.

We recognize that a lot of the tools available pre-covid such as mock interviews and in-person workshops are no longer available. So, we created InterviewBuddy at StormHacks 2021. An online tool that provides feedback to the answers you give during the one-way interview.

This hack won 2nd place at StormHacks 2021. Check out our presentation here: https://youtu.be/YCDsf2Melog

Check out our GitHub for more information: https://github.com/siddg97/stormhacks2021
`;
