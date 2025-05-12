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

const PREFIX_URL = "/profit/data/";

export const getProfitTable = createAsyncThunk(
  "stateProfit/getProfitTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().profitReducer;
    const params = create_params("table_profit_data", offset, recordsDisplay);
    const response = await apiClient.post(PREFIX_URL, params);
    return response;
  },
);

export const addProfitRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? "add_profit_data" : "edit_profit_data",
    pk,
    ...formData,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getProfitTable());
  return response;
};

export const deleteProfitRow = async (pk) => {
  const params = {
    command: "delete_profit_row",
    pk,
  };
  await apiClient.post(PREFIX_URL, params);
  await store.dispatch(getProfitTable());
};

export const getProfitRow = async (pk) => {
  const params = {
    command: "get_profit_row",
    pk,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};

export const stateProfit = createSlice({
  name: "stateProfit",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getProfitTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getProfitTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getProfitTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const profitReducer = stateProfit.reducer;
