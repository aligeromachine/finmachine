import { store } from '../../store';
import { refreshThunk } from './state';

export const refreshToken = async () => {
    const response = await store.dispatch(refreshThunk());
    return response;
};
