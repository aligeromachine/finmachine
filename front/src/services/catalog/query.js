import { postCheck } from "../../utils/utilsCheck";
import { CAT_URL, CAT_LST } from "./const";

export const getCatalogOptions = async () => {
  const params = {
    command: CAT_LST,
  };
  const response = await postCheck(CAT_URL, params);
  if (!response) return Promise.reject("Error response");
  return response;
};
