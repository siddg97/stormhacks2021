import { ABOUT_TEXT } from '../constants';
import styled from 'styled-components';

const Image = styled.img`
  width: 180px;
  height: 180px;
  object-fit: cover;
`;

const ContributorDiv = styled.div`
  display: flex;
  flex-direction: column;
  text-align: center;
  padding: 10px;
`;

const ContribListDiv = styled.div`
  display: flex;
  justify-content: center;
  padding: 20px;
`;

const Header = styled.h1`
  text-align: center;
`;

const Name = styled.span`
  font-weight: bold;
`;

const School = styled.span`
  font-size: 0.9rem;
`;

const Link = styled.a`
  font-size: 0.9rem;
`;

const Text = styled.p`
  padding: 10px;
`;

const About = () => {
  const contributors = [
    {
      image: 'https://pbs.twimg.com/profile_images/1092451626781163523/0YzJMi-8.jpg',
      name: 'Brandon Situ',
      role: 'UI/UX, PM',
      school: 'SFU Business',
      linkedin: 'linkedin.com/in/brandonsitu',
    }, {
      image: 'https://smartcdn.prod.postmedia.digital/windsorstar/wp-content/uploads/2015/02/cookiemonster.jpg',
      name: 'Jacob Pauls',
      role: 'Full Stack',
      school: 'BCIT Computing',
      linkedin: 'linkedin.com/in/jacobpauls',
    }, {
      image: 'https://variety.com/wp-content/uploads/2020/05/not-too-late-show-with-elmo.jpg',
      name: 'Siddharth Gupta',
      role: 'Back End',
      school: 'SFU Computer Science',
      linkedin: 'linkedin.com/in/siddg97',
    }, {
      image: 'https://ichef.bbci.co.uk/images/ic/640x360/p01wf46x.jpg',
      name: 'Shirley Vong',
      role: 'Front End',
      school: 'SFU Software Systems',
      linkedin: 'linkedin.com/in/shirley-vong',
    },
  ];

  return (
    <div>
      <Header>About Us</Header>
      <Text>{ABOUT_TEXT}</Text>
      <ContribListDiv>
        {contributors.map((c) => (
          <ContributorDiv>
            <Image src={c.image} alt={c.name} />
            <Name>{c.name}</Name>
            <School>{c.role}</School>
            <School>{c.school}</School>
            <Link href={c.linkedin}>{c.linkedin}</Link>
          </ContributorDiv>
        ))}
      </ContribListDiv>
    </div>
  );
};

export default About;
