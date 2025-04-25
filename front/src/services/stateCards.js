import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
import { apiClient } from "../utils/requests";

const initialState = {
  recordsTotal: 0,
  offset: 0,
  recordsDisplay: 0,
  draw: [],
  loading: "loading" | "idle" | "failed",
};

export const getCardsThunk = createAsyncThunk(
  "stateCards/getCardsThunk",
  async (data) => {
    const response = await apiClient.post("/cards/table/", data);
    return response;
  },
);

export const stateCards = createSlice({
  name: "stateCards",
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(getCardsThunk.pending, (state) => {
        state.loading = "loading";
      })
      .addCase(getCardsThunk.fulfilled, (state, action) => {
        state.recordsTotal = action.payload.recordsTotal;
        state.offset = action.payload.offset;
        state.recordsDisplay = action.payload.recordsDisplay;
        state.draw = action.payload.draw;
        state.loading = "idle";
      })
      .addCase(getCardsThunk.rejected, (state) => {
        state.loading = "failed";
      });
  },
});

export const cardsReducer = stateCards.reducer;
