import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";
import { create_params } from "../utils/func";

const initialState = {
  command: "update_shop_data",
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 100,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

export const getShopThunk = createAsyncThunk(
  "stateShop/getShopThunk",
  async (_, { getState }) => {
    const { command, offset, recordsDisplay } = getState().shopReducer;
    const params = create_params(command, offset, recordsDisplay);
    const response = await apiClient.post("/shop/table/", params);
    return response;
  },
);

export const addShopThunk = createAsyncThunk(
  "stateShop/addShopThunk",
  async (data, { dispatch }) => {
    const response = await apiClient.post("/shop/add/", data);
    if (!response.data) return Promise.reject(response.message);
    await dispatch(getShopThunk());
  },
);
export const stateShop = createSlice({
  name: "stateShop",
  initialState: initialState,
  reducers: {
    setParams: (state) => {
      state.loading = "empty";
      state.register = false;
      state.error = "";
    },
  },
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
