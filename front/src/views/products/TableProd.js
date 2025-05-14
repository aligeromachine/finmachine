import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/HeaderProd";
import { getProdTable } from "../../services/products/state";

export const TableProd = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getProdTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.productsReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
