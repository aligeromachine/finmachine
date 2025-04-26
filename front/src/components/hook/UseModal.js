import { useState, useCallback } from "react";
import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
} from "@coreui/react";

export const UseModal = ({ title }) => {
  const [visible, setVisible] = useState(false);

  return (
    <>
      <CButton
        color="secondary"
        className="mb-3"
        onClick={() => setVisible(!visible)}
        style={{ width: "150px" }}
      >
        {title}
      </CButton>
      <CModal
        size="lg"
        visible={visible}
        onClose={() => setVisible(false)}
        aria-labelledby="LiveDemoExampleLabel"
      >
        <CModalHeader>
          <CModalTitle id="LiveDemoExampleLabel">Modal title</CModalTitle>
        </CModalHeader>
        <CModalBody>Woohoo, you're reading this text in a modal!</CModalBody>
        <CModalFooter>
          <CButton color="secondary" onClick={() => setVisible(false)}>
            Close
          </CButton>
          <CButton color="primary">Save changes</CButton>
        </CModalFooter>
      </CModal>
    </>
  );
};
