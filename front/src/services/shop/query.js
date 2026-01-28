import { postCheck } from '../../utils/utilsCheck';
import { SHOP_URL, SHOP_LST } from './const';

export const getShopOptions = async () => {
    const params = {
        command: SHOP_LST,
    };
    const response = await postCheck(SHOP_URL, params);
    if (!response) return Promise.reject('Error response');
    return response;
};
