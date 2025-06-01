import { CCard, CCardBody, CCol, CRow } from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/view/Header";
import { Button } from "../../components/view/Button";
import { TableBuy } from "./Table";
import { BuysModal } from "./modal/Base";
import { Auth } from "../../components/auth/Auth";

export const DataTransactions = () => {
  return (
    <Auth>
      <ModalProvider>
        <CRow>
          <CCol xs={12}>
            <CCard className="mb-4">
              <Header title={"DataTransactions"} />
              <CCardBody>
                <BuysModal />
                <Button title={"Add Buy"} />
                <TableBuy />
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
      </ModalProvider>
    </Auth>
  );
};
