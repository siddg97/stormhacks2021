import { useHistory } from 'react-router-dom';
import styled from 'styled-components';
import { routes } from '../constants';

const ResultsPage = () => {
  const history = useHistory();

  const handleClick = () => {
    history.push(routes.SELECT_QUESTIONS);
  };

  return (
    <div>
      <h1>Results</h1>
      <div>Display results here lol</div>
      <button onClick={handleClick} type="button">New Interview</button>
    </div>
  );
};

export default ResultsPage;
