import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { setRowState, setRowPk } from "../row/state";
import { store } from "../store"; // Импортируем Redux store


const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 100,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

const PREFIX_URL = "/source/data/";

export const getSourceTable = createAsyncThunk(
  "stateSource/getSourceTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().sourceReducer;
    const params = create_params("table_source_data", offset, recordsDisplay);
    const response = await apiClient.post(PREFIX_URL, params);
    return response;
  },
);

export const addSourceRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? "add_source_data" : "edit_source_data",
    pk,
    ...formData,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getSourceTable());
  return response;
};

export const deleteSourceRow = async (pk) => {
  const params = {
    command: "delete_source_row",
    pk,
  };
  await apiClient.post(PREFIX_URL, params);
  await store.dispatch(getSourceTable());
};

export const getSourceRow = async (pk) => {
  const params = {
    command: "get_source_row",
    pk,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};

export const stateSource = createSlice({
  name: "stateSource",
  initialState: initialState,
  reducers: {},
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

export const sourceReducer = stateSource.reducer;
