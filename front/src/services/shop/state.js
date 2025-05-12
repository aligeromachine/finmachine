import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { store } from "../store";
import { initialState } from "./model";
import { SHOP_URL, SHOP_TBL } from "./const";

export const getShopTable = createAsyncThunk(
  "stateShop/getShopTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().shopReducer;
    const params = create_params(SHOP_TBL, offset, recordsDisplay);
    const response = await apiClient.post(SHOP_URL, params);
    return response;
  },
);

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
