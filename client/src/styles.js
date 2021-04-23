import { createGlobalStyle } from 'styled-components';

export default createGlobalStyle`
  html, body, #root, .App {
    height: 100%;
    margin: 0;
  }

  .App {
    display: flex;
    flex-direction: column;
  }

  html {
    --color-primary: #3C64B1;
    --color-text: #474747;
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

    &:hover {
      text-decoration: underline;
    }
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

    &:disabled {
      background-color: grey;

      &:hover {
        opacity: 1;
        transition: none
      }
    }
  }

  input {
    font-family: var(--font-text);
  }
`;
