import { configureStore } from '@reduxjs/toolkit'
import sideBar from './sideBar'
import dataBuys from './dataBuys'
import dataAuth from './auth'

const store = configureStore({
  reducer: {
    sideBar,
    dataBuys,
    dataAuth,
  },
})

export default store
