import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setAuthCheck } from "../../services/token/state";
import { getAccessToken } from "../../utils/storage";

export const Token = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    if (getAccessToken()) dispatch(setAuthCheck());
  }, [dispatch]);
};
