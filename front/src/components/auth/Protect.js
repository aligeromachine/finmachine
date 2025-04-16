import React from "react";
import { useSelector } from "react-redux";
import { Navigate, useLocation } from "react-router";
import { useDispatch } from "react-redux";
import { loadToken } from "../../services/auth";
import { refreshThunk } from "../../services/auth";

const Protected = ({ inner, guard = false }) => {
  const dispatch = useDispatch();

  const { loading, token } = useSelector((store) => store.dataAuth);
  const location = useLocation();

  if (!token) {
    console.log(token);
    loadToken();
  }

  console.log(token);

  if (loading === "loading") return null;

  if (token && !guard) return <Navigate to={"/"} replace />;

  if (!token && guard) {
    dispatch(refreshThunk());

    return <Navigate to={"/login"} state={location.from} />;
  }

  return inner;
};

export const GuestGuard = Protected;
export const AuthGuard = ({ inner }) => (
  <Protected inner={inner} guard={true} />
);
