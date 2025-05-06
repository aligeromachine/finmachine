import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  pk: 0,
  formData: null,
};

const stateRow = createSlice({
  name: "stateRow",
  initialState,
  reducers: {
    setRowState: (state, action) => {
      state.pk = action.payload.pk;
      state.formData = action.payload.formData;
    },
  },
});

export const { setRowState } = stateRow.actions;
export const rowReducer = stateRow.reducer;
