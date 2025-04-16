import React from "react";
import { CCard, CCardBody, CCardHeader, CCol, CRow } from "@coreui/react";
import { useEffect } from "react";
import BasicTable from "../../components/table/BasicTable";
import { useSelector, useDispatch } from "react-redux";
import { getBuysThunk } from "../../services/dataBuys";

const columns = [
  {
    accessorKey: "name", // Accessor key for the "name" field from data object
    header: "Name", // Column header
    size: 100,
  },
  {
    accessorKey: "category",
    header: "Category",
  },
  {
    accessorKey: "price",
    header: "Price",
    cell: (info) => `$${info.getValue().toFixed(2)}`, // Format price as currency
  },
  {
    accessorKey: "inStock",
    header: "In Stock",
  },
];

const DataShop = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getBuysThunk());
  }, [dispatch]);

  const { buys } = useSelector((store) => store.dataBuys);

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>DataShop</strong>
          </CCardHeader>
          <CCardBody>
            <BasicTable data={buys} columns={columns} />
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  );
};

export default DataShop;
