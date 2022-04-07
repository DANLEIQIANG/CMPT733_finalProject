import React, {Component} from 'react';
import "./index.css";
import { Row, Col } from "antd";

class File extends Component{
    render() {
            return (
                <div >
                    <div className="chart-wrapper">
                        <h2>EDA: </h2>
                            <Row gutter={32}>
                                <Col xs={24} sm={24} lg={8}>
                                    <div className="chart-wrapper">
                                        <h1>Tweet Length: </h1>
                                            <img src={require("./box_plot_tweet_length.png.png")} alt=""/>
                                    </div>
                                </Col>
                                <Col xs={24} sm={24} lg={8}>
                                    <div className="chart-wrapper">
                                        <h1>Total tweets By Country: </h1>
                                            <img src={require("./country_distribution.png")} alt=""/>
                                    </div>
                                </Col>
                                  <Col xs={24} sm={24} lg={8}>
                                        <div className="chart-wrapper">
                                            <h1>Account history By Country: </h1>
                                                <img src={require("./history_by_country.png")} alt=""/>
                                        </div>
                                    </Col>
                            </Row>
                              <Row gutter={32}>
                                <Col xs={24} sm={24} lg={8}>
                                    <div className="chart-wrapper">
                                        <h1>Tokenization Top20 words Frequency: </h1>
                                            <img src={require("./token_distribution.png")} alt=""/>
                                    </div>
                                </Col>
                               <Col xs={24} sm={24} lg={8}>
                                   <div className="chart-wrapper">
                                       <h1>User Created By Year: </h1>
                                           <img src={require("./user_created.png")} alt=""/>
                                   </div>
                               </Col>

                            </Row>







                    </div>


                </div>
            );
        }
}
export default File;