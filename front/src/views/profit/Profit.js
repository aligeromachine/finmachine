import React from "react";
import {
  CRow,
  CCol,
  CCard,
  CCardBody,
  CTab,
  CTabs,
  CTabContent,
  CTabList,
  CTabPanel,
} from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/view/Header";
import { Button } from "../../components/view/Button";
import { TableProfit } from "./TableProfit";
import { TableSource } from "./TableSource";
import { SourceModal } from "./modal/source/Base";
import { ProfitModal } from "./modal/profit/Base";

export const DataProfit = () => {
  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <Header title={"DataProfit"} />
          <CCardBody>
            <CTabs activeItemKey="profit">
              <CTabList variant="tabs">
                <CTab itemKey="profit">Money Fit</CTab>
                <CTab itemKey="source">Source</CTab>
              </CTabList>
              <CTabContent>
                <CTabPanel className="p-3" itemKey="profit">
                  <ModalProvider>
                    <ProfitModal />
                    <Button title={"Add Profit"} />
                    <TableProfit />
                  </ModalProvider>
                </CTabPanel>
                <CTabPanel className="p-3" itemKey="source">
                  <ModalProvider>
                    <SourceModal />
                    <Button title={"Add Source"} />
                    <TableSource />
                  </ModalProvider>
                </CTabPanel>
              </CTabContent>
            </CTabs>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};
