import { useSelector } from "react-redux";
import { Navigate, useLocation } from "react-router";

const Protected = ({ inner, guard = false }) => {
  const location = useLocation();
  const { isAuthChecked, loading } = useSelector((store) => store.tokenReducer);

  if (loading === "loading") return null;

  if (isAuthChecked && !guard) {
    return <Navigate to={"/"} replace />;
  }

  if (!isAuthChecked && guard) {
    return <Navigate to={"/login"} state={location.from} />;
  }

  return inner;
};

export const GuestGuard = Protected;
export const AuthGuard = ({ inner }) => {
  return <Protected inner={inner} guard={true} />;
};
