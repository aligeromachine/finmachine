import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../../utils/requests";
import { create_params } from "../../utils/func";
import { store } from "../store";
import { initialState } from "./model";
import { CARDS_URL, CARDS_TBL } from "./const";

export const getCardsTable = createAsyncThunk(
  "stateCards/getCardsTable",
  async () => {
    const { offset, recordsDisplay } = store.getState().cardsReducer;
    const params = create_params(CARDS_TBL, offset, recordsDisplay);
    const response = await apiClient.post(CARDS_URL, params);
    return response;
  },
);

export const stateCards = createSlice({
  name: "stateCards",
  initialState: initialState,
  reducers: {
    setOffset: (state, action) => {
      state.offset = action.payload.offset;
    },
  },
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

export const { setOffset } = stateCards.actions;
export const cardsReducer = stateCards.reducer;
