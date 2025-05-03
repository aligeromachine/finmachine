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

export const store = configureStore({
  reducer: {
    tokenReducer,
    registerReducer,
    barReducer,
    buysReducer,
    cardsReducer,
    shopReducer,
    sourceReducer,
    profitReducer,
    catalogReducer,
    productsReducer,
  },
});
