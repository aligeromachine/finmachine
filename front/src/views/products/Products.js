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
import { getProductsThunk } from "../../services/stateProducts";
import { getCatalogThunk } from "../../services/stateCatalog";
import { columnsProducts, columnsCatalog } from "../../utils/headers";

const DataProducts = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    const dataP = create_params("update_products_data", 0, 100);
    dispatch(getProductsThunk(dataP));
    const dataS = create_params("update_catalog_data", 0, 100);
    dispatch(getCatalogThunk(dataS));
  }, [dispatch]);

  const drawProd = useSelector((store) => store.productsReducer.draw);
  const drawCat = useSelector((store) => store.catalogReducer.draw);

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
                  <BasicTable data={drawProd} columns={columnsProducts} />
                </CTabPanel>
                <CTabPanel className="p-3" itemKey="catalog">
                  <BasicTable data={drawCat} columns={columnsCatalog} />
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
