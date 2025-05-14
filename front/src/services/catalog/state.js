import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { store } from "../store";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { initialState } from "./model";
import { CAT_URL, CAT_TBL } from "./const";

export const getCatTable = createAsyncThunk(
  "stateCatalog/getCatTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().catalogReducer;
    const params = create_params(CAT_TBL, offset, recordsDisplay);
    const response = await apiClient.post(CAT_URL, params);
    return response;
  },
);

export const stateCatalog = createSlice({
  name: "stateCatalog",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getCatTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getCatTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getCatTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const catalogReducer = stateCatalog.reducer;
