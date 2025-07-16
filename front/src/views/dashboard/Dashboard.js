import { useState, useEffect } from "react";
import { Auth } from "../../components/auth/Auth";
import { BaseChart } from "./MainChart";
import { WidgetSolid } from "./WidgetSolid";
import { WidgetBase } from "./WidgetBase";
import { WidgetSim } from "./WidgetSim";
import { getDash } from "../../services/dash/query";

export const Dashboard = () => {
  const [data, setData] = useState({});
  useEffect(() => {
    const fetchOptions = async () => {
      const response = await getDash();
      if (response) setData(response);
    };
    fetchOptions();
  }, []);
  return (
    <Auth>
      <WidgetSolid data={data.buy} />
      <WidgetBase data={data.profit} />
      <WidgetSim data={data.cash} card={data.card} />
      <BaseChart />
    </Auth>
  );
};
