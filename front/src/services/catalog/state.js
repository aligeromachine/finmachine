import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { PREFIX_URL } from "./const";
import { initialState } from "./model";

export const getCatalogThunk = createAsyncThunk(
  "stateCatalog/getCatalogThunk",
  async (data) => {
    const response = await apiClient.post(PREFIX_URL, data);
    return response;
  },
);

export const stateCatalog = createSlice({
  name: "stateCatalog",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getCatalogThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getCatalogThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getCatalogThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const catalogReducer = stateCatalog.reducer;
