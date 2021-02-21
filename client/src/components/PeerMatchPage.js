import styled from 'styled-components';
import PeerMatchForm from './PeerMatchForm';

const PeerMatchPage = () => {
  return (
    <div>
      <h1>Peer Interview</h1>
      <p>Get matched up with a </p>
      <p>Share more information about what kind of job are you applying for and get paired with another peer! Don’t forget to specify what kind of interview questions you want to be asked. </p>
      <p>Once you are both paired up, schedule a time to meet up and use the unique url sent to you to join a LOGO interview room. Further instructions will be provided. </p>

      <PeerMatchForm />
    </div>
  )
}

export default PeerMatchPage;


