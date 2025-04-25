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
import { create_params } from "../../utils/func";
import { getProfitThunk } from "../../services/stateProfit";
import { getSourceThunk } from "../../services/stateSource";
import { columnsProfit, columnsSource } from "../../utils/headers";

const DataProfit = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const dataP = create_params("update_profit_data", 0, 100);
    dispatch(getProfitThunk(dataP));
    const dataS = create_params("update_source_data", 0, 100);
    dispatch(getSourceThunk(dataS));
  }, [dispatch]);

  const drawProfit = useSelector((store) => store.profitReducer.draw);
  const drawSource = useSelector((store) => store.sourceReducer.draw);

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataProfit</strong>
          </CCardHeader>
          <CCardBody>
            <CTabs activeItemKey="profit">
              <CTabList variant="tabs">
                <CTab itemKey="profit">Money Fit</CTab>
                <CTab itemKey="source">Source</CTab>
              </CTabList>
              <CTabContent>
                <CTabPanel className="p-3" itemKey="profit">
                  <BasicTable data={drawProfit} columns={columnsProfit} />
                </CTabPanel>
                <CTabPanel className="p-3" itemKey="source">
                  <BasicTable data={drawSource} columns={columnsSource} />
                </CTabPanel>
              </CTabContent>
            </CTabs>
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataProfit;
