import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsShop } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getCardsTable } from "../../services/stateCards";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getCardsTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.cardsReducer);

  const columns = columnsShop(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
