import React from 'react';
import styled from 'styled-components';
import { ReactComponent as Logo } from '../logoWithTitle.svg';

const Div = styled.div`
  height: 50px;
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
`;

const ListItem = styled.li`
  padding: 30px;
`;

const Navbar = () => (
  <Div>
    <StyledLogo />
    <List>
      <ListItem><a href="/">Home</a></ListItem>
    </List>
  </Div>
);

export default Navbar;
