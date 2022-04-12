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
        positive:[],
        negative:[],
        neutral:[],
        overall:[],
        typeClass: [],
        numClass :[],
        infoClass :[],
        chartList:[],
        classItems:[],
        country:[],
        positive_country:[],
        negative_country:[],
        neutral_country:[],

    }
    onPickerChange(a,dateString){
      setTimeout(()=>{
            this.setState({
                  startTime:dateString[0].replace(/[/]/g,""),
                  endTime:dateString[1].replace(/[/]/g,""),
            });
            this.mixChartData();this.pieChartData();this.panelGroupData();this.boxCardData();this.barChartData()
        },0)
    }

    mixChartData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/api/timeselector/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    labels:response.data.date,
                    positive:response.data.positive,
                    negative:response.data.negative,
                    neutral:response.data.neutral,
                    overall:response.data.overall,
                })
                console.log(this.state)
            },
            error => {console.log("Mix Group request error")}
        )
    }
    pieChartData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/api/timeselector/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    typeClass:response.data.total.map(val => val.type),
                    numClass:response.data.total.map(val => val.num),
                    infoClass:response.data.total.map((value) => {return{name: value.type,value:value.num}})
                })
            },
            error => {console.log("Pie request error")}
        )
    }
    panelGroupData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/api/timeselector/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    chartList: response.data.total
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

    barChartData(){
        const {startTime, endTime} = this.state
        axios.get('http://localhost:3000/api/country/'+startTime+'_'+endTime).then(
            response => {
                this.setState({
                    country : response.data.country,
                    positive_coutry : response.data.positive,
                    negative_country : response.data.negative,
                    neutral_country : response.data.neutral
                })
            },
            error => {console.log("Panel Group request error")}
        )
    }

    render() {
        const disabledDates = [
          {
            start: "2021-07-01",
            end: "2021-12-31"
          }
        ];
        return (
            <div >
                <div>
                    Please select time preiod:&nbsp;&nbsp;&nbsp;
                    <RangePicker
                        defaultValue={[moment('2021-07-01', dateFormat), moment('2021-07-07', dateFormat)]}
                        format={dateFormat}
                        onChange = {(a,b) =>{this.onPickerChange(a,b)}}
                        placeholder={['Start Time','End Time']}
                        allowClear = {false}
                         disabledDate={current => {
                            console.log(current);
                            return disabledDates.some(date =>
                              !current.isBetween(
                                moment(date["start"], dateFormat),
                                moment(date["end"], dateFormat)
                              )
                            );
                          }}
                    />
                </div>
                <div className="chart-wrapper">
                    <h1>Data summary: </h1>
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

                    <h1>Country-based Twitter Sentiment Ratio by Day: </h1>
                    <LineChart {...this.state}/>
                    <br />
                    <h1>Twitter Sentiment Change By Day: </h1>
                    <MixChart {...this.state}/>






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