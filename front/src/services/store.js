import { configureStore } from '@reduxjs/toolkit';
import { tokenReducer } from './utils/token/state';
import { registerReducer } from './utils/register/state';
import { barReducer } from './utils/bar/state';
import { buysReducer } from './buys/state';
import { cardsReducer } from './cards/state';
import { shopReducer } from './shop/state';
import { sourceReducer } from './source/state';
import { profitReducer } from './profit/state';
import { catalogReducer } from './catalog/state';
import { productsReducer } from './products/state';
import { rowReducer } from './utils/row/state';

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
