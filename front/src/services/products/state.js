import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { store } from "../store";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { initialState } from "./model";
import { PROD_URL, PROD_TBL } from "./const";

export const getProdTable = createAsyncThunk(
  "stateProducts/getProdTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().productsReducer;
    const params = create_params(PROD_TBL, offset, recordsDisplay);
    const response = await apiClient.post(PROD_URL, params);
    return response;
  },
);

export const stateProducts = createSlice({
  name: "stateProducts",
  initialState: initialState,
  reducers: {
    setOffset: (state, action) => {
      state.offset = action.payload.offset;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getProdTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getProdTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getProdTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const { setOffset } = stateProducts.actions;
export const productsReducer = stateProducts.reducer;
