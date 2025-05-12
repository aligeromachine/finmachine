import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { store } from "../store"; // Импортируем Redux store
import { setRowState, setRowPk } from "../row/state";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 100,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

const PREFIX_URL = "/shop/data/";

export const getShopTable = createAsyncThunk(
  "stateShop/getShopTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().shopReducer;
    const params = create_params("table_shop_data", offset, recordsDisplay);
    const response = await apiClient.post(PREFIX_URL, params);
    return response;
  },
);

export const addShopRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? "add_shop_data" : "edit_shop_data",
    pk,
    ...formData,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getShopTable());
  return response;
};

export const deleteShopRow = async (pk) => {
  const params = {
    command: "delete_shop_row",
    pk,
  };
  await apiClient.post(PREFIX_URL, params);
  await store.dispatch(getShopTable());
};

export const getShopRow = async (pk) => {
  const params = {
    command: "get_shop_row",
    pk,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};

export const stateShop = createSlice({
  name: "stateShop",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getShopTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getShopTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getShopTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const shopReducer = stateShop.reducer;
