import React from "react";
import { Row, Col} from "antd";
import CountUp from "react-countup";
import "./index.css";

let chartList = [
    {
        type: "Friendly",
        num: 102400,
    },
    {
        type: "Unfrinedly",
        num: 81212,
    },
    {
        type: "Total",
        num: 81212,
    },
];

const PanelGroup = (props) => {
    const {chartList, endTime} = props
    return (
        <div className="panel-group-container">
            <Row gutter={40} className="panel-group">
                {chartList.map((chart, i) => (
                    <Col
                        key={i}
                        lg={8}
                        sm={12}
                        xs={12}
                        className="card-panel-col"
                    >
                    <div className="card-panel">
                        <div className="card-panel-description">
                            <p className="card-panel-text">{chart.type}</p>
                            <CountUp end={chart.num} start={0} className="card-panel-num" />
                        </div>
                    </div>
                    </Col>
                ))}
            </Row>
        </div>
    );
};

export default PanelGroup;