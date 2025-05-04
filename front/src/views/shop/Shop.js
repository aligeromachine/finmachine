import React from "react";
import { CRow, CCol, CCard, CCardBody } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "./Header";
import { Button } from "./Button";
import { ShopModal } from "./modal/Canvas";
import { ModalStaticBackdropExample } from "./modal/EditShop";
import { Table } from "./Table";

const DataShop = () => {
  return (
    <ModalProvider>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <Header title={"DataShop"} />
            <CCardBody>
              <Button title={"Add Shop"} />
              <ShopModal />
              <ModalStaticBackdropExample />
              <Table />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </ModalProvider>
  );
};

export default DataShop;
