import { safeJsonParse } from './func';
import { INTERVAL } from './const';
import { getTokenExpirationInfo } from './token';
import { printObj } from './func';

const ACCESS_TOKEN = 'accessToken';
const REFRESH_TOKEN = 'refreshToken';

const removeItem = key => {
    localStorage.removeItem(key);
};

const setWithExpiry = (key, value, ttl) => {
    if (!value) return;

    const now = new Date();
    const item = {
        value: value,
        expiry: now.getTime() + ttl,
    };
    localStorage.setItem(key, JSON.stringify(item));
};

const getWithExpiry = (key, ignore) => {
    const itemStr = localStorage.getItem(key);

    if (!itemStr) {
        return null;
    }

    const result = safeJsonParse(itemStr);
    if (!result) {
        removeItem(key);
        return null;
    }

    const item = result;
    const now = new Date();
    const expiry = now.getTime();

    if (ignore) {
        return item.value;
    }

    if (expiry > item.expiry) {
        removeItem(key);
        return null;
    }

    return item.value;
};

const setAccessToken = token => {
    const data = getTokenExpirationInfo(token);
    printObj(data);
    setWithExpiry(ACCESS_TOKEN, token, INTERVAL.MIN_TRIRTY);
};

const setRefreshToken = token => {
    setWithExpiry(REFRESH_TOKEN, token, INTERVAL.DAY_SEVEN);
};

export const setTokenResponse = payload => {
    setAccessToken(payload?.access);
    setRefreshToken(payload?.refresh);
};

export const getAccessToken = ignore => {
    return getWithExpiry(ACCESS_TOKEN, ignore ? true : false);
};

export const getRefreshToken = () => {
    return getWithExpiry(REFRESH_TOKEN, false);
};

const delAccessToken = () => {
    removeItem(ACCESS_TOKEN);
};

const delRefreshToken = () => {
    removeItem(REFRESH_TOKEN);
};

export const delToken = () => {
    delAccessToken();
    delRefreshToken();
};
