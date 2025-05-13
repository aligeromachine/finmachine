import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { store } from "../store";
import { initialState } from "./model";
import { PROFIT_URL, PROFIT_TBL } from "./const";

export const getProfitTable = createAsyncThunk(
  "stateProfit/getProfitTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().profitReducer;
    const params = create_params(PROFIT_TBL, offset, recordsDisplay);
    const response = await apiClient.post(PROFIT_URL, params);
    return response;
  },
);

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
