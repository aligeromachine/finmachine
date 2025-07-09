import React, { useState, useEffect } from "react";
import {
  CButton,
  CModal,
  CModalBody,
  CModalFooter,
  CModalHeader,
  CModalTitle,
  CFormInput,
  CFormSelect,
  CCol,
  CForm,
} from "@coreui/react";
import { RedCAlert } from "../../../components/elems/RedCAlert";
import { RedLable } from "../../../components/elems/RedCAlert";
import { AsyncFormSelect } from "../../../components/form/Select";
import { getShopOptions } from "../../../services/shop/query";
import { getCatalogOptions } from "../../../services/catalog/query";
import { getProdOptions } from "../../../services/products/query";
import { DatePicElem } from "../../../components/datetimepiker/BigDatepicker";

export const ProfitContent = ({
  visible,
  onClose,
  formData,
  onChange,
  validate,
  repErr,
  onAdd,
  isEdit,
}) => {
  const [secondaryOptions, setSecondaryOptions] = useState([]);
  useEffect(() => {
    if (formData.cat) {
      const fetchOptions = async () => {
        const data = await getProdOptions(formData.cat);

        const listOptions = data.map((item) => ({
          value: item.id,
          label: item.title,
        }));

        const newItems = [{ value: "", label: "-- Choise --", disabled: true }];

        setSecondaryOptions([...newItems, ...listOptions]);
        if (!isEdit) {
          formData.prod = "";
        }
      };

      fetchOptions();
    } else {
      setSecondaryOptions([]);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [formData.cat]);

  return (
    <CModal size="lg" visible={visible} onClose={onClose}>
      <CModalHeader>
        <CModalTitle>Buys Data</CModalTitle>
      </CModalHeader>
      <CModalBody>
        <CForm className="row g-3">
          <CCol xs={12}>
            <DatePicElem
              onChange={onChange}
              value={formData.created || new Date()}
              name={"created"}
            />
          </CCol>
          <CCol xs={12}>
            <AsyncFormSelect
              label={"Shop"}
              onChange={onChange}
              value={formData.shop || ""}
              name={"shop"}
              request={getShopOptions}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <AsyncFormSelect
              label={"Catalog"}
              onChange={onChange}
              value={formData.cat || ""}
              name={"cat"}
              request={getCatalogOptions}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormSelect
              label="Products"
              aria-label="Default select example"
              placeholder="Выберите вариант..."
              value={formData.prod || ""}
              name={"prod"}
              onChange={onChange}
              options={secondaryOptions}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Title"
              placeholder="5 ed"
              onChange={onChange}
              value={formData.title || ""}
              name={"title"}
            />
            <RedLable title={validate.title} />
          </CCol>
          <CCol xs={12}>
            <CFormInput
              label="Amount"
              placeholder="125.2"
              onChange={onChange}
              value={formData.amount || ""}
              name={"amount"}
            />
            <RedLable title={validate.amount} />
          </CCol>
        </CForm>
        <RedCAlert title={repErr} />
      </CModalBody>
      <CModalFooter>
        <CButton color="secondary" onClick={onClose}>
          Close
        </CButton>
        <CButton color="primary" onClick={onAdd}>
          Save changes
        </CButton>
      </CModalFooter>
    </CModal>
  );
};
