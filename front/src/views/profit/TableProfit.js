import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/HeaderProfit";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getProfitTable } from "../../services/stateProfit";

export const TableProfit = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getProfitTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.profitReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
