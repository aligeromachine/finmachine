import { apiClient } from "../../utils/requests";
import { store } from "../store";
import { setRowState, setRowPk } from "../row/state";
import { getProdTable } from "./state";
import { PROD_URL, PROD_ADD, PROD_EDIT, PROD_DEL, PROD_ROW } from "./const";

export const addProdRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? PROD_ADD : PROD_EDIT,
    pk,
    ...formData,
  };
  const response = await apiClient.post(PROD_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getProdTable());
  return response;
};

export const deleteProdRow = async (pk) => {
  const params = {
    command: PROD_DEL,
    pk,
  };
  await apiClient.post(PROD_URL, params);
  await store.dispatch(getProdTable());
};

export const getProdRow = async (pk) => {
  const params = {
    command: PROD_ROW,
    pk,
  };
  const response = await apiClient.post(PROD_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};
