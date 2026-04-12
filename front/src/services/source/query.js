import { postRequestCheck } from '../../utils/requests';
import { SOURCE_URL, SOURCE_LST } from './const';

export const getSourceOptions = async () => {
    const params = {
        command: SOURCE_LST,
    };
    const response = await postRequestCheck(SOURCE_URL, params);
    if (!response) return Promise.reject('Error response');
    return response;
};
