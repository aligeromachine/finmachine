import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getBuysTable } from "../../services/buys/state";

export const TableBuy = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getBuysTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.buysReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
