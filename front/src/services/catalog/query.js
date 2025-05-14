import { apiClient } from "../../utils/requests";
import { CAT_URL, CAT_LST } from "./const";

export const getCatalogOptions = async () => {
  const params = {
    command: CAT_LST,
  };
  const response = await apiClient.post(CAT_URL, params);
  if (!response) return Promise.reject("Error response");
  return response;
};
