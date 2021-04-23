import { useHistory, useLocation } from 'react-router-dom';
import styled from 'styled-components';
import { routes } from '../constants';
import { useGetResults } from '../hooks'

const ResultsPage = () => {
  const history = useHistory();
  const { pollURLs } = useLocation().state;

  const handleClick = () => {
    history.push(routes.SELECT_QUESTIONS);
  };

  const { isLoading, isError, results } = useGetResults(pollURLs);
  console.log('results: ', results);
  if (isLoading) return <span>Loading...</span>
  if (isError)   return <span>Error</span>

  return (
    <div>
      <h1>Results</h1>
      {results.map((res, idx) => (
        <>
          <h1>Result for question ${idx + 1}</h1>
          <div>
            {JSON.stringify(res)}
          </div>
        </>
      ))}
      <button onClick={handleClick} type="button">New Interview</button>
    </div>
  );
};

export default ResultsPage;
