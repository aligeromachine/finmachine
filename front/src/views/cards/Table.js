import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getCardsTable } from "../../services/cards/state";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCardsTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.cardsReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
