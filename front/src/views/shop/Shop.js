import React from "react";
import { CRow, CCol, CCard, CCardBody } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "./Header";
import { Button } from "./Button";
import { ShopModal } from "./modal/ShopModal";
import { Table } from "./Table";

const DataShop = () => {
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

export default DataShop;
