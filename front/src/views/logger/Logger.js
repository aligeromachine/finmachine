import { useState, useEffect } from "react";
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
import { ButtonBase } from "../../components/elems/Button";
import { Auth } from "../../components/auth/Auth";
import { getLogger, delLogger } from "../../services/logger/query";
import { MONEY, DJANGO, API } from "../../services/logger/const";
import { CodeBlock } from "../../components/elems/CodeBlock";
import { handleDeleteLog } from "../../components/action/Action";

export const Logger = () => {
  const [dataLog, setLog] = useState({});
  useEffect(() => {
    const fetchOptions = async () => {
      const data = await getLogger();

      if (data) {
        setLog(data.message);
      }
    };

    fetchOptions();
  }, []);

  const baseClick = async (msg) => {
    const freeCanvas = async () => {
      const data = await delLogger(msg);
      setLog({ ...dataLog, ...{ [msg]: data.message } });
    };
    handleDeleteLog(msg, freeCanvas);
  };

  return (
    <Auth>
      <CRow>
        <CCol xs={12}>
          <CCard className="mb-4">
            <CCardHeader>
              <strong>Logger</strong>
            </CCardHeader>
            <CCardBody>
              <CTabs activeItemKey={1}>
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
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(MONEY);
                      }}
                    />
                    <CodeBlock content={dataLog.money} />
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    aria-labelledby="profile-tab-pane"
                    itemKey={2}
                  >
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(API);
                      }}
                    />
                    <CodeBlock content={dataLog.api} />
                  </CTabPanel>
                  <CTabPanel
                    className="py-3"
                    aria-labelledby="contact-tab-pane"
                    itemKey={3}
                  >
                    <ButtonBase
                      title={"Clear"}
                      onClick={() => {
                        baseClick(DJANGO);
                      }}
                    />
                    <CodeBlock content={dataLog.django} />
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
