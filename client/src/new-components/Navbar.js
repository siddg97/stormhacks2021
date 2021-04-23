import React from 'react';
import styled from 'styled-components';
import { ReactComponent as Logo } from '../svg/logoWithTitle.svg';
import { useHistory } from 'react-router-dom';
import { routes } from '../constants';

const Div = styled.div`
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background: rgba(60,100,177, 0.1)
`;

const StyledLogo = styled(Logo)`
  height: 100%;
  width: auto;
  padding: 0 10px;
  box-sizing: border-box;
`;

const List = styled.ul`
  list-style-type: none;
  display: flex;
  justify-content: center;
  align-items: center;
`;

const ListItem = styled.li`
  padding: 30px;
`;

const LeftDiv = styled.div`
  height: 100%;
`;

const Navbar = () => {
  const history = useHistory();

  const interview = () => {
    history.push(routes.SELECT_QUESTIONS);
  }

  return (
    <Div>
      <LeftDiv>
        <a href="/"><StyledLogo /></a>
      </LeftDiv>
      <List>
        <ListItem><a href="/">Home</a></ListItem>
        <ListItem><a href="/">About</a></ListItem>
        <ListItem><a href="/">Tips</a></ListItem>
        <ListItem><button onClick={interview}>Start Interview</button></ListItem>
      </List>
    </Div>
  );
}

export default Navbar;
