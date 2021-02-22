import styled from 'styled-components';

const Container = styled.div`
    border: 1px solid black;
    width: 600px;
    margin: 10px;
`;

const TitleDiv = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    border-bottom: 1px solid black;
    padding: 10px;
`;

const QuestionsDiv = styled.div`
    padding: 10px;
`;

const QuestionsList = ({ title, description, questions, keyId }) => {
    return (
        <Container>
            <TitleDiv>
                <h5>{title}</h5>
                <p>{description}</p>
            </TitleDiv>
            <QuestionsDiv>
                <ul>
                    {questions.map((q, i) => (
                        <li key={`question-${keyId}=${i}`}>{q}</li>
                    ))}
                </ul>
            </QuestionsDiv>
        </Container>
    );
};

export default QuestionsList;
