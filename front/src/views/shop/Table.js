import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { useModal } from "../../components/hook/ModalContext";
import { columnsShop } from "./column/Header";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getShopThunk } from "../../services/stateShop";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getShopThunk());
  }, [dispatch]);

  const { openModal } = useModal();

  const columns = columnsShop(openModal);
  const { draw } = useSelector((store) => store.shopReducer);
  return <BasicTable data={draw} columns={columns} />;
};
