import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";
import { create_params } from "../utils/func";
import { store } from "./store"; // Импортируем Redux store

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 100,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

export const getShopThunk = createAsyncThunk(
  "stateShop/getShopThunk",
  async (_, { getState }) => {
    const { offset, recordsDisplay } = getState().shopReducer;
    const params = create_params("update_shop_data", offset, recordsDisplay);
    const response = await apiClient.post("/shop/table/", params);
    return response;
  },
);

export const addShopThunk = async (data) => {
  const params = {
    command: "add_shop_data",
    ...data,
  };
  const response = await apiClient.post("/shop/table/", params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getShopThunk());
  return response;
};

export const stateShop = createSlice({
  name: "stateShop",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getShopThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getShopThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getShopThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const shopReducer = stateShop.reducer;
