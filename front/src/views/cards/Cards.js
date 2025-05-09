import React from "react";
import { CCard, CCardBody, CCol, CRow } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/view/Header";
import { Button } from "../../components/view/Button";
import { Table } from "./Table";

export const DataCards = () => {
  return (
    <ModalProvider>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <Header title={"DataCards"} />
            <CCardBody>
              <Button title={"Add Card"} />
              <Table />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </ModalProvider>
  );
};
