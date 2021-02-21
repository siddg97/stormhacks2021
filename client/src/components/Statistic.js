import styled from 'styled-components';

const Container = styled.div`
  padding: 20px;
  width: 300px;
  text-align: center;
`;

const Statistic = ({ title, description, value }) => {
  return (
    <Container>
      <span>{value}</span>
      <h6>{title}</h6>
      <p>{description}</p>
    </Container>
  );
};

export default Statistic;