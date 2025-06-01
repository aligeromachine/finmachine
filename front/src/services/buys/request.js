import { store } from "../store";
import { setRowState, setRowPk } from "../row/state";
import { getBuysTable } from "./state";
import { BUY_URL, BUY_ADD, BUY_EDIT, BUY_DEL, BUY_ROW } from "./const";
import { postCheck } from "../../utils/utilsCheck";

export const addBuyRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? BUY_ADD : BUY_EDIT,
    pk,
    ...formData,
  };
  const response = await postCheck(BUY_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getBuysTable());
  return response;
};

export const deleteBuyRow = async (pk) => {
  const params = {
    command: BUY_DEL,
    pk,
  };
  await postCheck(BUY_URL, params);
  await store.dispatch(getBuysTable());
};

export const getBuyRow = async (pk) => {
  const params = {
    command: BUY_ROW,
    pk,
  };
  const response = await postCheck(BUY_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};
