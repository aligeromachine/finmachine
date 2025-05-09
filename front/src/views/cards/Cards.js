import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { useEffect } from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { columnsCards } from "../../components/table/column/headers";
import { useSelector, useDispatch } from "react-redux";
import { getCardsThunk } from "../../services/stateCards";
import { create_params } from "../../utils/func";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/view/Header";
import { Button } from "../../components/view/Button";

export const DataCards = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const data = create_params("update_cards_data", 0, 100);
    dispatch(getCardsThunk(data));
  }, [dispatch]);

  const { draw } = useSelector((store) => store.cardsReducer);

  return (
    <ModalProvider>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <Header title={"DataCards"} />
            <CCardBody>
              <Button title={"Add Card"} />
              <BasicTable data={draw} columns={columnsCards} />
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </ModalProvider>
  );
};
