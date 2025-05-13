import { apiClient } from "../../utils/requests";
import { store } from "../store";
import { setRowState, setRowPk } from "../row/state";
import { getProfitTable } from "./state";
import {
  PROFIT_URL,
  PROFIT_ADD,
  PROFIT_EDIT,
  PROFIT_DEL,
  PROFIT_ROW,
} from "./const";

export const addProfitRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? PROFIT_ADD : PROFIT_EDIT,
    pk,
    ...formData,
  };
  console.log(params);
  const response = await apiClient.post(PROFIT_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getProfitTable());
  return response;
};

export const deleteProfitRow = async (pk) => {
  const params = {
    command: PROFIT_DEL,
    pk,
  };
  await apiClient.post(PROFIT_URL, params);
  await store.dispatch(getProfitTable());
};

export const getProfitRow = async (pk) => {
  const params = {
    command: PROFIT_ROW,
    pk,
  };
  const response = await apiClient.post(PROFIT_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};
