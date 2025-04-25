import React from "react";
import {
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CRow,
  CTab,
  CTabContent,
  CTabList,
  CTabPanel,
  CTabs,
} from "@coreui/react";
import { useEffect } from "react";
import BasicTable from "../../components/table/BasicTable";
import { useSelector, useDispatch } from "react-redux";
import { getBuysThunk } from "../../services/stateBuys";
import { create_params } from "../../utils/func";
import { columnsBuy } from "../../utils/headers";

const DataProducts = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const data = create_params("update_money_data", 0, 100);
    dispatch(getBuysThunk(data));
  }, [dispatch]);

  const { draw } = useSelector((store) => store.buysReducer);

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataProducts</strong>
          </CCardHeader>
          <CCardBody>
            <CTabs activeItemKey="product">
              <CTabList variant="tabs">
                <CTab itemKey="product">Product</CTab>
                <CTab itemKey="catalog">Catalog</CTab>
              </CTabList>
              <CTabContent>
                <CTabPanel className="p-3" itemKey="product">
                  <BasicTable data={draw} columns={columnsBuy} />
                </CTabPanel>
                <CTabPanel className="p-3" itemKey="catalog">
                  <div>TEST</div>
                </CTabPanel>
              </CTabContent>
            </CTabs>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataProducts;
