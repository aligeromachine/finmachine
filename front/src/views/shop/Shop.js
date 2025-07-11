import React from "react";
import { CRow, CCol, CCard, CCardBody } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/elems/Header";
import { Button } from "../../components/elems/Button";
import { ShopModal } from "./modal/Base";
import { Table } from "./Table";
import { Auth } from "../../components/auth/Auth";

export const DataShop = () => {
  return (
    <Auth>
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
    </Auth>
  );
};
