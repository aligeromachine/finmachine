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
import { registerThunk, setRegister } from "../../services/stateRegister";
import { UseForm } from "../../components/hook/UseForm";
import { UseValidRegister } from "./Validate";
import { RedLable } from "../../components/redflag/RedLable";

export const Register = () => {
  const dispatch = useDispatch();
  const { formData, onChange } = UseForm();
  const { validate, validateForm } = UseValidRegister();

  const { register, error, loading } = useSelector(
    (store) => store.registerReducer,
  );

  useEffect(() => {
    dispatch(setRegister());
  }, [dispatch]);

  async function onRegister(e) {
    e.preventDefault();

    if (!validateForm(formData)) {
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
                  {loading === "empty" && (
                    <CFormLabel className="text-info">
                      Create your account
                    </CFormLabel>
                  )}
                  {register && (
                    <CFormLabel className="text-success">
                      User create success!
                    </CFormLabel>
                  )}
                  <RedLable title={error} />
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
                  <RedLable title={validate.username} />
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
                  <RedLable title={validate.email} />
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
                  <RedLable title={validate.password} />
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
                  <RedLable title={validate.confirmPassword} />
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
