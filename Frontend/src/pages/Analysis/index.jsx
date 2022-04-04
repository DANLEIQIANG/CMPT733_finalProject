import React, {Component} from 'react';
import { DatePicker, Space } from 'antd';
import { Row, Col } from "antd";
import { Button } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import moment from 'moment';
import "./index.css";
import axios from "axios";
import PanelGroup from "../../components/PanelGroup";
import PieChart from "../../components/PieChart";
import MixChart from "../../components/MixChart";
import BarChart from "../../components/BarChart";

const { RangePicker } = DatePicker;
const dateFormat = 'YYYY/MM/DD';
class Analysis extends Component {
    state = {
        typeClass_war1:[],
        numClass_war1:[],
        infoClass_war1:[],
        typeClass_war2:[],
        numClass_war2:[],
        infoClass_war2:[],
        typeClass_war3:[],
        numClass_war3:[],
        infoClass_war3:[],
        typeClass_election1:[],
        numClass_election1:[],
        infoClass_election1:[],
        typeClass_election2:[],
        numClass_election2:[],
        infoClass_election2:[],
        typeClass_covid1:[],
        numClass_covid1:[],
        infoClass_covid1:[],
        typeClass_covid2:[],
        numClass_covid2:[],
        infoClass_covid2:[],
        date_covid:[],
        positive_covid:[],
        negative_covid:[],
        neutral_covid:[],
    }
    onPickerChange(a,dateString){
        this.setState({
            startTime:dateString[0].replace(/[/]/g,""),
            endTime:dateString[1].replace(/[/]/g,""),
        })

    }
    pieChartData_war(){
        axios.get('http://localhost:3000/api/compare/war').then(
            response => {
                this.setState({
                    typeClass_war1:response.data.info1.map(val => val.type),
                    numClass_war1:response.data.info1.map(val => val.num),
                    infoClass_war1:response.data.info1.map((value) => {return{name: value.type,value:value.num}}),
                    typeClass_war2:response.data.info2.map(val => val.type),
                    numClass_war2:response.data.info2.map(val => val.num),
                    infoClass_war2:response.data.info2.map((value) => {return{name: value.type,value:value.num}}),
                    typeClass_war3:response.data.info3.map(val => val.type),
                    numClass_war3:response.data.info3.map(val => val.num),
                    infoClass_war3:response.data.info3.map((value) => {return{name: value.type,value:value.num}})
                })
            },
            error => {console.log("Pie request error")}
        )
    }
    pieChartData_election(){
        axios.get('http://localhost:3000/api/compare/politic').then(
            response => {
                this.setState({
                    typeClass_election1:response.data.info1.map(val => val.type),
                    numClass_election1:response.data.info1.map(val => val.num),
                    infoClass_election1:response.data.info1.map((value) => {return{name: value.type,value:value.num}}),
                    typeClass_election2:response.data.info2.map(val => val.type),
                    numClass_election2:response.data.info2.map(val => val.num),
                    infoClass_election2:response.data.info2.map((value) => {return{name: value.type,value:value.num}})
                })
            },
            error => {console.log("Pie request error")}
        )
    }
    pieChartData_covid(){
        axios.get('http://localhost:3000/api/compare/covid').then(
            response => {
                this.setState({
                    typeClass_covid1:response.data.info1.map(val => val.type),
                    numClass_covid1:response.data.info1.map(val => val.num),
                    infoClass_covid1:response.data.info1.map((value) => {return{name: value.type,value:value.num}}),
                    typeClass_covid2:response.data.info2.map(val => val.type),
                    numClass_covid2:response.data.info2.map(val => val.num),
                    infoClass_covid2:response.data.info2.map((value) => {return{name: value.type,value:value.num}})
                })
            },
            error => {console.log("Pie request error")}
        )
    }
    barChartData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/api/covid_byday').then(
            response => {
                this.setState({
                    date_covid : response.data.date,
                    positive_covid : response.data.positive,
                    negative_covid : response.data.negative,
                    neutral_covid : response.data.neutral

                })
                console.log(this.state)
            },
            error => {console.log("Panel Group request error")}
        )
    }

    render() {
        return (
            <div >
                <div>
                    <Button icon={<SearchOutlined />}
                            onClick = {() =>{this.pieChartData_war();this.pieChartData_election();this.pieChartData_covid();this.barChartData()}}>Click to find result:
                    </Button>

                    <div className="chart-wrapper">
                        <h2>War: </h2>
                        <Row gutter={32}>
                            <Col xs={24} sm={24} lg={8}>
                                <div className="chart-wrapper">
                                    <h1>Normal: </h1>
                                    <PieChart typeClass={this.state.typeClass_war1} numClass={this.state.numClass_war1} infoClass={this.state.infoClass_war1}/>

                                </div>
                            </Col>
                            <Col xs={24} sm={24} lg={8}>
                                <div className="chart-wrapper">
                                    <h1>Holiday: </h1>
                                    <PieChart typeClass={this.state.typeClass_war2} numClass={this.state.numClass_war2} infoClass={this.state.infoClass_war2}/>
                                </div>
                            </Col>
                            <Col xs={24} sm={24} lg={8}>
                                <div className="chart-wrapper">
                                    <h1>War start: </h1>
                                    <PieChart typeClass={this.state.typeClass_war3} numClass={this.state.numClass_war3} infoClass={this.state.infoClass_war3}/>
                                </div>
                            </Col>
                        </Row>
                        <h2>Election: </h2>
                        <Row gutter={8}>
                            <Col  xs={24} sm={24} md={24} lg={12} xl={12}
                                  style={{paddingRight: "8px" }}>
                                <div className="chart-wrapper">
                                    <h1>Before: </h1>
                                    <PieChart typeClass={this.state.typeClass_election1} numClass={this.state.numClass_election1} infoClass={this.state.infoClass_election1}/>
                                </div>
                            </Col>
                            <Col  xs={24} sm={24} md={24} lg={12} xl={10} style={{paddingRight: "8px"}}>
                                <div className="chart-wrapper">
                                    <h1>After: </h1>
                                    <PieChart typeClass={this.state.typeClass_election2} numClass={this.state.numClass_election2} infoClass={this.state.infoClass_election2}/>
                                </div>
                            </Col>

                        </Row>

                        <h2>Covid19: </h2>
                        <Row gutter={8}>
                            <Col  xs={24} sm={24} md={24} lg={12} xl={12}
                                  style={{paddingRight: "8px" }}>
                                <div className="chart-wrapper">
                                    <h1>2019.3.07-2019.3.14: </h1>
                                    <PieChart typeClass={this.state.typeClass_covid1} numClass={this.state.numClass_covid1} infoClass={this.state.infoClass_covid1}/>
                                </div>
                            </Col>
                            <Col  xs={24} sm={24} md={24} lg={12} xl={10} style={{paddingRight: "8px"}}>
                                <div className="chart-wrapper">
                                    <h1>2020.3.07-2020.3.14: </h1>
                                    <PieChart typeClass={this.state.typeClass_covid2} numClass={this.state.numClass_covid2} infoClass={this.state.infoClass_covid2}/>
                                </div>
                            </Col>

                        </Row>
                        <h1>Covid 2020.3.07 - 2020.3.15: </h1>
                        <BarChart country={this.state.date_covid} positive_coutry={this.state.positive_covid} negative_country={this.state.negative_covid} neutral_country={this.state.neutral_covid}/>










                        <br />
                        <br />
                        <br />
                        <br />
                        <br />
                        <br />

                    </div>

                </div>
            </div>
        );
    }
}

export default Analysis;