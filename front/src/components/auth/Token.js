import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { setCredentials, refreshThunk } from "../../services/token/state";
import { loadToken } from "../../services/token/utils";

export const Token = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    const token = loadToken();
    if (token) {
      dispatch(setCredentials(token));
    } else {
      dispatch(refreshThunk());
    }
  }, [dispatch]);
};
