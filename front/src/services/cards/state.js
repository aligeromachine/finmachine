import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { setRowState, setRowPk } from "../row/state";
import { store } from "../store";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 100,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

const PREFIX_URL = "/cards/data/";

export const getCardsTable = createAsyncThunk(
  "stateCards/getCardsTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().cardsReducer;
    const params = create_params("table_cards_data", offset, recordsDisplay);
    const response = await apiClient.post(PREFIX_URL, params);
    return response;
  },
);

export const addCardsRow = async () => {
  const { pk, formData } = store.getState().rowReducer;
  const params = {
    command: pk === 0 ? "add_cards_data" : "edit_cards_data",
    pk,
    ...formData,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  if (!response) return Promise.reject("Error response");
  await store.dispatch(getCardsTable());
  return response;
};

export const deleteCardsRow = async (pk) => {
  const params = {
    command: "delete_cards_row",
    pk,
  };
  await apiClient.post(PREFIX_URL, params);
  await store.dispatch(getCardsTable());
};

export const getCardsRow = async (pk) => {
  const params = {
    command: "get_cards_row",
    pk,
  };
  const response = await apiClient.post(PREFIX_URL, params);
  store.dispatch(setRowPk(pk));
  store.dispatch(setRowState(response));
};

export const stateCards = createSlice({
  name: "stateCards",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getCardsTable.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getCardsTable.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getCardsTable.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const cardsReducer = stateCards.reducer;
