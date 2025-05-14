import React, { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { getCatTable } from "../../services/catalog/state";
import { columnsTbl } from "./column/HeaderCat";

export const TableCat = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCatTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.catalogReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
