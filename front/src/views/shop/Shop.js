import React from "react";
import { CRow, CCol, CCard, CCardBody } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/view/Header";
import { Button } from "../../components/view/Button";
import { ShopModal } from "./modal/Base";
import { Table } from "./Table";

export const DataShop = () => {
  return (
    <ModalProvider>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <Header title={"DataShop"} />
            <CCardBody>
              <ShopModal />
              <Button title={"Add Shop"} />
              <Table />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </ModalProvider>
  );
};
