import { useEffect } from "react";
import { useDispatch } from "react-redux";
import {
  loadToken,
  setCredentials,
  refreshThunk,
} from "../../services/token/state";

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
