import { postCheck } from "../../utils/utilsCheck";
import { setRowState, setRowPk } from "../row/state";
import { store } from "../store";
import { getSourceTable } from "./state";
import {
  SOURCE_URL,
  SOURCE_ADD,
  SOURCE_EDIT,
  SOURCE_DEL,
  SOURCE_ROW,
} from "./const";

export const addSourceRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? SOURCE_ADD : SOURCE_EDIT,
    pk,
    ...formData,
  };
  const response = await postCheck(SOURCE_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getSourceTable());
  return response;
};

export const deleteSourceRow = async (pk) => {
  const params = {
    command: SOURCE_DEL,
    pk,
  };
  await postCheck(SOURCE_URL, params);
  await store.dispatch(getSourceTable());
};

export const getSourceRow = async (pk) => {
  const params = {
    command: SOURCE_ROW,
    pk,
  };
  const response = await postCheck(SOURCE_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};
