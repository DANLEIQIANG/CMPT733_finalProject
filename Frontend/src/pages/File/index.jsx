import React, {Component} from 'react';
import "./index.css";
import { Row, Col } from "antd";

class File extends Component{
    render() {
            return (
                <div >
                    <div className="chart-wrapper">
                        <h2>War: </h2>
                            <Row gutter={32}>
                                <Col xs={24} sm={24} lg={12}>
                                    <div className="chart-wrapper">
                                        <h1>Normal: </h1>
                                            <img src={require("./tensorboard.png")} alt=""/>
                                    </div>
                                </Col>
                                <Col xs={24} sm={24} lg={12}>
                                    <div className="chart-wrapper">
                                        <h1>Holiday: </h1>
                                            <img src={require("./tensorboard.png")} alt=""/>

                                    </div>
                                </Col>

                            </Row>




                    </div>


                </div>
            );
        }
}
export default File;