import styled from 'styled-components';

export const theme = Object.freeze({
  colors: {
    primary: '#3C64B1',
  },
  fonts: {
    primary: "'Mulish', sans-serif",
    secondary: "'Poppins', sans-serif",
  },
});

export const StyledButton = styled.button`
  background-color: ${props => props.theme.colors.primary};
  color: white;
  font-family: ${props => props.theme.fonts.primary};
  font-weight: bold;
  text-align: center;
  letter-spacing: 0.3px;
  border-radius: 3px;
  padding: 12px 30px;
  border: none;
`;
