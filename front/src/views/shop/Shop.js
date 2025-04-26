import React from "react";
import {
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CRow,
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
} from "@coreui/react";
import { useEffect, useState } from "react";
import BasicTable from "../../components/table/BasicTable";
import { useSelector, useDispatch } from "react-redux";
import { getShopThunk } from "../../services/stateShop";
import { create_params } from "../../utils/func";
import { columnsShop } from "../../utils/headers";
import { UseModal } from "../../components/hook/UseModal";
const DataShop = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const data = create_params("update_shop_data", 0, 100);
    dispatch(getShopThunk(data));
  }, [dispatch]);

  const { draw } = useSelector((store) => store.shopReducer);

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataShop</strong>
          </CCardHeader>
          <CCardBody>
            <UseModal title={"Add Shop"} />
            <BasicTable data={draw} columns={columnsShop} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataShop;
