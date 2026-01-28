import { postCheck } from '../../utils/utilsCheck';
import { store } from '../store';
import { setRowState, setRowPk } from '../row/state';
import { getShopTable } from './state';
import { SHOP_URL, SHOP_ADD, SHOP_EDIT, SHOP_DEL, SHOP_ROW } from './const';

export const addShopRow = async () => {
    const { pk, formData } = store.getState().rowReducer;
    const params = {
        command: pk === 0 ? SHOP_ADD : SHOP_EDIT,
        pk,
        ...formData,
    };
    const response = await postCheck(SHOP_URL, params);
    if (!response) return Promise.reject('Error response');
    await store.dispatch(getShopTable());
    return response;
};

export const deleteShopRow = async pk => {
    const params = {
        command: SHOP_DEL,
        pk,
    };
    await postCheck(SHOP_URL, params);
    await store.dispatch(getShopTable());
};

export const getShopRow = async pk => {
    const params = {
        command: SHOP_ROW,
        pk,
    };
    const response = await postCheck(SHOP_URL, params);
    store.dispatch(setRowPk(pk));
    store.dispatch(setRowState(response));
};
