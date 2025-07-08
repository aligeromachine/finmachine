import {
  CCard,
  CCardBody,
  CCol,
  CRow,
  CTab,
  CTabContent,
  CTabList,
  CTabPanel,
  CTabs,
  CCardHeader,
} from "@coreui/react";
import { ModalProvider } from "../../components/hook/ModalContext";
import { Header } from "../../components/elems/Header";
import { Button } from "../../components/elems/Button";
import { Auth } from "../../components/auth/Auth";

import "../../libs/prism-coy.css";

export const Config = () => {
  return (
    <Auth>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Logger</strong>
            </CCardHeader>
            <CCardBody>
              <CTabs activeItemKey={2}>
                <CTabList variant="underline-border">
                  <CTab aria-controls="home-tab-pane" itemKey={1}>
                    Money
                  </CTab>
                  <CTab aria-controls="profile-tab-pane" itemKey={2}>
                    Api
                  </CTab>
                  <CTab aria-controls="contact-tab-pane" itemKey={3}>
                    Django
                  </CTab>
                </CTabList>
                <CTabContent>
                  <CTabPanel
                    className="py-3"
                    aria-labelledby="home-tab-pane"
                    itemKey={1}
                  >
                    <CCardBody>
                      <code className="language-makrup">
                        classes are also available, for when you want to match
                        the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML
                        element.classes are also available, for when you want to
                        match the font styling of a heading but cannot use the
                        associated HTML element.classes are also available, for
                        when you want to match the font styling of a heading but
                        cannot use the associated HTML element.classes are also
                        available, for when you want to match the font styling
                        of a heading but cannot use the associated HTML element.
                      </code>
                    </CCardBody>
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    aria-labelledby="profile-tab-pane"
                    itemKey={2}
                  >
                    Profile tab content
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    aria-labelledby="contact-tab-pane"
                    itemKey={3}
                  >
                    Contact tab content
                  </CTabPanel>
                </CTabContent>
              </CTabs>
            </CCardBody>
          </CCard>
        </CCol>
      </CRow>
    </Auth>
  );
};
