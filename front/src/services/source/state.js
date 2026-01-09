import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { store } from "../store"; // Импортируем Redux store
import { SOURCE_URL, SOURCE_TBL } from "./const";
import { initialState } from "./model";

export const getSourceTable = createAsyncThunk(
  "stateSource/getSourceTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().sourceReducer;
    const params = create_params(SOURCE_TBL, offset, recordsDisplay);
    const response = await apiClient.post(SOURCE_URL, params);
    return response;
  },
);

export const stateSource = createSlice({
  name: "stateSource",
  initialState: initialState,
  reducers: {
    setOffset: (state, action) => {
      state.offset = action.payload.offset;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getSourceTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getSourceTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getSourceTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const { setOffset } = stateSource.actions;
export const sourceReducer = stateSource.reducer;
