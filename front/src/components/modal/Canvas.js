import { useState, useCallback } from "react";
import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
  CRow,
  CCol,
  CFormInput,
} from "@coreui/react";
import { UseModal } from "../hook/UseModal";
import { LayoutGutters2Example } from "./Content";
import { InputGroupSizingExample } from "./Content2";

export const ShopModalTest = ({ title }) => {
  const { visible, refreshModal, closeModal } = UseModal();

  return (
    <>
      <CButton
        color="secondary"
        className="mb-3"
        onClick={refreshModal}
        style={{ width: "150px" }}
      >
        {title}
      </CButton>
      <CModal size="lg" visible={visible} onClose={closeModal}>
        <CModalHeader>
          <CModalTitle id="LiveDemoExampleLabel">Modal title</CModalTitle>
        </CModalHeader>
        <CModalBody>
          <InputGroupSizingExample />
          <LayoutGutters2Example />
        </CModalBody>
        <CModalFooter>
          <CButton color="secondary" onClick={closeModal}>
            Close
          </CButton>
          <CButton color="primary">Save changes</CButton>
        </CModalFooter>
      </CModal>
    </>
  );
};
