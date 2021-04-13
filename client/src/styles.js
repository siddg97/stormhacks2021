import { createGlobalStyle } from 'styled-components';

export default createGlobalStyle`
  html {
    --color-primary: #3C64B1;
    --color-text: #737B7D;
    --color-heading: #373F41;

    --font-text: 'Mulish', sans-serif;
    --font-header: 'Poppins', san-serif;
  }

  body {
    font-family: var(--font-text)
  }

  p {
    white-space: break-spaces;
    color: var(--color-text);
  }

  h1 {
    color: var(--color-heading);
  }

  a {
    text-decoration: none;
    font-weight: bold;
    color: var(--color-primary);
  }

  a:hover {
    text-decoration: underline;
  }

  button {
    background-color: var(--color-primary);
    color: white;
    font-family: var(--font-text);
    font-weight: bold;
    text-align: center;
    letter-spacing: 0.3px;
    border-radius: 3px;
    padding: 12px 30px;
    border: none;

    &:hover {
    opacity: 0.85;
    transition: opacity 0.1s linear;
  }
`;
