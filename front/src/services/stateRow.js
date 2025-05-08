import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  pk: 0,
  formData: {},
};

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
    getRowState: (state) => {
      return { ...state.formData };
    },
  },
});

export const { setRowState, setRowPk, getRowState } = stateRow.actions;
export const rowReducer = stateRow.reducer;
