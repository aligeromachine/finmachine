import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";

const initialState = {
  buys: [],
  loading: "loading" | "idle" | "failed",
};

export const getBuysThunk = createAsyncThunk(
  "dataBuys/getBuysThunk",
  async () => {
    const data = await apiClient.get("/v1/task/");
    return data;
  },
);

export const dataBuys = createSlice({
  name: "dataBuys",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getBuysThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getBuysThunk.fulfilled, (state, action) => {
        state.buys = action.payload;
        state.loading = "idle";
      })
      .addCase(getBuysThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export default dataBuys.reducer;
