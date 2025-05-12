import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 0,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

const PREFIX_URL = "/buy/data/";

export const getBuysThunk = createAsyncThunk(
  "stateBuys/getBuysThunk",
  async (data) => {
    const response = await apiClient.post(PREFIX_URL, data);
    return response;
  },
);

export const stateBuys = createSlice({
  name: "stateBuys",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getBuysThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getBuysThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getBuysThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const buysReducer = stateBuys.reducer;
