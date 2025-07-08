import React from "react";
import { CCard, CCardBody, CCol, CRow } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/elems/Header";
import { Button } from "../../components/elems/Button";
import { Table } from "./Table";
import { CardsModal } from "./modal/Base";
import { Auth } from "../../components/auth/Auth";

export const DataCards = () => {
  return (
    <Auth>
      <ModalProvider>
        <CRow>
          <CCol xs={12}>
            <CCard className="mb-4">
              <Header title={"DataCards"} />
              <CCardBody>
                <CardsModal />
                <Button title={"Add Card"} />
                <Table />
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
      </ModalProvider>
    </Auth>
  );
};
