import React, { useState, useEffect } from "react";
import {
  CButton,
  CCard,
  CCardBody,
  CCol,
  CContainer,
  CForm,
  CFormInput,
  CInputGroup,
  CInputGroupText,
  CFormFeedback,
  CFormLabel,
  CRow,
} from "@coreui/react";
import CIcon from "@coreui/icons-react";
import { cilLockLocked, cilUser } from "@coreui/icons";
import { useDispatch, useSelector } from "react-redux";
import { registerThunk, setRegister } from "../../services/auth";
import { UseForm } from "../../components/hook/UseForm";
import { isEmpty } from "../../utils/func";

const Register = () => {
  const dispatch = useDispatch();
  const { formData, onChange } = UseForm();
  const [errors, setErrors] = useState({});

  const { register, registerErr, registerLoading } = useSelector(
    (store) => store.dataAuth,
  );

  useEffect(() => {
    dispatch(setRegister());
  }, [dispatch]);

  const validateForm = () => {
    const newErrors = {};

    if (!formData.username) {
      newErrors.username = "Имя обязательно";
    }

    if (!formData.email) {
      newErrors.email = "Email обязателен";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = "Некорректный email";
    }

    if (!formData.password) {
      newErrors.password = "Пароль обязателен";
    } else if (formData.password.length < 6) {
      newErrors.password = "Пароль должен быть не менее 6 символов";
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = "Пароли не совпадают";
    }

    setErrors(newErrors);
    return isEmpty(newErrors);
  };

  async function onRegister(e) {
    e.preventDefault();

    if (!validateForm()) {
      return;
    }

    await dispatch(registerThunk(formData));
  }

  return (
    <div className="bg-body-tertiary min-vh-100 d-flex flex-row align-items-center">
      <CContainer>
        <CRow className="justify-content-center">
          <CCol md={9} lg={7} xl={6}>
            <CCard className="mx-4">
              <CCardBody className="p-4">
                <CForm onSubmit={onRegister}>
                  <h1>Register </h1>
                  {registerLoading === "empty" && (
                    <CFormLabel className="text-info">
                      Create your account
                    </CFormLabel>
                  )}
                  {register && (
                    <CFormLabel className="text-success">
                      User create success!
                    </CFormLabel>
                  )}
                  {registerErr && (
                    <CFormLabel className="text-danger">
                      {registerErr}
                    </CFormLabel>
                  )}
                  <CInputGroup className="mb-3">
                    <CInputGroupText>
                      <CIcon icon={cilUser} />
                    </CInputGroupText>
                    <CFormInput
                      placeholder="Username"
                      autoComplete="username"
                      onChange={onChange}
                      value={formData.username || ""}
                      name={"username"}
                    />
                  </CInputGroup>
                  {errors.username && (
                    <p className="text-sm mt-1">{errors.username}</p>
                  )}
                  <CInputGroup className="mb-3">
                    <CInputGroupText>@</CInputGroupText>
                    <CFormInput
                      placeholder="Email"
                      autoComplete="email"
                      onChange={onChange}
                      value={formData.email || ""}
                      name={"email"}
                    />
                  </CInputGroup>
                  {errors.email && (
                    <CFormLabel className="text-danger">
                      {errors.email}
                    </CFormLabel>
                  )}
                  <CInputGroup className="mb-3">
                    <CInputGroupText>
                      <CIcon icon={cilLockLocked} />
                    </CInputGroupText>
                    <CFormInput
                      type="password"
                      placeholder="Password"
                      autoComplete="new-password"
                      onChange={onChange}
                      value={formData.password || ""}
                      name={"password"}
                    />
                  </CInputGroup>
                  {errors.password && (
                    <CFormLabel className="text-danger">
                      {errors.password}
                    </CFormLabel>
                  )}
                  <CInputGroup className="mb-4">
                    <CInputGroupText>
                      <CIcon icon={cilLockLocked} />
                    </CInputGroupText>
                    <CFormInput
                      type="password"
                      placeholder="Repeat password"
                      autoComplete="new-password"
                      onChange={onChange}
                      value={formData.confirmPassword || ""}
                      name={"confirmPassword"}
                    />
                  </CInputGroup>
                  {errors.confirmPassword && (
                    <CFormLabel className="text-danger">
                      {errors.confirmPassword}
                    </CFormLabel>
                  )}
                  <div className="d-grid">
                    <CButton color="success" type="submit">
                      Create Account
                    </CButton>
                  </div>
                </CForm>
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
      </CContainer>
    </div>
  );
};

export default Register;
