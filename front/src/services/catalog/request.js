import { postCheck } from '../../utils/utilsCheck';
import { store } from '../store';
import { setRowState, setRowPk } from '../row/state';
import { getCatTable } from './state';
import { CAT_URL, CAT_ADD, CAT_EDIT, CAT_DEL, CAT_ROW } from './const';

export const addCatRow = async () => {
    const { pk, formData } = store.getState().rowReducer;
    const params = {
        command: pk === 0 ? CAT_ADD : CAT_EDIT,
        pk,
        ...formData,
    };
    const response = await postCheck(CAT_URL, params);
    if (!response) return Promise.reject('Error response');
    await store.dispatch(getCatTable());
    return response;
};

export const deleteCatRow = async pk => {
    const params = {
        command: CAT_DEL,
        pk,
    };
    await postCheck(CAT_URL, params);
    await store.dispatch(getCatTable());
};

export const getCatRow = async pk => {
    const params = {
        command: CAT_ROW,
        pk,
    };
    const response = await postCheck(CAT_URL, params);
    store.dispatch(setRowPk(pk));
    store.dispatch(setRowState(response));
};
