import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/HeaderSource";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getSourceTable } from "../../services/source/state";

export const TableSource = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getSourceTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.sourceReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
