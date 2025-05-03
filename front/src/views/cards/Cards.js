import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { useEffect } from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { columnsCards } from "../../components/table/column/headers";
import { useSelector, useDispatch } from "react-redux";
import { getCardsThunk } from "../../services/stateCards";
import { create_params } from "../../utils/func";

const DataCards = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const data = create_params("update_cards_data", 0, 100);
    dispatch(getCardsThunk(data));
  }, [dispatch]);

  const { draw } = useSelector((store) => store.cardsReducer);

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataCards</strong>
          </CCardHeader>
          <CCardBody>
            <BasicTable data={draw} columns={columnsCards} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataCards;
