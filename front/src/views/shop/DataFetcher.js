import { useEffect, useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { getShopThunk } from "../../services/stateShop";

export const ShopFetcher = () => {
  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(getShopThunk());
  }, [dispatch]);

  const { draw } = useSelector((store) => store.shopReducer);
  return draw;
};
