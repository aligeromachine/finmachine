import { postCheck } from '../../utils/utilsCheck';
import { PROD_URL, PROD_LST } from './const';

export const getProdOptions = async pk => {
    const params = {
        command: PROD_LST,
        pk,
    };
    const response = await postCheck(PROD_URL, params);
    if (!response) return Promise.reject('Error response');
    return response;
};
