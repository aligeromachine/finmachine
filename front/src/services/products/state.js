import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { initialState } from "./model";
import { PREFIX_URL } from "./const";

export const getProductsThunk = createAsyncThunk(
  "stateProducts/getProductsThunk",
  async (data) => {
    const response = await apiClient.post(PREFIX_URL, data);
    return response;
  },
);

export const stateProducts = createSlice({
  name: "stateProducts",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getProductsThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getProductsThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getProductsThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const productsReducer = stateProducts.reducer;
