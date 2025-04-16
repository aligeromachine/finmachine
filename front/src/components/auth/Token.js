import React from "react";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useSelector } from "react-redux";

import { refreshThunk } from "../../services/auth";
import { Preloader } from "../preloader/Preloader";

export const Token = () => {
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(refreshThunk());
  }, [dispatch]);

  const user = useSelector((store) => store.dataAuth.loading) !== "idle";

  return <Preloader isLoading={user} />;
};
