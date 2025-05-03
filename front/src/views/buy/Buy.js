import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { useEffect } from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { columnsBuy } from "../../components/table/column/headers";
import { useSelector, useDispatch } from "react-redux";
import { getBuysThunk } from "../../services/stateBuys";
import { create_params } from "../../utils/func";

const DataTransactions = () => {
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
            <strong>DataTransactions</strong>
          </CCardHeader>
          <CCardBody>
            <BasicTable data={draw} columns={columnsBuy} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataTransactions;
