import { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Input, Button } from 'rsuite';
import styled from 'styled-components';
import { useGetQuestions } from '../hooks';

const Div = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
`;

const Text = styled.p`
    margin: 40px;
`;

const StyledInput = styled(Input)`
    margin: 20px auto;
    max-width: 800px;
`;

const ScanJobPage = ({ setUid, setSq, setTq }) => {
    const history = useHistory();
    const [description, setDescription] = useState('');

    const options = {
        onSuccess: (data) => {
            const { soft, tech, uid } = data;
            setUid(uid);
            setSq(soft);
            setTq(tech);
            history.push('/questions');
        },
        onError: (err) => {
            console.log(err);
        },
    };

    const { refetch, status } = useGetQuestions({ description, options });

    const scan = () => {
        if (description !== '') {
            refetch();
            console.log({ description: JSON.stringify(description) });
        }
    };

    const handleInputChange = (text) => {
        setDescription(text);
    };

    return (
        <Div>
            <h1>Let's Get Started</h1>
            <Text>
                Copy and paste a job description below. Our AI will scan through the text
                and generate relevant questions for you.
            </Text>
            <StyledInput
                onChange={handleInputChange}
                componentClass='textarea'
                rows={20}
                placeholder='Paste job description here'
            />
            <Button onClick={scan}>Scan</Button>
        </Div>
    );
};

export default ScanJobPage;
