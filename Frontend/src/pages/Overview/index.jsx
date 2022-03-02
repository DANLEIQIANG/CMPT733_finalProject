import React, {Component} from 'react';
import { DatePicker, Space } from 'antd';
import { Row, Col } from "antd";
import moment from 'moment';
import BarChart from "../../components/BarChart";
import "./index.css";
import MixChart from "../../components/MixChart";
import LineChart from "../../components/LineChart";
import PieChart from "../../components/PieChart";
import BoxCard from "../../components/BoxCard";
import PanelGroup from "../../components/PanelGroup";
import axios from "axios";

const { RangePicker } = DatePicker;
const dateFormat = 'YYYY/MM/DD';
class Overview extends Component {
    state = {
        startTime:undefined,//开始时间
        endTime:undefined,  //结束时间
        labels:[],
        friendly:[],
        unfriendly:[],
        overall:[],
        typeClass: [],
        numClass :[],
        infoClass :[],
        chartList:[],
        classItems:[],
    }
    onPickerChange(a,dateString){
        this.setState({
            startTime:dateString[0].replace(/[/]/g,""),
            endTime:dateString[1].replace(/[/]/g,""),
        })

    }
    mixChartData(){
        let {startTime, endTime} = this.state
        axios.get('http://localhost:3000/overview/key_metrics_byday/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    labels:response.data.date,
                    friendly:response.data.friendly,
                    unfriendly:response.data.unfriendly,
                    overall:response.data.overall,
                })
            },
            error => {console.log("Mix Group request error")}
        )
    }
    pieChartData(){
        let {startTime, endTime} = this.state
        axios.get('http://localhost:3000/overview/key_metrics/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    typeClass:response.data.info.filter(val=>val.type!='Total').map(val => val.type),
                    numClass:response.data.info.filter(val=>val.type!='Total').map(val => val.num),
                    infoClass:response.data.info.filter(val=>val.type!='Total').map((value) => {return{name: value.type,value:value.num}})
                })
            },
            error => {console.log("Pie request error")}
        )
    }
    panelGroupData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/overview/key_metrics/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    chartList : response.data.info
                })
            },
            error => {console.log("Panel Group request error")}
        )
    }

    boxCardData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/overview/type/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    classItems : response.data.items
                })
            },
            error => {console.log("Panel Group request error")}
        )
    }

    render() {
        console.log(this.state)
        return (
            <div >
                <div>
                    Please select time preiod:&nbsp;&nbsp;&nbsp;
                    <RangePicker
                        defaultValue={[moment('2019-09-03', dateFormat), moment('2019-11-22', dateFormat)]}
                        format={dateFormat}
                        onChange = {(a,b) =>{this.onPickerChange(a,b);this.mixChartData();this.pieChartData();this.panelGroupData();this.boxCardData()}}
                        placeholder={['Start Time','End Time']}
                        allowClear = {false}
                    />
                </div>
                <div className="chart-wrapper">
                    <h1>Twitter Cyberbullying Analysis: </h1>
                    <Row gutter={8}>
                        <Col  xs={24} sm={24} md={24} lg={12} xl={12}
                              style={{paddingRight: "8px" }}>
                            <div className="chart-wrapper">
                                <PanelGroup {...this.state}/>
                            </div>
                        </Col>
                        <Col  xs={24} sm={24} md={24} lg={12} xl={10} style={{paddingRight: "8px"}}>
                            <div className="chart-wrapper">
                                <PieChart {...this.state}/>
                            </div>
                        </Col>

                    </Row>
                    <h1>Twitter Cyberbullying Analysis: </h1>
                    <MixChart {...this.state}/>

                    <h1>Twitter Cyberbullying Analysis: </h1>
                    <BoxCard {...this.state}/>
                    <br />
                    <h1>Twitter Cyberbullying Analysis: </h1>
                    <BarChart />
                    <h1>Twitter Cyberbullying Analysis: </h1>
                    <LineChart />



                    <br />
                    <br />
                    <br />
                    <br />
                    <br />
                    <br />

                </div>


            </div>
        );
    }
}

export default Overview;