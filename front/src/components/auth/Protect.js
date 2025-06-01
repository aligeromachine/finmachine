import { useSelector } from "react-redux";
import { Navigate, useLocation } from "react-router";
import { getAccessToken } from "../../utils/storage";

const Protected = ({ inner, guard = false }) => {
  const location = useLocation();
  const { loading } = useSelector((store) => store.tokenReducer);
  const isAuth = Boolean(getAccessToken());

  if (loading === "loading") return null;

  if (isAuth && !guard) {
    return <Navigate to={"/"} replace />;
  }

  if (!isAuth && guard) {
    return <Navigate to={"/login"} state={location.from} />;
  }

  return inner;
};

export const GuestGuard = Protected;
export const AuthGuard = ({ inner }) => {
  return <Protected inner={inner} guard={true} />;
};
