import React from 'react';
import { Navbar as Navbar_, Nav, Icon } from 'rsuite';
import styled from 'styled-components';

const Logo = styled.a`
  padding: 18px 20px;
  display: inline-block;
`;

const Navbar = () => {
  return (
    <Navbar_>
      <Navbar_.Header>
        <Logo href="#">LOGO</Logo>
      </Navbar_.Header>
      <Navbar_.Body>
        <Nav>
          <Nav.Item icon={<Icon icon="home" />}>Home</Nav.Item>
          <Nav.Item>About</Nav.Item>
        </Nav>
      </Navbar_.Body>
    </Navbar_>
  );
};

export default Navbar;