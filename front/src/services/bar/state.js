import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  sidebarShow: true,
  sidebarUnfoldable: false,
  theme: "light",
};

const stateBar = createSlice({
  name: "stateBar",
  initialState,
  reducers: {
    changeSideShow: (state, action) => {
      state.sidebarShow = action.payload;
    },
    changeSideUnfo: (state, action) => {
      state.sidebarUnfoldable = action.payload;
    },
    changeTheme: (state, action) => {
      state.theme = action.payload;
    },
  },
});

export const { changeSideShow, changeSideUnfo, changeTheme } = stateBar.actions;
export const barReducer = stateBar.reducer;
