import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 0,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

export const getSourceThunk = createAsyncThunk(
  "stateSource/getSourceThunk",
  async (data) => {
    const response = await apiClient.post("/source/table/", data);
    return response;
  },
);

export const stateSource = createSlice({
  name: "stateSource",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getSourceThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getSourceThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getSourceThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const sourceReducer = stateSource.reducer;
