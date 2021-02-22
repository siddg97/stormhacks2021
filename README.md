# stormhacks2021

**Inspiration:**
Job seekers may have less and less opportunities to conduct mock interviews.

InterviewBuddy.space seeks to solve this problem by providing a mock interview AI and peer interview system.

**What does it do?**
Users can upload job descriptions that are parsed for keywords.

After, those keywords become template interview questions that they can either answer to an AI or ask to another peer over the internet.

Once the interview is conducted (either with an AI, or via peer connection) the results for their recorded interview are transcribed and their performance (enunciation of words, filler words, and wpm).

**How did you guys build this?**
Our prototype is built using a Flask app to communicate with a GCP storage bucket.
In the Flask app, recordings are sent to the GCP's Speech-to-Text API and are transcribed.
After, the text is evaluated and interviewees get feedback based on their mock interview performance.
The frontend of this application leverages React.

**What's next for InterviewBuddy.Online?**
As far as further developing our prototype, the sky is the limit.

In the future, we would seek to incorporate real-time synchronous video between the interviewee and interviewer.

As well, we're hoping to incorporate some sort of web scraping service to provision company specific culture questions to better prepare prospective interviewers on the platform.

Finally, during development, we were researching eye tracking libraries, such as PyGaze. With this library, our goal would be to build out a feature that tracks eye contact during an interview. This metric could also be displayed to the interviewee on the results page once their interview is over.
