import React from "react";
import { useSelector } from "react-redux";
import { Navigate, useLocation } from "react-router";

const Protected = ({ inner, guard = false }) => {
  const { loading, token } = useSelector((store) => store.tokenReducer);
  const location = useLocation();

  if (loading === "loading") return null;

  if (token && !guard) return <Navigate to={"/"} replace />;

  if (!token && guard) {
    return <Navigate to={"/login"} state={location.from} />;
  }

  return inner;
};

export const GuestGuard = Protected;
export const AuthGuard = ({ inner }) => (
  <Protected inner={inner} guard={true} />
);
