import { safeJsonParse } from "./func";
import { TWENTY_MIN, SEVEN_DAYS } from "./const";

const setWithExpiry = (key, value, ttl) => {
  const now = new Date();
  const item = {
    value: value,
    expiry: now.getTime() + ttl,
  };
  localStorage.setItem(key, JSON.stringify(item));
};

const getWithExpiry = (key) => {
  const itemStr = localStorage.getItem(key);

  if (!itemStr) {
    return null;
  }

  const result = safeJsonParse(itemStr);
  if (!result.success) {
    localStorage.removeItem(key);
    return null;
  }

  const item = result.data;
  const now = new Date();

  if (now.getTime() > item.expiry) {
    localStorage.removeItem(key);
    return null;
  }

  return item.value;
};

export const removeItem = (key) => {
  localStorage.removeItem(key);
};

const setAccessToken = (token) => {
  setWithExpiry("accessToken", token, TWENTY_MIN);
};

const setRefreshToken = (token) => {
  setWithExpiry("refreshToken", token, SEVEN_DAYS);
};

export const setTokenResponse = (action) => {
  setAccessToken(action.payload.access);
  setRefreshToken(action.payload.refresh);
};

export const getAccessToken = () => {
  return getWithExpiry("accessToken");
};

export const getRefreshToken = () => {
  return getWithExpiry("refreshToken");
};

const delAccessToken = () => {
  removeItem("accessToken");
};

const delRefreshToken = () => {
  removeItem("refreshToken");
};

export const delToken = () => {
  delAccessToken();
  delRefreshToken();
};
