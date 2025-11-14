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
      <WidgetSim data={data.capital} card={data.cards} />
      <WidgetBase data={data.profit} />
      <WidgetSolid data={data.buy} />
      <BaseChart />
    </Auth>
  );
};
