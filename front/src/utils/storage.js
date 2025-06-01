import { safeJsonParse } from "./func";
import { ONE_HOUR, SEVEN_DAYS } from "./const";

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
  setWithExpiry("accessToken", token, ONE_HOUR);
};

const setRefreshToken = (token) => {
  setWithExpiry("refreshToken", token, SEVEN_DAYS);
};

export const setTokenResponse = (response) => {
  setAccessToken(response.token.access);
  setRefreshToken(response.token.refresh);
};

export const getAccessToken = () => {
  return getWithExpiry("accessToken");
};

export const getRefreshToken = () => {
  return getWithExpiry("refreshToken");
};

export const delAccessToken = () => {
  removeItem("accessToken");
};

export const delRefreshToken = () => {
  removeItem("refreshToken");
};
