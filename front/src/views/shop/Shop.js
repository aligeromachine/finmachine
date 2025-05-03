import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { BasicTable } from "../../components/table/BasicTable";
import { columnsShop } from "../../components/table/column/headers";
import { ShopModal } from "./modal/Canvas";
import { ShopFetcher } from "./DataFetcher";

const DataShop = () => {
  const draw = ShopFetcher();

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataShop</strong>
          </CCardHeader>
          <CCardBody>
            <ShopModal title={"Add Shop"} />
            <BasicTable data={draw} columns={columnsShop} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataShop;
