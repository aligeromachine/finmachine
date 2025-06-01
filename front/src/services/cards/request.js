import { setRowState, setRowPk } from "../row/state";
import { store } from "../store";
import { getCardsTable } from "./state";
import {
  CARDS_URL,
  CARDS_ADD,
  CARDS_EDIT,
  CARDS_DEL,
  CARDS_ROW,
} from "./const";
import { postCheck } from "../../utils/utilsCheck";

export const addCardsRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? CARDS_ADD : CARDS_EDIT,
    pk,
    ...formData,
  };
  const response = await postCheck(CARDS_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getCardsTable());
  return response;
};

export const deleteCardsRow = async (pk) => {
  const params = {
    command: CARDS_DEL,
    pk,
  };
  await postCheck(CARDS_URL, params);
  await store.dispatch(getCardsTable());
};

export const getCardsRow = async (pk) => {
  const params = {
    command: CARDS_ROW,
    pk,
  };
  const response = await postCheck(CARDS_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};
