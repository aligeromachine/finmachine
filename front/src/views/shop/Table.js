import React from "react";
import { BasicTable } from "../../components/table/BasicTable";
import { columnsShop } from "../../components/table/column/headers";
import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getShopThunk } from "../../services/stateShop";

export const Table = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getShopThunk());
  }, [dispatch]);

  const { draw } = useSelector((store) => store.shopReducer);
  return <BasicTable data={draw} columns={columnsShop} />;
};
