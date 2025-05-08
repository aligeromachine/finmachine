import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsShop } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getShopTable } from "../../services/stateShop";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getShopTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.shopReducer);

  const columns = columnsShop(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
