import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { useEffect } from "react";
import BasicTable from "../../components/table/BasicTable";
import { useSelector, useDispatch } from "react-redux";
import { getShopThunk } from "../../services/stateShop";
import { create_params } from "../../utils/func";
import { columnsShop } from "../../utils/headers";

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
            <BasicTable data={draw} columns={columnsShop} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataShop;
