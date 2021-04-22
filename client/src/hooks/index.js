import { useQuery } from 'react-query';
import { setQuestions } from '../api';

export const useSetQuestions = (questions) => {
    const {
        isLoading, isError, data, error,
    } = useQuery('questionIDs', () => setQuestions(questions));

    return { isLoading, isError, error, questionIDs: data && data['questions'] };
};
