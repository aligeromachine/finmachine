import { checkToken } from "../services/token/request";
import { apiClient } from "./requests";

export const postCheck = async (url, params) => {
  await checkToken();
  return await apiClient.post(url, params);
};
