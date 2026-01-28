import { store } from '../store';
import { refreshThunk } from './state';
import { getAccessToken } from '../../utils/storage';

export const checkToken = async () => {
    if (!getAccessToken()) {
        await store.dispatch(refreshThunk());
    }
};
