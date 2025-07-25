import { createSlice } from "@reduxjs/toolkit";
import { initialState } from "./model";

const stateRow = createSlice({
  name: "stateRow",
  initialState,
  reducers: {
    setRowState: (state, action) => {
      state.formData = { ...state.formData, ...action.payload };
    },
    setRowPk: (state, action) => {
      state.pk = action.payload;
    },
    nullRowData: (state) => {
      state.pk = 0;
      state.formData = {};
    },
  },
});

export const { setRowState, setRowPk, nullRowData } = stateRow.actions;
export const rowReducer = stateRow.reducer;
