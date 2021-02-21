const Question = ({ questionNumber, question }) => {
  return (
    <div>
      <h1>{`Q${questionNumber}: ${question}`}</h1>
    </div>
  );
};

export default Question;