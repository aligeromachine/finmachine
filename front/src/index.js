import React from 'react';
import 'core-js';
import { createRoot } from 'react-dom/client';
import { Provider } from 'react-redux';
import { PageConstructor } from './pages/PageConstructor';
import { store } from './services/store';

createRoot(document.getElementById('root')).render(
    <Provider store={store}>
        <PageConstructor />
    </Provider>
);
