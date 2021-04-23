import { useState } from 'react';
import { useQuery, useQueries } from 'react-query';
import { setQuestions, getResult  } from '../api';

export const useSetQuestions = (questions) => {
  const {
    isLoading, isError, data, error,
  } = useQuery('questionIDs', () => setQuestions(questions));

  return { isLoading, isError, error, questionIDs: data && data['questions'] };
};

export const useGetResults = (pollURLs) => {
  const [results, setResults] = useState([]);
  const refetchInterval = 2 * 1000;

  const queries = useQueries(
    pollURLs.map((url, idx) => ({
      queryKey: ['results', url],
      queryFn: () => getResult(url),
      refetchInterval: results[idx] ? false : refetchInterval,
      onSuccess: (data) => {
        if (data.state !== 'PROGRESS') {
          results[idx] = data;
          setResults([...results]);
        }
      }
    })),
  );

  let isLoading = false;
  let isError = false;

  for (let i = 0; i < queries.length; i++) {
    if (queries[i].isLoading || (queries[i].isSuccess && queries[i].data.state === 'PROGRESS')) {
      isLoading = true;
      break;
    }

    if (queries[i].isError || (queries[i].isSuccess && queries[i].data.state === 'FAILURE')) {
      isError = true;
      break;
    }
  }

  return { isLoading, isError, results };
}
