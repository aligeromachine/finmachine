import { getWithExpiry } from "../../utils/storage";

export const loadToken = () => {
  const token = getWithExpiry("accessToken");
  return token;
};
