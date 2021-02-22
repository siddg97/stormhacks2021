import { useState } from 'react';
import styled from 'styled-components';
import QuestionChoice from './QuestionChoice';
import { Button } from 'rsuite';
import { useHistory } from 'react-router';

const Container = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`;

const QuestionChoicePage = ({ setGen, setSoft, setTech }) => {
    const history = useHistory();
    const handleGeneralChecked = (event) => {
        setGen(event.target.checked);
    };

    const handleSoftSkillsChecked = (event) => {
        setSoft(event.target.checked);
    };

    const handleHardSkillsChecked = (event) => {
        setTech(event.target.checked);
    };

    const handleButtonClick = () => {
        console.log('practicing');
        history.push('/question/1');
    };

    return (
        <Container>
            <h1>Choose Your Questions</h1>
            <p>
                Only the cateogry of questions you select will be asked to you during the
                mock interview. A random question will be pulled from the customized pool.
            </p>
            <QuestionChoice
                title={'General Questions'}
                description={
                    'Inital screening questions and general knowledge about the company'
                }
                onChecked={handleGeneralChecked}
            />
            <QuestionChoice
                title={'Soft Skill Questions'}
                description={'Soft skill questions based off of your submission'}
                onChecked={handleSoftSkillsChecked}
            />
            <QuestionChoice
                title={'Hard Skill Questions'}
                description={'Hard skill questions based off of your submission'}
                onChecked={handleHardSkillsChecked}
            />
            <Button onClick={handleButtonClick}>Let's Practice!</Button>
        </Container>
    );
};

export default QuestionChoicePage;
