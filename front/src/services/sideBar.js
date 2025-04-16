import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  sidebarShow: true,
  sidebarUnfoldable: false,
  theme: 'light',
}

const sideBar = createSlice({
  name: 'sideBar',
  initialState,
  reducers: {
    changeSideShow: (state, action) => {
      state.sidebarShow = action.payload
    },
    changeSideUnfo: (state, action) => {
      state.sidebarUnfoldable = action.payload
    },
    changeTheme: (state, action) => {
      state.theme = action.payload
    },
  },
})

export const { changeSideShow, changeSideUnfo, changeTheme } = sideBar.actions
export default sideBar.reducer
