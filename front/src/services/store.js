import { configureStore } from '@reduxjs/toolkit';
import { tokenReducer } from './token/state';
import { registerReducer } from './register/state';
import { barReducer } from './bar/state';
import { buysReducer } from './buys/state';
import { cardsReducer } from './cards/state';
import { shopReducer } from './shop/state';
import { sourceReducer } from './source/state';
import { profitReducer } from './profit/state';
import { catalogReducer } from './catalog/state';
import { productsReducer } from './products/state';
import { rowReducer } from './row/state';

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
        rowReducer,
    },
});
