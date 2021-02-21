import styled from 'styled-components';
import { Modal } from 'rsuite';
import SelectInterviewType from './SelectInterviewType';

const InterviewTypeModal = ({ isOpen, close }) => {
  return (
    <Modal show={isOpen} onHide={close}>
      <Modal.Header>
        <Modal.Title>Select Interview Type</Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <SelectInterviewType />
      </Modal.Body>
    </Modal>
  );
};

export default InterviewTypeModal;