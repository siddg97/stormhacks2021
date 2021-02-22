<p align="left">
  <img src="./img/logo.png" alt="InterviewBuddy.online" height="250" />
</p>
<p>Created by: Brandon Situ, Siddharth Gupta, Shirley Vong, and Jake Pauls</p>
<p> ⚡ Stormhacks 2021 ⚡ </p>
<p> 🥈 2nd Place Overall  </p>

---

## Inspiration

Job seekers may have less opportunities to conduct mock interviews with each other. InterviewBuddy.space seeks to solve this problem by providing a mock interview AI and peer interview system.

## What does it do?

Users can upload job descriptions that are parsed for keywords. After, those keywords become template interview questions that they can either answer to an AI or ask to another peer over the internet.

Once the interview is conducted (either with an AI, or via peer connection) the results for their recorded interview are transcribed and their performance (enunciation of words, filler words, and wpm).

## How did you guys build this?

Our prototype is built using a Flask app to communicate with a GCP storage bucket. In the Flask app, recordings are sent to the GCP's Speech-To-Text API and are transcribed. After, the text is evaluated and interviewees get feedback based on their mock interview performance. The frontend of this application leverages React.

## What were some challenges? 

With our idea, we frequently overshot and tried to complete too many features. Early on, we knew that some of our features/concerns would be simply on implementing everything on time. As such, time management was a huge concern.

Technically, we had problems getting the Peer-to-Peer connection to work for video. In particular, we tried to implement WebRTC in React, which was fairly time consuming and required a lot of pre-requisite knowledge that later become unattainable. As well, our deployment to the App Engine ran into multiple issues that we struggled to overcome. 

## What's next for InterviewBuddy.space?

As far as further developing and manifesting our prototype, the sky is the limit. In the future, we would seek to incorporate real-time synchronous video between the interviewee and the interviewer (as originally planned).

As well, we're hoping to incorporate some sort of web scraping service in the future, to provision company specific culture questions. With this implemented, we can better prepare prospective interviewers for each other on the platform.

Finally, during development, we were researching eye tracking libraries, such as PyGaze. With this library, our goal would be to build our a feature that tracks eye contact during the interview. This metric could be captured and displayed to the interviewee on the results page once their interview is over.
