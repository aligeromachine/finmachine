import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 0,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

export const getCatalogThunk = createAsyncThunk(
  "stateCatalog/getCatalogThunk",
  async (data) => {
    const response = await apiClient.post("/catalog/table/", data);
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
