import { configureStore } from "@reduxjs/toolkit";
import { tokenReducer } from "./stateToken";
import { registerReducer } from "./stateRegister";
import { barReducer } from "./stateBar";
import { buysReducer } from "./stateBuys";
import { cardsReducer } from "./stateCards";
import { shopReducer } from "./stateShop";
import { sourceReducer } from "./stateSource";
import { profitReducer } from "./stateProfit";
import { catalogReducer } from "./stateCatalog";
import { productsReducer } from "./stateProducts";

const store = configureStore({
  reducer: {
    barReducer,
    buysReducer,
    tokenReducer,
    registerReducer,
    cardsReducer,
    shopReducer,
    sourceReducer,
    profitReducer,
    catalogReducer,
    productsReducer,
  },
});

export default store;
