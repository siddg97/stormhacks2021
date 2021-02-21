import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Input, Button } from 'rsuite';
import styled from 'styled-components';
import QuestionsList from './QuestionsList';
import InterviewTypeModal from './InterviewTypeModal';
import EmailForm from './EmailForm';

const Div = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const Text = styled.p`
  margin-top: 40px;
`;

const List = styled.ol`
  display: flex;
  padding-inline-start: 0px;
`;

const ListItem = styled.li`
  margin: 10px;
  max-width: 300px;
`;

const QuestionsContainer = styled.div`
  margin: 20px;
`;

const generalQuestions = [
  'Tell me about yourself.',
  'What do you know about our company?',
  'What do you understand about the role?',
  'Why are you interested in working at our company?',
  'What motivates you in a job?',
];

const softSkillQuestions = [
  'Tell me about yourself.',
  'What do you know about our company?',
  'What do you understand about the role?',
  'Why are you interested in working at our company?',
  'What motivates you in a job?',
];

const technicalQuestions = [
  'Tell me about yourself.',
  'What do you know about our company?',
  'What do you understand about the role?',
  'Why are you interested in working at our company?',
  'What motivates you in a job?',
];

const QuestionsPage = () => {
  const [isModalOpen, setisModalOpen] = useState(false);

  const openModal = () => {
    setisModalOpen(true);
  };

  const closeModal = () => {
    setisModalOpen(false);
  }

  return (
    <Div>
      <h1>Your Personalized Interview Questions</h1>
      <Text>Our AI created interview questions based off of your submission. Questions are grouped into three categories:</Text>
      <ol>
        <li>General</li>
        <li>Soft Skills</li>
        <li>Technical Skills</li>
      </ol>

      <QuestionsContainer>
        <QuestionsList
          title={'General Questions'}
          description={'Inital screening questions and general knowledge about the company'}
          questions={generalQuestions}
        />

        <QuestionsList
          title={'Soft Skill Questions'}
          description={'Soft skill questions based off of your submission'}
          questions={softSkillQuestions}
        />

        <QuestionsList
          title={'Technical Skill Questions'}
          description={'Technical skill questions based off of your submission'}
          questions={technicalQuestions}
        />
      </QuestionsContainer>

      <EmailForm />

      <h1>How To Practice With LOGO</h1>
      <List>
        <ListItem>
          <h5>Pair Up</h5>
          <p>Tell us what you want to practice and we will select random questions accordingly. You can choose to get paired with another peer, or conduct a one-way interview.</p>
        </ListItem>
        <ListItem>
          <h5>Practice</h5>
          <p>Answer the questions when prompted, follow the tips to ace it! After the interview get feedback using AI and from your peer. Swap roles if you are paired up after you’re done. </p>
        </ListItem>
        <ListItem>
          <h5>Review</h5>
          <p>Learn from peers’ feedback and from insights generated by AI. Keep practicing until you become an interview rock star.</p>
        </ListItem>
      </List>

      <Button onClick={openModal}>Let's Practice!</Button>

      <InterviewTypeModal
        isOpen={isModalOpen}
        close={closeModal}
      />
    </Div>
  );
};

export default QuestionsPage;


