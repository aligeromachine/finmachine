import React from "react";
import { useEffect } from "react";
import { useDispatch } from "react-redux";

import {
  loadToken,
  setCredentials,
  refreshThunk,
} from "../../services/stateToken";
import { Preloader } from "../preloader/Preloader";

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
