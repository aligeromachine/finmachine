import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsTbl } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getShopTable } from "../../services/shop/state";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getShopTable());
  }, [dispatch]);

  const { openModal } = useModal();
  const { draw } = useSelector((store) => store.shopReducer);

  const columns = columnsTbl(openModal);
  return <BasicTable data={draw} columns={columns} />;
};
